import React from "react";
import SelectCapitalOrCountry from "../components/quiz_questions/SelectCapitalOrCountry";
import axios from "axios";

interface P {
  match: any;
}

interface option {
  name: string;
  capital: string;
  iso_a2: string;
}

interface S {
  gameID: string;
  question: option;
  optionsList: option[];
  capitalList: string[];
  countryList: string[];
  needNext: boolean;
  mode: number;
  selectedIndex: number | undefined;
  randomIndexForOptions: number;
}

export default class GamePlayPageCapital extends React.Component<P, S> {
  constructor(props: P) {
    super(props);
    this.state = {
      gameID: "",
      optionsList: [], // list of full options
      countryList: [],
      capitalList: [],
      needNext: false, // need to get next question or not
      mode: 0,
      question: {
        name: "",
        capital: "",
        iso_a2: ""
      },
      selectedIndex: undefined,
      randomIndexForOptions: 0
    };
  }

  getCountries(optionlist: any) {
    let res: any[] = [];
    optionlist.forEach((item: { name: string; capital: string }) => {
      res.push(item.name);
    });
    return res;
  }

  getCapitals(optionlist: any) {
    let res: any[] = [];
    optionlist.forEach((item: { name: string; capital: string }) => {
      res.push(item.capital);
    });
    console.log(res);
    return res;
  }

  getRandomIndex(countryList: string[]) {
    return Math.floor(Math.random() * countryList.length);
  }

  async componentDidMount() {
    this.setState({ mode: parseInt(this.props.match.params.id) });
    try {
      const id: string = await this.getGameID();
      console.log(id);
      this.setState({ gameID: id });

      const ops: [] = await this.getRandomCountryOptions();
      this.setState({ optionsList: ops });
      this.setState({ capitalList: this.getCapitals(ops) });
      this.setState({ countryList: this.getCountries(ops) });
      const question: option = this.state.optionsList[
        Math.floor(Math.random() * this.state.optionsList.length)
      ];
      this.setState({ question });
    } catch (e) {
      console.log(e);
    }
  }

  /*
    get game id for this game
  */
  async getGameID(): Promise<string> {
    const usersUniqueName = "not_a_user";
    let paramString = "?given=";
    if (parseInt(this.props.match.params.id) === 0)
      paramString += "Country&asked_for=Captial";
    else paramString += "Capital&asked_for=Country";
    const url = `${process.env.REACT_APP_API_URL}/api/country/new_game/${paramString}&users_unique_name=${usersUniqueName}`;
    const response = await axios.get(url);
    return response.data;
  }
  /*
    get random country options
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
      this.setState({ optionsList: ops });
      this.setState({
        capitalList: this.getCapitals(ops),
        countryList: this.getCountries(ops)
      });
      this.setState({
        randomIndexForOptions: this.getRandomIndex(this.state.countryList),
        selectedIndex: undefined
      });
      const question: option = this.state.optionsList[
        this.state.randomIndexForOptions
      ];
      this.setState({ question });
    } catch (e) {
      console.log(e);
    }
  };

  indexCallback = (selectedIndex: number | undefined) => {
    console.log("oh");
    this.setState({ selectedIndex: selectedIndex });
  };

  render() {
    if (this.state.gameID !== "") {
      return (
        <div>
            <SelectCapitalOrCountry
              gameID={this.state.gameID}
              questionCountry={this.state.question.name}
              questionCapital={this.state.question.capital}
              optionsList={this.state.optionsList}
              countryList={this.state.countryList}
              capitalList={this.state.capitalList}
              callback={this.nextQuestionPlsCallback}
              indexCallback={this.indexCallback}
              selectedIndex={this.state.selectedIndex}
              mode={this.state.mode}
            />
        </div>
      );
    } else {
      return null;
    }
  }
}
