import React from "react";
import SelectCountryFromFlag from "../components/quiz_questions/SelectCountryFromFlag";
import axios from "axios";
import LinearDeterminate from '../components/LinearDeterminate';

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
  selectedIndex: number | undefined;
}

export default class GamePlayPageFlag extends React.Component<P, S> {
  constructor(props: P) {
    super(props);
    this.state = {
      gameID: "",
      optionsList: [],
      countryExpected: undefined,
      needNext: false, // need to get next question or not
      selectedIndex: undefined
    };
  }

  getCountries(optionlist: any) {
    let res: any[] = [];
    optionlist.forEach((item: { name: string; iso_a2: string }) => {
      res.push({
        name: item.name,
        iso_a2: item.iso_a2
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
        countryExpected: countrylist[this.getRandomIndex(countrylist)]
      });
    } catch (e) {
      console.log(e);
    }
  }

  /*
    get game id for this game
  */
  async getGameID(): Promise<string> {
    const url = `${process.env.REACT_APP_API_URL}/api/country/new_game/`;
    const response = await axios.get(url);
    return response.data;
  }

  /*
    get random options
  */
  async getRandomCountryOptions() {
    const url = `${process.env.REACT_APP_API_URL}/api/country/random/?amount=4&id=${this.state.gameID}`;
    const response = await axios.get(url);
    return response.data;
  }

  nextQuestionPlsCallback = async () => {
    // this.setState({ needNext: next })
    try {
      const ops: [] = await this.getRandomCountryOptions();
      const countrylist: Country[] = this.getCountries(ops);
      console.log(countrylist);
      this.setState({
        optionsList: countrylist,
        countryExpected: countrylist[this.getRandomIndex(countrylist)],
        selectedIndex: undefined
      });
    } catch (e) {
      console.log(e);
    }
  };

  indexCallback = (selectedIndex: number | undefined) => {
    console.log("oh");
    this.setState({ selectedIndex: selectedIndex });
  };

  getRandomIndex(countryList: Country[]) {
    return Math.floor(Math.random() * countryList.length);
  }

  render() {
  
    if (this.state.gameID !== "") {
      return (
        <div>
          <LinearDeterminate/>
          <SelectCountryFromFlag
            selectedIndex={this.state.selectedIndex}
            gameID={this.state.gameID}
            countryExpected={this.state.countryExpected}
            optionsList={this.state.optionsList}
            callback={this.nextQuestionPlsCallback}
            indexCallback={this.indexCallback}
          />
        </div>
      );
    } else {
      return null;
    }
  }
}
