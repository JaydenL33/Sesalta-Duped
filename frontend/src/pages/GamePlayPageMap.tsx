import React from "react";
import SelectCountryOnMap from "../components/quiz_questions/SelectCountryOnMap";
import axios from "axios";

interface P {
  location: any;
}

interface S {
  gameID: string;
  needNext: boolean;
  countryExpected: string;
}

export default class GamePlayPage extends React.Component<P, S> {
  constructor(props: P) {
    super(props);
    this.state = {
      gameID: "",
      countryExpected: "",
      needNext: false // need to get next question or not
    };
  }

  getCountries(optionlist: any) {
    let res: any[] = [];
    optionlist.forEach((item: { name: any }) => {
      res.push(item.name);
    });
    return res;
  }

  async componentDidMount() {
    try {
      const id: string = await this.getGameID();
      console.log(id);
      this.setState({ gameID: id });

      const ops: any = await this.getRandomCountryOptions();
      const country: string = ops[0].name;
      this.setState({ countryExpected: country });
    } catch (e) {
      console.log(e);
    }
  }

  /*
    get game id for this game
  */
  async getGameID(): Promise<string> {
    const usersUniqueName = this.props.location.state.publicName;
    const url = `${process.env.REACT_APP_API_URL}/api/country/new_game/?given=Country&asked_for=Map&users_unique_name=${usersUniqueName}`;
    const response = await axios.get(url);
    return response.data;
  }
  /*
    get random options
  */
  async getRandomCountryOptions() {
    const url = `${process.env.REACT_APP_API_URL}/api/country/random/?amount=1&id=${this.state.gameID}`;
    const response = await axios.get(url);
    return response.data;
  }

  nextQuestionPlsCallback = async () => {
    // this.setState({ needNext: next })
    try {
      const ops: any = await this.getRandomCountryOptions();
      const country: string = ops[0].name;
      this.setState({ countryExpected: country });
      // console.log(countrylist)
    } catch (e) {
      console.log(e);
    }
  };

  render() {
    if (this.state.gameID !== "") {
      return (
        <div>
          <SelectCountryOnMap
            gameID={this.state.gameID}
            countryExpected={this.state.countryExpected}
            callback={this.nextQuestionPlsCallback}
            publicName={this.props.location.state.publicName}
          />
        </div>
      );
    } else {
      return null;
    }
  }
}
