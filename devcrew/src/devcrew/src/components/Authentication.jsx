import React, { useState } from 'react';
import axios from 'axios';

const Authentication = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${process.env.REACT_APP_CASPIO_API_URL}/login`, { email, password });
      // Handle successful login (e.g., store user data)
    } catch (err) {
      setError('Invalid credentials');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input type='email' value={email} onChange={(e) => setEmail(e.target.value)} placeholder='Email' required />
        <input type='password' value={password} onChange={(e) => setPassword(e.target.value)} placeholder='Password' required />
        <button type='submit'>Login</button>
      </form>
      {error && <p>{error}</p>}
    </div>
  );
};

export default Authentication;