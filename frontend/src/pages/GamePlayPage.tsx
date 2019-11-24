import React from "react";
import SelectCountryFromMap from "../components/quiz_questions/SelectCountryFromMap";
import axios from "axios";

interface P {
  location: any;
}

interface S {
  gameID: string;
  optionsList: string[];
  needNext: boolean;
  selectedIndex: number | undefined;
  randomIndexForOptions: number;
  // attemptCount: number,
}

export default class GamePlayPage extends React.Component<P, S> {
  constructor(props: P) {
    super(props);
    this.state = {
      gameID: "",
      optionsList: [],
      needNext: false, // need to get next question or not
      selectedIndex: undefined,
      randomIndexForOptions: 0
      // attemptCount: 0,
    };
  }

  getCountries(optionlist: any) {
    let res: any[] = [];
    optionlist.forEach((item: { name: any }) => {
      res.push(item.name);
    });
    return res;
  }

  getRandomIndex(countryList: string[]) {
    return Math.floor(Math.random() * countryList.length);
  }

  async componentDidMount() {
    try {
      const id: string = await this.getGameID();
      console.log(id);
      this.setState({ gameID: id });

      const ops: [] = await this.getRandomCountryOptions();
      const countrylist: string[] = this.getCountries(ops);
      console.log(countrylist);
      this.setState({
        optionsList: countrylist,
        randomIndexForOptions: this.getRandomIndex(countrylist)
      });
    } catch (e) {
      console.log(e);
    }
  }

  /*
    get game id for this game
  */
  async getGameID(): Promise<string> {
    const usersUniqueName = this.props.location.state.publicName;
    const url = `${process.env.REACT_APP_API_URL}/api/country/new_game/?given=Map&asked_for=Country&users_unique_name=${usersUniqueName}`;
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
      const countrylist: string[] = this.getCountries(ops);
      console.log(countrylist);
      this.setState({
        optionsList: countrylist,
        randomIndexForOptions: this.getRandomIndex(countrylist),
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

  render() {
    if (this.state.gameID !== "") {
      return (
        <div>
          <SelectCountryFromMap
            selectedIndex={this.state.selectedIndex}
            // attemptCount={this.state.attemptCount}
            gameID={this.state.gameID}
            countryExpected={
              this.state.optionsList[this.state.randomIndexForOptions]
            }
            optionsList={this.state.optionsList}
            callback={this.nextQuestionPlsCallback}
            indexCallback={this.indexCallback}
            publicName={this.props.location.state.publicName}
          />
        </div>
      );
    } else {
      return null;
    }
  }
}
