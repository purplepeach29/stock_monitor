
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Watchlist: React.FC = () => {
  const [watchlistData, setWatchlistData] = useState<{ [symbol: string]: number }>({});

  useEffect(() => {
    const fetchWatchlistData = async () => {
      try {
        const response = await axios.get('/api/watchlist/');
        setWatchlistData(response.data);
      } catch (error) {
        console.error('Fetch watchlist data error:', error);
      }
    };

    fetchWatchlistData();
  }, []);

  return (
    <div>
      <h2>Watchlist</h2>
      <ul>
        {Object.entries(watchlistData).map(([symbol, value]) => (
          <li key={symbol}>
            {symbol}: {value}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Watchlist;
