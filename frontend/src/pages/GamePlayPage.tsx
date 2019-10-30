// import QuizElement from '../components/quiz_questions/QuizElement';
import React from 'react';
import SelectCountryFromMap from '../components/quiz_questions/SelectCountryFromMap'
// import AnswerComponent from "../components/quiz_questions/AnswerComponent";


interface P {

}

interface S {
  gameID: string,
}

export default class GamePlayPage extends React.Component<P, S> {
  constructor(props: P) {
    super(props);
    this.state = {
      gameID: "",
    }
  }

  async componentDidMount() {
    try {
      const res: string = await this.getGameID();
      console.log(res);
      this.setState({ gameID: res });
    } catch (e) {
      console.log(e);
    }
  }

  /*
    get game id for this game
  */
  getGameID(): Promise<string> {
    const url = "http://127.0.0.1:5000/api/country/new_game/"
    return fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response: any) => response.json())
    .then((response: any) => {
      console.log(response);
      return response;
    })
    .catch((e) => {
      console.log(e);
    });
  }

  render() {
    if (this.state.gameID !== "") {
      return (
        <div>
          <SelectCountryFromMap gameID={this.state.gameID}/>
        </div>
      )
    } else {
      return null
    }
  }
}

