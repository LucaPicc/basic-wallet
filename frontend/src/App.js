import './App.css';

import { Route, Routes } from 'react-router-dom';

import HomePage from './pages/home';
import LoginPage from './pages/login';
import Transaction from 'pages/transaction';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<LoginPage />} />
        <Route path="home" element={<HomePage />} />
        <Route path="transaction" element={<Transaction/>}>
          <Route path=":transaction" element={<Transaction/>}/>
        </Route>
        <Route path="*" element={<div>Not Found</div>}/>
      </Routes>
    </div>
  );
}

export default App;
