// import QuizElement from '../components/quiz_questions/QuizElement';
import React from 'react';
import SelectCountryOnMap from '../components/quiz_questions/SelectCountryOnMap'
import SelectCountryFromMap from '../components/quiz_questions/SelectCountryFromMap'
// import AnswerComponent from "../components/quiz_questions/AnswerComponent";

export default function GamePlayPage () {
  return <div>
          <SelectCountryFromMap />
          <SelectCountryOnMap />
        </div>
}

