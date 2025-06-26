import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

export default function LessonsList() {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState('');
  const [showSearch, setShowSearch] = useState(false);

  useEffect(() => {
    setLoading(true);
    axios.get('/api/v1/lessons', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    })
      .then(res => {
        setLessons(res.data);
        setLoading(false);
      })
      .catch(() => {
        setError('Could not load lessons.');
        setLoading(false);
      });
  }, []);

  const filtered = lessons.filter(l => l.title.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="max-w-6xl mx-auto p-4">
      <div className="flex items-center mb-4">
        <h2 className="text-2xl font-bold flex-1">Lessons</h2>
        <button
          className="px-3 py-1 rounded bg-gray-200 dark:bg-gray-700 text-sm ml-2"
          onClick={() => setShowSearch(s => !s)}
        >
          {showSearch ? 'Hide Search' : 'Search'}
        </button>
      </div>
      {showSearch && (
        <input
          type="text"
          placeholder="Search by title..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          className="w-full mb-4 px-3 py-2 border rounded dark:bg-gray-700"
        />
      )}
      {loading && <div>Loading lessons...</div>}
      {error && <div className="text-red-500">{error}</div>}
      <div className="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
        {filtered.map(lesson => (
          <div
            key={lesson.id}
            className="bg-white dark:bg-gray-800 rounded shadow p-4 flex flex-col transition-transform transform hover:-translate-y-1 hover:shadow-lg duration-200"
          >
            <div className="font-bold text-lg mb-2">{lesson.title}</div>
            {lesson.image_path && (
              <img src={lesson.image_path} alt="Lesson visual" className="mb-2 max-h-32 object-cover rounded" />
            )}
            <div className="text-gray-600 dark:text-gray-300 text-sm mb-4">
              {lesson.snippet || 'No description available.'}
            </div>
            <Link
              to={`/lesson/${lesson.id}`}
              className="mt-auto px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
            >
              Start Lesson
            </Link>
          </div>
        ))}
      </div>
      {!loading && filtered.length === 0 && <div className="mt-8 text-center text-gray-500">No lessons found.</div>}
    </div>
  );
} 