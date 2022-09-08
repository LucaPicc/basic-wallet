import './App.css';

import { Route, Routes } from 'react-router-dom';

import { AuthContextProvider } from './context/auth-context';
import HomePage from './pages/home';
import LoginPage from './pages/login';

function App() {
  return (
    <div className="App">
    <AuthContextProvider>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="home" element={<HomePage />} />
        <Route path="*" element={<div>Not Found</div>}/>
      </Routes>
    </AuthContextProvider>
    </div>
  );
}

export default App;
