import './index.css';

import App from './App';
import { BrowserRouter } from 'react-router-dom';
import { CookiesProvider } from 'react-cookie';
import React from 'react';
import ReactDOM from 'react-dom/client';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <CookiesProvider>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </CookiesProvider>
  </React.StrictMode>
);

