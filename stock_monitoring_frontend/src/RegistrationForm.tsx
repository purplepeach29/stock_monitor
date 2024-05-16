import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';
import axios from 'axios';

const RegistrationForm: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async () => {
    try {
        const response = await axios.post('/api/register/', { 
            username: username, 
            password: password 
          });
          console.log('Registration successful:', response.data);      // Optionally, handle successful registration
    } catch (error) {
      console.error('Registration error:', error);
    }
  };

  return (
    <form>
      <h4>Don't have an account? Signup here.</h4>
      <TextField
        label="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <TextField
        label="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <Button variant="contained" onClick={handleRegister}>Register</Button>
    </form>
  );
};

export default RegistrationForm;