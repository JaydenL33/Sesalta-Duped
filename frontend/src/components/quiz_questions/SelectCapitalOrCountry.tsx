import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import AnswerComponent from "./AnswerComponent";
import { Link } from "react-router-dom";

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
  answerObserved: string;
  answerExpected: string;
  bgColor: string;
  showButton: boolean;
  showFinishButton: boolean;
  gameResults: QuestionData[];
}

interface Option {
  name: string;
  capital: string;
  iso_a2: string;
}

interface QuestionData {
  expected_answer: string;
  observed_answers: string[];
  points: number;
  potentional: number;
  question_num: number;
}

interface IProps {
  gameID?: string;
  questionCountry: string;
  questionCapital: string;
  optionsList: Option[];
  countryList: string[];
  capitalList: string[];
  classes: any;
  callback: any;
  indexCallback: any;
  selectedIndex?: number | undefined;
  mode: number;
}

class SelectCapitalOrCountry extends React.Component<IProps, IState> {
  constructor(props: IProps) {
    super(props);
    this.state = {
      isCorrect: undefined,
      answerObserved: "",
      answerExpected: "",
      bgColor: "primary",
      showButton: false,
      showFinishButton: false,
      gameResults: []
    };
  }

  getQuestion() {
    if (this.props.mode === 0) {
      return `What is the capital city of ${this.props.questionCountry}?`;
    } else {
      return `Which country's capital city is ${this.props.questionCapital}?`;
    }
  }

  /*
    check with backend
  */
  async answerVerifier(answerObserved: string) {
    const url = `http://127.0.0.1:5000/api/country/check/?expected=${this.props.questionCountry}&observed=${answerObserved}&id=${this.props.gameID}`;
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
    let gr: Array<QuestionData> = JSON.parse(JSON.stringify(gameResults));
    const currentQuestion = gr.length;
    let newGR: QuestionData = gr[currentQuestion-1];
    for (let j = 0; j < newGR.observed_answers.length; j++) {
      if (this.props.mode === 0 && this.props.countryList.includes(newGR.observed_answers[j])) {
        newGR.observed_answers[j] = this.convertCountryToCapital(newGR.observed_answers[j]);
      }
    }
    if (this.props.mode === 1 && this.props.capitalList.includes(newGR.expected_answer)) {
      newGR.expected_answer = this.convertCapitalToCountry(newGR.expected_answer);
    }
    if (this.props.mode === 0 && this.props.countryList.includes(newGR.expected_answer)) {
      newGR.expected_answer = this.convertCountryToCapital(newGR.expected_answer);
    }
    let oldGR = [...this.state.gameResults];
    oldGR[currentQuestion - 1] = newGR;
    this.setState({ gameResults: oldGR });
    console.log("these are the game results", this.state.gameResults);
    if (
      gameResults[currentQuestion - 1].observed_answers.length > 1 ||
      correctBoolean === 1
    ) {
      if (currentQuestion === 3) this.setState({ showFinishButton: true });
      else this.setState({ showButton: true });
    }
  }

  convertCountryToCapital(country: string): string {
    let res = "not found";
    this.props.optionsList.forEach(item => {
      if (item.name === country) {
        res = item.capital;
      }
    })
    return res;
  }

  convertCapitalToCountry(capital: string): string {
    let res = "";
    this.props.optionsList.forEach(item => {
      if (item.capital === capital) {
        res = item.name;
      }
    })
    return res;
  }

  answerComponentCallback = async (answerObserved: string, selectedIndex: number | undefined) => {
    console.log("answered observed: ", answerObserved);
    this.props.indexCallback(selectedIndex);
    let ans = answerObserved;
    if (this.props.capitalList.includes(answerObserved)) {
      ans = this.convertCapitalToCountry(answerObserved);
    }
    const correctBoolean = await this.answerVerifier(ans);
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
            <Typography className={classes.title} gutterBottom>
              {this.getQuestion()}
            </Typography>
          </CardContent>
          <AnswerComponent
            optionsList={this.props.mode === 0 ? this.props.capitalList : this.props.countryList}
            selectedIndex={this.props.selectedIndex}
            disabled={this.state.showButton}
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
              next question
            </Button>
            <Link
              to={{ pathname: "/en/game/results", state: this.state.gameResults }}
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

export default withStyles(styles)(SelectCapitalOrCountry);
