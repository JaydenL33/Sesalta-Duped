import React from 'react';
import SelectCountryFromFlag from '../components/quiz_questions/SelectCountryFromFlag';

interface Country {
  name: string;
  iso_a2: string;
}

interface P {}

interface S {
  gameID: string;
  optionsList: Country[];
  countryExpected?: Country;
  needNext: boolean;
}

export default class GamePlayPageFlag extends React.Component<P, S> {
  constructor(props: P) {
    super(props);
    this.state = {
      gameID: '',
      optionsList: [],
      countryExpected: undefined,
      needNext: false, // need to get next question or not
    };
  }

  getCountries(optionlist: any) {
    let res: any[] = [];
    optionlist.forEach((item: { name: string; iso_a2: string }) => {
      res.push({
        name: item.name,
        iso_a2: item.iso_a2,
      });
    });
    return res;
  }

  async componentDidMount() {
    try {
      const id: string = await this.getGameID();
      console.log(id);
      this.setState({ gameID: id });

      const ops: [] = await this.getRandomCountryOptions();
      const countrylist: Country[] = this.getCountries(ops);
      console.log(countrylist);
      this.setState({
        optionsList: countrylist,
        countryExpected:
          countrylist[Math.floor(Math.random() * countrylist.length)],
      });
    } catch (e) {
      console.log(e);
    }
  }

  /*
    get game id for this game
  */
  getGameID(): Promise<string> {
    const url = 'http://127.0.0.1:5000/api/country/new_game/';
    return fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response: any) => response.json())
      .then((response: any) => {
        console.log(response);
        return response;
      })
      .catch(e => {
        console.log(e);
      });
  }

  /*
    get random options
  */
  getRandomCountryOptions() {
    const url = `http://127.0.0.1:5000/api/country/random/?amount=4&id=${this.state.gameID}`;
    return fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response: any) => response.json())
      .then((response: any) => {
        console.log(response);
        return response;
      })
      .catch(e => {
        console.log(e);
      });
  }

  nextQuestionPlsCallback = async () => {
    // this.setState({ needNext: next })
    try {
      const ops: [] = await this.getRandomCountryOptions();
      const countrylist: Country[] = this.getCountries(ops);
      console.log(countrylist);
      this.setState({
        optionsList: countrylist,
        countryExpected:
          countrylist[Math.floor(Math.random() * countrylist.length)],
      });
    } catch (e) {
      console.log(e);
    }
  };

  render() {
    if (this.state.gameID !== '') {
      return (
        <div>
          <SelectCountryFromFlag
            gameID={this.state.gameID}
            countryExpected={this.state.countryExpected}
            optionsList={this.state.optionsList}
            callback={this.nextQuestionPlsCallback}
          />
        </div>
      );
    } else {
      return null;
    }
  }
}
