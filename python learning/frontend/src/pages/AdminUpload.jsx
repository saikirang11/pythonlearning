import React, { useState } from 'react';
import axios from 'axios';

export default function AdminUpload() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [code, setCode] = useState('');
  const [videoUrl, setVideoUrl] = useState('');
  const [pdf, setPdf] = useState(null);
  const [pdfNotes, setPdfNotes] = useState('');
  const [image, setImage] = useState(null);
  const [imagePrompt, setImagePrompt] = useState('');
  const [status, setStatus] = useState('');
  const [loading, setLoading] = useState(false);

  const handlePdfUpload = async (e) => {
    const file = e.target.files[0];
    setPdf(file);
    setPdfNotes('');
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append('pdf', file);
    try {
      const res = await axios.post('/api/v1/admin/upload-pdf', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      });
      setPdfNotes(res.data.extracted_text);
      setStatus('PDF uploaded and notes extracted.');
    } catch {
      setStatus('Failed to extract PDF notes.');
    }
    setLoading(false);
  };

  const handleLessonSubmit = async (e) => {
    e.preventDefault();
    setStatus('');
    setLoading(true);
    const formData = new FormData();
    formData.append('title', title);
    formData.append('content', content);
    formData.append('notes', pdfNotes);
    formData.append('code', code);
    formData.append('video_url', videoUrl);
    formData.append('image_prompt', imagePrompt || content);
    if (pdf) formData.append('pdf_path', pdf.name);
    if (image) formData.append('image', image);
    try {
      await axios.post('/api/v1/admin/lesson', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `Bearer ${localStorage.getItem('token')}`
        }
      });
      setStatus('Lesson uploaded successfully!');
      setTitle(''); setContent(''); setCode(''); setVideoUrl(''); setPdf(null); setPdfNotes(''); setImage(null); setImagePrompt('');
    } catch {
      setStatus('Failed to upload lesson.');
    }
    setLoading(false);
  };

  return (
    <div className="max-w-2xl mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">Admin Upload</h2>
      <form onSubmit={handleLessonSubmit} className="space-y-4 bg-white dark:bg-gray-800 rounded shadow p-4">
        <input type="text" placeholder="Title" value={title} onChange={e => setTitle(e.target.value)} className="w-full px-3 py-2 border rounded dark:bg-gray-700" required />
        <textarea placeholder="Content" value={content} onChange={e => setContent(e.target.value)} className="w-full px-3 py-2 border rounded dark:bg-gray-700" required />
        <textarea placeholder="Code" value={code} onChange={e => setCode(e.target.value)} className="w-full px-3 py-2 border rounded dark:bg-gray-700" />
        <input type="text" placeholder="Video URL" value={videoUrl} onChange={e => setVideoUrl(e.target.value)} className="w-full px-3 py-2 border rounded dark:bg-gray-700" />
        <input type="file" accept="application/pdf" onChange={handlePdfUpload} className="w-full" />
        {pdfNotes && <textarea value={pdfNotes} readOnly className="w-full px-3 py-2 border rounded dark:bg-gray-700" placeholder="Extracted PDF Notes" />}
        <input type="file" accept="image/*" onChange={e => setImage(e.target.files[0])} className="w-full" />
        <input type="text" placeholder="Image Prompt (optional)" value={imagePrompt} onChange={e => setImagePrompt(e.target.value)} className="w-full px-3 py-2 border rounded dark:bg-gray-700" />
        <button type="submit" className="w-full px-4 py-2 bg-blue-600 text-white rounded" disabled={loading}>{loading ? 'Uploading...' : 'Upload Lesson'}</button>
        {status && <div className="mt-2 text-center text-sm text-blue-600 dark:text-blue-400">{status}</div>}
      </form>
    </div>
  );
} 