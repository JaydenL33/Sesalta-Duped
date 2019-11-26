import React from "react";
import "./App.css";
import NavBar from "./components/Navbar";
import Routes from "./Routes";
import { BrowserRouter } from "react-router-dom";
// import firebase from "firebase";

class App extends React.Component {
  constructor(props: any) {
    super(props);

    this.state = {
      authUser: null
    };
  }

  public render() {
    return (
      <div className="App">
        {/* put Browser Router outside so we can use 'Link' everywhere in the app */}
        <BrowserRouter>
          <NavBar />
          <Routes />
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
