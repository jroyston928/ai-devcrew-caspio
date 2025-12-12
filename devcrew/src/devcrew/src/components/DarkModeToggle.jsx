import React from 'react';

const DarkModeToggle = ({ darkMode, setDarkMode }) => {
  return (
    <button onClick={() => setDarkMode(!darkMode)}>
      {darkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
    </button>
  );
};

export default DarkModeToggle;