import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
// For code highlighting
import 'prismjs/themes/prism.css';
import Prism from 'prismjs';

const tabs = [
  { key: 'content', label: 'Content' },
  { key: 'code', label: 'Code' },
  { key: 'notes', label: 'Notes' },
  { key: 'quiz', label: 'Quiz' },
  { key: 'video', label: 'Video' },
  { key: 'discussions', label: 'Discussions' },
];

export default function LessonPage() {
  const { id } = useParams();
  const [active, setActive] = useState('content');
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [copied, setCopied] = useState(false);
  const [codeOutput, setCodeOutput] = useState('');
  const [codeError, setCodeError] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [pyodide, setPyodide] = useState(null);
  const [quiz, setQuiz] = useState([]);
  const [quizLoading, setQuizLoading] = useState(false);
  const [quizError, setQuizError] = useState(null);
  const [answers, setAnswers] = useState({});
  const [feedback, setFeedback] = useState(null);
  const [discussions, setDiscussions] = useState([]);
  const [discussionLoading, setDiscussionLoading] = useState(false);
  const [discussionError, setDiscussionError] = useState(null);
  const [newComment, setNewComment] = useState('');
  const [posting, setPosting] = useState(false);

  useEffect(() => {
    setLoading(true);
    axios.get(`/api/v1/lesson/${id}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    })
      .then(res => {
        setLesson(res.data);
        setLoading(false);
      })
      .catch(err => {
        setError('Could not load lesson.');
        setLoading(false);
      });
  }, [id]);

  useEffect(() => {
    if (active === 'code') {
      Prism.highlightAll();
    }
  }, [active, lesson]);

  useEffect(() => {
    if (active === 'quiz') {
      setQuizLoading(true);
      setQuizError(null);
      axios.get(`/api/v1/quiz/${id}`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
        .then(res => {
          setQuiz(res.data);
          setQuizLoading(false);
        })
        .catch(() => {
          setQuizError('Could not load quiz.');
          setQuizLoading(false);
        });
    }
  }, [active, id]);

  useEffect(() => {
    // Load Pyodide
    const loadPyodide = async () => {
      try {
        const pyodideModule = await import('pyodide');
        const pyodideInstance = await pyodideModule.loadPyodide();
        setPyodide(pyodideInstance);
      } catch (err) {
        console.error('Failed to load Pyodide:', err);
      }
    };
    loadPyodide();
  }, []);

  useEffect(() => {
    if (active === 'discussions') {
      setDiscussionLoading(true);
      setDiscussionError(null);
      axios.get(`/api/v1/lesson/${id}/discussions`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      })
        .then(res => {
          setDiscussions(res.data);
          setDiscussionLoading(false);
        })
        .catch(() => {
          setDiscussionError('Could not load discussions.');
          setDiscussionLoading(false);
        });
    }
  }, [active, id]);

  const runCode = async () => {
    if (!pyodide) {
      setCodeError('Python runtime not loaded yet. Please wait...');
      return;
    }
    setIsRunning(true);
    setCodeOutput('');
    setCodeError('');
    try {
      const result = await pyodide.runPythonAsync(lesson.code);
      setCodeOutput(result || 'Code executed successfully!');
    } catch (err) {
      setCodeError(err.toString());
    }
    setIsRunning(false);
  };

  const handleQuizChange = (qid, value) => {
    setAnswers(a => ({ ...a, [qid]: value }));
  };

  const handleQuizSubmit = (e) => {
    e.preventDefault();
    setFeedback(null);
    axios.post('/api/v1/quiz/submit', {
      lesson_id: id,
      answers
    }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    })
      .then(res => setFeedback(res.data))
      .catch(() => setFeedback({ error: 'Could not submit quiz.' }));
  };

  const handlePostComment = async (e) => {
    e.preventDefault();
    if (!newComment.trim()) return;
    setPosting(true);
    try {
      await axios.post(`/api/v1/lesson/${id}/discussions`, {
        message: newComment
      }, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      });
      setNewComment('');
      // Refresh discussions
      const res = await axios.get(`/api/v1/lesson/${id}/discussions`, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      });
      setDiscussions(res.data);
    } catch {
      setDiscussionError('Failed to post comment.');
    }
    setPosting(false);
  };

  if (loading) return <div className="p-4">Loading...</div>;
  if (error) return <div className="p-4 text-red-500">{error}</div>;
  if (!lesson) return null;

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-2">{lesson.title}</h1>
      <div className="flex border-b mb-4 dark:border-gray-700">
        {tabs.map(tab => (
          <button
            key={tab.key}
            className={`px-4 py-2 -mb-px border-b-2 focus:outline-none transition-colors ${active === tab.key ? 'border-blue-500 text-blue-600 dark:text-blue-400' : 'border-transparent text-gray-500 dark:text-gray-300'}`}
            onClick={() => setActive(tab.key)}
          >
            {tab.label}
          </button>
        ))}
      </div>
      <div className="bg-white dark:bg-gray-800 rounded shadow p-4 min-h-[200px]">
        {active === 'content' && (
          <div>
            <p className="mb-4">{lesson.content}</p>
            {lesson.image_path && <img src={lesson.image_path} alt="Lesson visual" className="mb-4 max-w-xs rounded shadow" />}
            <div className="flex justify-between mt-8">
              <button className="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded">&larr; Previous</button>
              <button className="px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded">Next &rarr;</button>
            </div>
          </div>
        )}
        {active === 'code' && (
          <div>
            <pre className="relative bg-gray-900 text-white rounded p-4 overflow-x-auto">
              <code className="language-python">{lesson.code}</code>
              <button
                className="absolute top-2 right-2 px-2 py-1 bg-blue-500 text-xs text-white rounded"
                onClick={() => {
                  navigator.clipboard.writeText(lesson.code);
                  setCopied(true);
                  setTimeout(() => setCopied(false), 1000);
                }}
              >
                {copied ? 'Copied!' : 'Copy'}
              </button>
            </pre>
            <div className="mt-4 space-y-2">
              <button 
                className="px-4 py-2 bg-green-600 text-white rounded disabled:opacity-50" 
                onClick={runCode}
                disabled={isRunning || !pyodide}
              >
                {isRunning ? 'Running...' : 'Try it Yourself'}
              </button>
              {codeOutput && (
                <div className="bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 p-3 rounded">
                  <strong>Output:</strong><br />
                  <pre className="whitespace-pre-wrap">{codeOutput}</pre>
                </div>
              )}
              {codeError && (
                <div className="bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200 p-3 rounded">
                  <strong>Error:</strong><br />
                  <pre className="whitespace-pre-wrap">{codeError}</pre>
                </div>
              )}
            </div>
          </div>
        )}
        {active === 'notes' && <div>{lesson.notes || 'No notes available.'}</div>}
        {active === 'quiz' && (
          <div>
            {quizLoading && <div>Loading quiz...</div>}
            {quizError && <div className="text-red-500">{quizError}</div>}
            {!quizLoading && !quizError && quiz.length > 0 && !feedback && (
              <form onSubmit={handleQuizSubmit} className="space-y-6">
                {quiz.map(q => (
                  <div key={q.id} className="mb-4">
                    <div className="font-semibold mb-2">{q.question}</div>
                    {q.options && Array.isArray(q.options) && q.options.map(opt => (
                      <label key={opt} className="block">
                        <input
                          type="radio"
                          name={`quiz-${q.id}`}
                          value={opt}
                          checked={answers[q.id] === opt}
                          onChange={() => handleQuizChange(q.id, opt)}
                          className="mr-2"
                        />
                        {opt}
                      </label>
                    ))}
                  </div>
                ))}
                <button type="submit" className="px-4 py-2 bg-blue-600 text-white rounded">Submit</button>
              </form>
            )}
            {feedback && (
              <div className="mt-4">
                {feedback.error && <div className="text-red-500">{feedback.error}</div>}
                {feedback.feedback && (
                  <div>
                    <div className="font-bold mb-2">Score: {feedback.score}</div>
                    {feedback.feedback.map(fb => (
                      <div key={fb.quiz_id} className="mb-2">
                        <span className={fb.correct ? 'text-green-600' : 'text-red-600'}>
                          {fb.correct ? '✔ Correct' : '✖ Incorrect'}
                        </span>
                        {!fb.correct && fb.explanation && (
                          <div className="text-sm text-gray-500">{fb.explanation}</div>
                        )}
                      </div>
                    ))}
                  </div>
                )}
                <button className="mt-2 px-4 py-2 bg-gray-200 dark:bg-gray-700 rounded" onClick={() => { setFeedback(null); setAnswers({}); }}>Try Again</button>
              </div>
            )}
            {!quizLoading && !quizError && quiz.length === 0 && <div>No quiz available for this lesson.</div>}
          </div>
        )}
        {active === 'video' && lesson.video_url && (
          <div className="aspect-w-16 aspect-h-9">
            <iframe
              src={lesson.video_url}
              title="Lesson Video"
              allowFullScreen
              className="w-full h-64 rounded"
            ></iframe>
          </div>
        )}
        {active === 'discussions' && (
          <div>
            <form onSubmit={handlePostComment} className="mb-4">
              <textarea
                value={newComment}
                onChange={e => setNewComment(e.target.value)}
                placeholder="Add a comment..."
                className="w-full px-3 py-2 border rounded dark:bg-gray-700 mb-2"
                rows="3"
              />
              <button
                type="submit"
                disabled={posting || !newComment.trim()}
                className="px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50"
              >
                {posting ? 'Posting...' : 'Post Comment'}
              </button>
            </form>
            {discussionLoading && <div>Loading discussions...</div>}
            {discussionError && <div className="text-red-500 mb-4">{discussionError}</div>}
            {!discussionLoading && !discussionError && discussions.length === 0 && (
              <div className="text-gray-500">No comments yet. Be the first to comment!</div>
            )}
            {discussions.map(d => (
              <div key={d.id} className="mb-4 p-3 bg-gray-50 dark:bg-gray-700 rounded">
                <div className="flex justify-between items-start mb-2">
                  <span className="font-semibold text-blue-600 dark:text-blue-400">{d.username}</span>
                  <span className="text-xs text-gray-500">{d.created_at}</span>
                </div>
                <div className="text-gray-800 dark:text-gray-200">{d.message}</div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
} 