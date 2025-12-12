import React, { useState, useEffect } from 'react';
import Authentication from './components/Authentication';
import Search from './components/Search';
import DarkModeToggle from './components/DarkModeToggle';
import { registerSW } from 'virtual:pwa-register';

const App = () => {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    const savedMode = localStorage.getItem('darkMode');
    if (savedMode) {
      setDarkMode(JSON.parse(savedMode));
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('darkMode', darkMode);
  }, [darkMode]);

  // Register PWA service worker
  registerSW();

  return (
    <div className={darkMode ? 'bg-gray-900 text-white' : 'bg-white text-black'}>
      <DarkModeToggle darkMode={darkMode} setDarkMode={setDarkMode} />
      <Authentication />
      <Search />
    </div>
  );
};

export default App;