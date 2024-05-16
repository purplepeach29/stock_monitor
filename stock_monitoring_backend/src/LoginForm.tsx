import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';
import axios from 'axios';
import Watchlist from './Watchlist';
import StockMonitoring from './StockMonitoring';
//import { Link, useNavigate} from 'react-router-dom';


const LoginForm: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
  //const navigate = useNavigate();

  const handleLogin = async () => {
    
      console.log({username, password})
      axios.post('/api/login/', { username, password})
      .then(response => {
        console.log('Login successful:', response.data);
        setIsLoggedIn(true);

        // Handle successful login
      })
      .catch(error => {
        console.error('Login error:', error);
        // Handle login error
      });
      
  };
 if (isLoggedIn) {
    return <StockMonitoring />;
  }
  return (
    <div>
    <form>
      <h4>Log in to view dashboard</h4>
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
      <Button variant="contained" onClick={handleLogin}>Login</Button>
      
    </form>
    </div>

  );
};

export default LoginForm;



