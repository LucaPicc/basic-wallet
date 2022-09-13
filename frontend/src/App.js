import './App.css';

import { Route, Routes } from 'react-router-dom';

import { AccountContextProvider } from 'context/account-context';
import CreateAccountPage from 'pages/create-account';
import HomePage from './pages/home';
import LoginPage from './pages/login';
import Transaction from 'pages/transaction';
import ValidatePage from 'pages/validate';

function App() {
  return (
    <AccountContextProvider>    
      <div className="App">
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/create-account/" element={<CreateAccountPage />} />
          <Route path="/home/" element={<HomePage />} />
          <Route path="/transaction/" element={<Transaction/>}>
            <Route path=":transaction" element={<Transaction/>}/>
          </Route>
          <Route path="/validate/" element={<ValidatePage/>}>
            <Route path="/validate/:code" element={<ValidatePage/>}/>
          </Route>
          <Route path="*" element={<div>Not Found</div>}/>
        </Routes>
      </div>
    </AccountContextProvider>
  );
}

export default App;
