import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

function App() {
  const [realtimeOutput, setRealtimeOutput] = useState('');

  useEffect(() => {
    const socket = io('http://localhost:5000');

    socket.on('connect', () => {
      console.log('Connected to server');
    });

    socket.on('realtime_output', data => {
      setRealtimeOutput(data.output);
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div className="App">
      <h1>Real-time Output Display</h1>
      <p>Real-time Output from Python: {realtimeOutput}</p>
    </div>
  );
}

export default App;
