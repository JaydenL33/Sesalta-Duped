import React, { useState }  from 'react';
// import logo from './logo.svg';
import './App.css';
import NavBar from './components/Navbar';

import Routes from "./Routes";

const App: React.FC = () => {
  const [isAuthenticated, setAuthenticated] = useState(true); // should be false if we have login stuff

  return (
    <div className="App">
      <NavBar/>
      <Routes appProps={{ isAuthenticated, setAuthenticated }} />
    </div>
  );
}

export default App;
