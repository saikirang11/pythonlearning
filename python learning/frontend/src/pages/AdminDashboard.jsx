import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function AdminDashboard() {
  const [analytics, setAnalytics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [seeding, setSeeding] = useState(false);
  const [seedStatus, setSeedStatus] = useState('');

  useEffect(() => {
    setLoading(true);
    axios.get('/api/v1/admin/analytics', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    })
      .then(res => {
        setAnalytics(res.data);
        setLoading(false);
      })
      .catch(() => {
        setError('Could not load analytics.');
        setLoading(false);
      });
  }, []);

  const handleSeedData = async () => {
    setSeeding(true);
    setSeedStatus('');
    try {
      const res = await axios.post('/api/v1/admin/seed-data', {}, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      });
      setSeedStatus(`✅ ${res.data.msg}`);
      // Refresh analytics after seeding
      const analyticsRes = await axios.get('/api/v1/admin/analytics', {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      });
      setAnalytics(analyticsRes.data);
    } catch (err) {
      setSeedStatus('❌ Failed to seed sample data');
    }
    setSeeding(false);
  };

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Admin Dashboard</h2>
      
      {/* Seed Data Section */}
      <div className="mb-6 bg-white dark:bg-gray-800 rounded shadow p-4">
        <h3 className="text-lg font-semibold mb-2">Quick Setup</h3>
        <p className="text-gray-600 dark:text-gray-300 mb-3">
          Populate the database with sample Python lessons and quizzes to get started quickly.
        </p>
        <button
          onClick={handleSeedData}
          disabled={seeding}
          className="px-4 py-2 bg-green-600 text-white rounded disabled:opacity-50"
        >
          {seeding ? 'Creating Sample Data...' : 'Seed Sample Data'}
        </button>
        {seedStatus && (
          <div className="mt-2 text-sm">
            {seedStatus}
          </div>
        )}
      </div>

      {/* Analytics Section */}
      <div className="bg-white dark:bg-gray-800 rounded shadow p-4">
        <h3 className="text-lg font-semibold mb-4">Analytics</h3>
        {loading ? (
          <div>Loading analytics...</div>
        ) : error ? (
          <div className="text-red-500">{error}</div>
        ) : (
          <table className="w-full">
            <thead>
              <tr className="border-b dark:border-gray-700">
                <th className="p-2 text-left">Lesson ID</th>
                <th className="p-2 text-left">Views</th>
                <th className="p-2 text-left">Quiz Attempts</th>
              </tr>
            </thead>
            <tbody>
              {analytics.map(a => (
                <tr key={a.lesson_id} className="border-b dark:border-gray-700">
                  <td className="p-2">{a.lesson_id}</td>
                  <td className="p-2">{a.views}</td>
                  <td className="p-2">{a.quiz_attempts}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
} 