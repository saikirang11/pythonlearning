import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

export default function Dashboard() {
  const [recent, setRecent] = useState([]);
  const [streak, setStreak] = useState(0);
  const [lastLesson, setLastLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    setLastLesson(localStorage.getItem('lastLesson'));
    setLoading(true);
    axios.get('/api/v1/progress', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    })
      .then(res => {
        setRecent(res.data.recent);
        setStreak(res.data.streak);
        setLoading(false);
      })
      .catch(() => {
        setError('Could not load dashboard data.');
        setLoading(false);
      });
  }, []);

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Welcome Back!</h2>
      <div className="mb-6 flex flex-col sm:flex-row gap-4">
        <div className="flex-1 bg-white dark:bg-gray-800 rounded shadow p-4">
          <div className="text-gray-500 dark:text-gray-300 text-sm mb-2">Current Streak</div>
          {loading ? (
            <div className="text-gray-400">Loading...</div>
          ) : (
            <div className="text-3xl font-bold text-blue-600 dark:text-blue-400">🔥 {streak} days</div>
          )}
        </div>
        <div className="flex-1 bg-white dark:bg-gray-800 rounded shadow p-4">
          <div className="text-gray-500 dark:text-gray-300 text-sm mb-2">Resume</div>
          {lastLesson ? (
            <button
              className="px-4 py-2 bg-green-600 text-white rounded"
              onClick={() => navigate(`/lesson/${lastLesson}`)}
            >
              Continue Lesson
            </button>
          ) : (
            <div className="text-gray-400">No lesson in progress.</div>
          )}
        </div>
      </div>
      <div className="bg-white dark:bg-gray-800 rounded shadow p-4">
        <div className="text-gray-500 dark:text-gray-300 text-sm mb-2">Recent Activity</div>
        {loading ? (
          <div className="text-gray-400">Loading...</div>
        ) : error ? (
          <div className="text-red-500">{error}</div>
        ) : recent.length === 0 ? (
          <div className="text-gray-400">No recent activity.</div>
        ) : (
          <ul>
            {recent.map(item => (
              <li key={item.id} className="mb-2 flex justify-between items-center">
                <Link to={`/lesson/${item.id}`} className="text-blue-600 dark:text-blue-400 hover:underline">
                  {item.title}
                </Link>
                <span className="text-xs text-gray-400">{item.date}</span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
} 