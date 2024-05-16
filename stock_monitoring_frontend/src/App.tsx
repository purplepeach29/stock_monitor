import React from 'react';
import './App.css';
//import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { CssBaseline, ThemeProvider, createTheme, Box, Container } from '@mui/material';
import LoginForm from './LoginForm';
import RegistrationForm from './RegistrationForm';

import StockMonitoring from './StockMonitoring';
import Watchlist from './Watchlist';

const theme = createTheme();
const App: React.FC = () => {
  return (
    <Container maxWidth="md">
      <Box sx={{  marginTop: 4, textAlign:  'center'}}>
    <ThemeProvider theme={theme}>
      < CssBaseline />
    
    <div className='Appbox'>
      <LoginForm />
      <RegistrationForm />
    </div>
    </ThemeProvider>
    </Box>
    </Container>
  );
};

export default App;
