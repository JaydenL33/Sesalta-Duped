import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import AnswerComponent from "./AnswerComponent";
import Map from "../Map";
import { useHistory } from "react-router-dom";
import { Link } from "react-router-dom";
// import { browserHistory } from "react-router";

const styles = {
  card: {
    minWidth: 275,
    marginTop: 50
  },
  title: {
    fontSize: 24,
    fontWeight: 500,
    fontFamily: "Helvetica Neue"
  },
  pos: {
    marginBottom: 12
  },
  button: {
    margin: 5
  },
  hidden: {
    display: "none"
  }
};

interface IState {
  isCorrect?: boolean;
  // isTried: boolean
  countryObserved: string;
  bgColor: string;
  showButton: boolean;
  showFinishButton: boolean;
  gameResults: QuestionData[];
}

interface IProps {
  gameID?: string;
  countryExpected: string;
  optionsList: string[];
  classes: any;
  callback: any;
  indexCallback: any;
  selectedIndex?: number | undefined;
}
interface QuestionData {
  expected_answer: string;
  observed_answers: string[];
  points: number;
  potentional: number;
  question_num: number;
}

class SelectCountryFromMap extends React.Component<IProps, IState> {
  constructor(props: any) {
    super(props);
    this.state = {
      isCorrect: undefined,
      countryObserved: "",
      bgColor: "primary",
      showButton: false,
      showFinishButton: false,
      gameResults: []
    };
  }

  /*
    check with backend
  */
  async answerVerifier(countryObserved: string) {
    console.log(this.props.countryExpected, countryObserved, this.props.gameID);
    const url = `http://127.0.0.1:5000/api/country/check/?expected=${this.props.countryExpected}&observed=${countryObserved}&id=${this.props.gameID}`;
    const res = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    });
    let response = await res.json();
    console.log("this is the response", response);
    this.setState({ isCorrect: response });
    return response;
  }

  async attemptChecker(correctBoolean: number) {
    const gameResultsResponse = await fetch(
      `http://127.0.0.1:5000/api/country/results/?id=${this.props.gameID}`,
      {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      }
    );
    let gameResults = await gameResultsResponse.json();
    this.setState({ gameResults: JSON.parse(JSON.stringify(gameResults)) });
    console.log("these are the game results", gameResults);
    const currentQuestion = gameResults.length;
    if (
      gameResults[currentQuestion - 1].observed_answers.length > 1 ||
      correctBoolean === 1
    ) {
      console.log("setting show button");
      if (currentQuestion === 3) this.setState({ showFinishButton: true });
      else this.setState({ showButton: true });
    }
  }

  answerComponentCallback = async (
    countryObserved: string,
    selectedIndex: number | undefined
  ) => {
    console.log("observed: ", countryObserved);
    this.props.indexCallback(selectedIndex);
    this.setState({ countryObserved: countryObserved });
    const correctBoolean = await this.answerVerifier(countryObserved);
    this.attemptChecker(correctBoolean);
  };

  handleButtonClick = (e: React.SyntheticEvent) => {
    this.setState({ showButton: false, isCorrect: undefined });
    this.props.callback(); // trigger getting new quiz and render
  };
  render() {
    const { classes } = this.props;
    return (
      <Container maxWidth="sm">
        <Card className={classes.card}>
          <CardContent>
            <div>
              <Map country={this.props.countryExpected} />
            </div>
            <Typography className={classes.title} gutterBottom>
              What is the name of the highlighted country?
            </Typography>
          </CardContent>
          <AnswerComponent
            selectedIndex={this.props.selectedIndex}
            disabled={this.state.showButton}
            optionsList={this.props.optionsList}
            callback={this.answerComponentCallback}
          />
          <Typography>
            {this.state.isCorrect !== undefined &&
              (this.state.isCorrect ? "Correct" : "Wrong")}
          </Typography>
          <CardActions style={{ justifyContent: "center" }}>
            <Button
              className={
                this.state.showButton ? classes.button : classes.hidden
              }
              variant="contained"
              color="secondary"
              size="medium"
              onClick={this.handleButtonClick}
            >
              Next Question
            </Button>
            <Link
              to={{ pathname: "/game/results", state: this.state.gameResults }}
            >
              <Button
                className={
                  this.state.showFinishButton ? classes.button : classes.hidden
                }
                variant="contained"
                color="primary"
                size="medium"
              >
                Finish!
              </Button>
            </Link>
          </CardActions>
        </Card>
      </Container>
    );
  }
}

export default withStyles(styles)(SelectCountryFromMap);
