import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { I18nProvider, useI18n } from './i18n';
import LessonPage from './pages/LessonPage';
import Login from './pages/Login';
import Register from './pages/Register';
import Roadmap from './pages/Roadmap';

function Dashboard() {
  return <div className="p-4">Dashboard (Student)</div>;
}
function LessonsList() {
  return <div className="p-4">Lessons List</div>;
}
function AdminDashboard() {
  return <div className="p-4">Admin Dashboard</div>;
}
function AdminUpload() {
  return <div className="p-4">Admin Upload</div>;
}

function NavBar({ dark, setDark, isLoggedIn, isAdmin, onLogout }) {
  const { lang, setLang, t } = useI18n();
  return (
    <nav className="flex gap-4 p-4 border-b dark:border-gray-700">
      <Link to="/">{t('dashboard')}</Link>
      <Link to="/roadmap">Roadmap</Link>
      <Link to="/lessons">{t('lessons')}</Link>
      {isAdmin && <Link to="/admin">{t('admin')}</Link>}
      {!isLoggedIn && <Link to="/login">Login</Link>}
      {!isLoggedIn && <Link to="/register">Register</Link>}
      {isLoggedIn && <button onClick={onLogout} className="ml-2 text-red-500">Logout</button>}
      <button className="ml-auto" onClick={() => setDark(d => !d)}>
        {dark ? '🌙' : '☀️'}
      </button>
      <select
        className="ml-2 bg-transparent border rounded dark:border-gray-600"
        value={lang}
        onChange={e => setLang(e.target.value)}
      >
        <option value="en">EN</option>
        {/* Add more languages here */}
      </select>
    </nav>
  );
}

export default function App() {
  const [dark, setDark] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token'));
  const [isAdmin, setIsAdmin] = useState(localStorage.getItem('is_admin') === 'true');

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('is_admin');
    setIsLoggedIn(false);
    setIsAdmin(false);
    window.location.href = '/';
  };

  useEffect(() => {
    setIsLoggedIn(!!localStorage.getItem('token'));
    setIsAdmin(localStorage.getItem('is_admin') === 'true');
  }, []);

  return (
    <I18nProvider>
      <div className={dark ? 'dark bg-gray-900 min-h-screen text-white' : 'bg-white min-h-screen text-gray-900'}>
        <Router>
          <NavBar dark={dark} setDark={setDark} isLoggedIn={isLoggedIn} isAdmin={isAdmin} onLogout={handleLogout} />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/lessons" element={<LessonsList />} />
            <Route path="/lesson/:id" element={<LessonPage />} />
            <Route path="/admin" element={<AdminDashboard />} />
            <Route path="/admin/upload" element={<AdminUpload />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/roadmap" element={<Roadmap />} />
          </Routes>
        </Router>
      </div>
    </I18nProvider>
  );
} 