import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import Map from "../Map";
import { Link } from "react-router-dom";
import { Furigana } from "furigana-react";
import axios from "axios";

const styles = {
  card: {
    minWidth: 275,
    marginTop: 30
  },
  bullet: {
    display: "inline-block",
    margin: "0 2px",
    transform: "scale(0.8)"
  },
  title: {
    fontSize: 24
  },
  pos: {
    marginBottom: 12
  },
  hidden: {
    display: "none"
  }
};

interface IState {
  isCorrect?: boolean;
  countryObserved: string;
  showButton: boolean;
  showFinishButton: boolean;
  gameResults: QuestionData[];
}

interface IProps {
  gameID: string;
  countryExpected: string;
  classes: any;
  callback: any;
}
interface QuestionData {
  expected_answer: string;
  observed_answers: string[];
  points: number;
  potentional: number;
  question_num: number;
}

class SelectCountryOnMap extends React.Component<IProps, IState> {
  constructor(props: any) {
    super(props);
    this.state = {
      isCorrect: undefined,
      countryObserved: "",
      showFinishButton: false,
      showButton: false,
      gameResults: []
    };
  }

  async answerVerifier() {
    const url = `${process.env.REACT_APP_API_URL}/api/country/check/?expected=${this.props.countryExpected}&observed=${this.state.countryObserved}&id=${this.props.gameID}`;
    const res = await axios.get(url);
    const response = res.data;
    this.setState({ isCorrect: response });
    return response;
  }

  async attemptChecker(correctBoolean: number) {
    const url = `${process.env.REACT_APP_API_URL}/api/country/results/?id=${this.props.gameID}`;
    const gameResultsResponse = await axios.get(url);
    let gameResults = gameResultsResponse.data;
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

  handleNextQuestion = () => {
    this.setState({ showButton: false, isCorrect: undefined });
    this.props.callback(); // trigger getting new quiz and render
  };

  handleMapClickCallback = (countryClicked: string) => {
    this.setState({ countryObserved: countryClicked }, async () => {
      const correctBoolean = await this.answerVerifier();
      this.attemptChecker(correctBoolean);
    });
  };

  render() {
    const { classes } = this.props;
    let QuestionText, ResponseText, QuizButton, EndButton;

    if (window.location.pathname.substr(1, 2) === "jp") {
      QuestionText = (
        <Typography color="textSecondary" gutterBottom>
          {this.props.countryExpected}
          <Furigana furigana="み" opacity={1.0}>
            {" "}
            を見つける
          </Furigana>
        </Typography>
      );
      ResponseText = (
        <Typography>
          {this.state.isCorrect !== undefined &&
            (this.state.isCorrect ? "正解" : "不正解")}
        </Typography>
      );
      QuizButton = (
        <Button
          // className={classes.button}
          className={this.state.showButton ? classes.button : classes.hidden}
          variant="contained"
          color="primary"
          size="medium"
          onClick={this.handleNextQuestion}
        >
          次の質問
        </Button>
      );
      EndButton = (
        <Link
          to={{
            pathname: "/jp/game/results/",
            state: {
              stateData: this.state.gameResults,
              gameID: this.props.gameID
            }
          }}
        >
          <Button
            className={
              this.state.showFinishButton ? classes.button : classes.hidden
            }
            variant="contained"
            color="primary"
            size="medium"
          >
            おわり！
          </Button>
        </Link>
      );
    } else {
      QuestionText = (
        <Typography color="textSecondary" gutterBottom>
          Find {this.props.countryExpected}
        </Typography>
      );
      ResponseText = (
        <Typography>
          {this.state.isCorrect !== undefined &&
            (this.state.isCorrect ? "Correct" : "Wrong")}
        </Typography>
      );
      QuizButton = (
        <Button
          // className={classes.button}
          className={this.state.showButton ? classes.button : classes.hidden}
          variant="contained"
          color="primary"
          size="medium"
          onClick={this.handleNextQuestion}
        >
          Next Question
        </Button>
      );
      EndButton = (
        <Link
          to={{
            pathname: "/en/game/results/",
            state: {
              stateData: this.state.gameResults,
              gameID: this.props.gameID
            }
          }}
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
      );
    }

    return (
      <Container maxWidth="sm">
        <Card className={classes.card}>
          <CardContent>
            <div>
              <Map callback={this.handleMapClickCallback} initialScale={1}/>
            </div>
            {QuestionText}
          </CardContent>
          {ResponseText}
          <CardActions style={{ justifyContent: "center" }}>
            {QuizButton}
            {EndButton}
          </CardActions>
        </Card>
      </Container>
    );
  }
}

export default withStyles(styles)(SelectCountryOnMap);
