import React, { useState, useEffect } from 'react';
import { Typography, List, ListItem, ListItemText, Box, Container, Button, TextField } from '@mui/material';
import axios from 'axios';

interface Stock {
  id: number;
  symbol: string;
  name: string;
}

const StockMonitoring: React.FC = () => {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [newStockSymbol, setNewStockSymbol] = useState<string>('');
  const [newStockName, setNewStockName] = useState<string>('');


  useEffect(() => {
    const fetchStocks = async () => {
      try {
        const response = await axios.get('/api/');
        setStocks(response.data);
      } catch (error) {
        console.error('Fetch stocks error:', error);
      }
    };

    fetchStocks();
  }, []);
    
  const addStock = async () => {
    try {
      const response = await axios.post('/api/add/',{
        symbol: newStockSymbol, 
        name: newStockName
      } );
      setStocks([...stocks, response.data]);
      setNewStockSymbol('');
      setNewStockName('');
    } catch (error) {
      console.error('Add stock error:', error);
    }
  };

  const deleteStock = async (id: number) => {
    try {
      await axios.delete(`/api/delete/${id}`);
      setStocks(stocks.filter(stock => stock.id !== id));
    } catch (error) {
      console.error('Delete stock error:', error);
    }
  };

  return (
    <Container maxWidth="md">
      <Box sx={{  marginTop: 4, textAlign:  'center'}}>

      
    <div>
      <Typography variant="h4" gutterBottom>Stock Monitoring Dashboard</Typography>
      <List>
        {stocks.map(stock => (
          <ListItem key={stock.id}>
            <ListItemText primary={stock.name} secondary={stock.symbol} />
            <Button variant="contained" color="secondary" onClick={() => deleteStock(stock.id)}>Delete</Button>

          </ListItem>
        ))}
      </List>
      <TextField
        label="New Stock Symbol"
        value={newStockSymbol}
        onChange={(e) => setNewStockSymbol(e.target.value)}
      />
      <TextField
        label="New Stock Name"
        type="newStockName"
        value={newStockName}
        onChange={(e) => setNewStockName(e.target.value)}
      />
      <Button variant="contained" color="primary" onClick={addStock}>Add Stock</Button>

    </div>
    </Box>
    </Container>
  );
};

export default StockMonitoring;