import React, { useState } from "react";
import "./App.css";
import NavBar from "./components/Navbar";
import Routes from "./Routes";
import { BrowserRouter } from "react-router-dom";

const App: React.FC = () => {
  const [isAuthenticated, setAuthenticated] = useState(true); // should be false if we have login stuff

  return (
    <div className="App">
      {/* put Browser Router outside so we can use 'Link' everywhere in the app */}
      <BrowserRouter>
        <NavBar />
        <Routes appProps={{ isAuthenticated, setAuthenticated }} />
      </BrowserRouter>
    </div>
  );
};

export default App;
