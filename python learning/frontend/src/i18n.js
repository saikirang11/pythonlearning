import React, { createContext, useContext, useState } from 'react';

const translations = {
  en: {
    dashboard: 'Dashboard',
    lessons: 'Lessons',
    admin: 'Admin',
    dark_mode: 'Dark Mode',
    light_mode: 'Light Mode',
    lesson_page: 'Lesson Page',
    admin_dashboard: 'Admin Dashboard',
    admin_upload: 'Admin Upload',
    // ...add more keys as needed
  },
  // Add more languages here
};

const I18nContext = createContext();

export function I18nProvider({ children }) {
  const [lang, setLang] = useState('en');
  const t = (key) => translations[lang][key] || key;
  return (
    <I18nContext.Provider value={{ lang, setLang, t }}>
      {children}
    </I18nContext.Provider>
  );
}

export function useI18n() {
  return useContext(I18nContext);
} 