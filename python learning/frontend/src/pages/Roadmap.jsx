import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';

export default function Roadmap() {
  const [roadmap, setRoadmap] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    axios.get('/api/v1/roadmap', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    })
      .then(res => {
        setRoadmap(res.data);
        setLoading(false);
      })
      .catch(() => {
        setError('Could not load roadmap.');
        setLoading(false);
      });
  }, []);

  return (
    <div className="max-w-3xl mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Python Learning Roadmap</h2>
      {loading && <div>Loading roadmap...</div>}
      {error && <div className="text-red-500">{error}</div>}
      {roadmap && (
        <div className="prose dark:prose-invert max-w-none">
          <ReactMarkdown>{roadmap.content}</ReactMarkdown>
        </div>
      )}
    </div>
  );
} 