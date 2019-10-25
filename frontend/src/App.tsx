import React from 'react';
// import logo from './logo.svg';
import './App.css';

import NavBar from './components/Navbar';
import QuizElement from './components/QuizElement';

const App: React.FC = () => {
	return (
		<div className="App">
			<NavBar />
			<QuizElement />

		</div>
	);
}

export default App;
