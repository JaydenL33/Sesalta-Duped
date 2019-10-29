import React from 'react';
// import logo from './logo.svg';
import './App.css';

import NavBar from './components/Navbar';
import QuizElement from './components/quiz_questions/QuizElement';
import SelectCountryOnMap from './components/quiz_questions/SelectCountryOnMap'
import SelectCountryFromMap from './components/quiz_questions/SelectCountryFromMap'
import AnswerComponent from "./components/quiz_questions/AnswerComponent";


const App: React.FC = () => {
  return (
    <div className="App">
      <NavBar/>
      <SelectCountryFromMap/>
      <SelectCountryOnMap/>
    </div>
  );
}

export default App;
