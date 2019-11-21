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
import { Furigana } from "furigana-react";
import axios from "axios";
import LinearDeterminate from "../LinearDeterminate";

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
  progBar: number;
  pointsScored: number;
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
      gameResults: [],
      progBar: 0,
      pointsScored: 0
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
    const url = `${process.env.REACT_APP_API_URL}/api/country/check/?expected=${this.props.questionCountry}&observed=${answerObserved}&id=${this.props.gameID}`;
    const res = await axios.get(url);
    let response = res.data;
    console.log("this is the response", response);
    this.setState({ isCorrect: response });
    return response;
  }

  async attemptChecker(correctBoolean: number) {
    const url = `${process.env.REACT_APP_API_URL}/api/country/results/?id=${this.props.gameID}`;
    const gameResultsResponse = await axios.get(url);
    let gameResults = gameResultsResponse.data;
    let gr: Array<QuestionData> = JSON.parse(JSON.stringify(gameResults));
    const currentQuestion = gr.length;
    let newGR: QuestionData = gr[currentQuestion - 1];
    for (let j = 0; j < newGR.observed_answers.length; j++) {
      if (
        this.props.mode === 0 &&
        this.props.countryList.includes(newGR.observed_answers[j])
      ) {
        newGR.observed_answers[j] = this.convertCountryToCapital(
          newGR.observed_answers[j]
        );
      }
    }
    if (
      this.props.mode === 1 &&
      this.props.capitalList.includes(newGR.expected_answer)
    ) {
      newGR.expected_answer = this.convertCapitalToCountry(
        newGR.expected_answer
      );
    }
    if (
      this.props.mode === 0 &&
      this.props.countryList.includes(newGR.expected_answer)
    ) {
      newGR.expected_answer = this.convertCountryToCapital(
        newGR.expected_answer
      );
    }
    let oldGR = [...this.state.gameResults];
    oldGR[currentQuestion - 1] = newGR;
    this.setState({ gameResults: oldGR });
    console.log("these are the game results", this.state.gameResults);
    if (
      gameResults[currentQuestion - 1].observed_answers.length > 1 ||
      correctBoolean === 1
    ) {
      if (currentQuestion === 3) this.setState({ showFinishButton: true, pointsScored: gameResults[currentQuestion - 1].points, progBar: 1 });
      else this.setState({ showButton: true, pointsScored: gameResults[currentQuestion - 1].points, progBar: 1 });
    }
  }

  convertCountryToCapital(country: string): string {
    let res = "not found";
    this.props.optionsList.forEach(item => {
      if (item.name === country) {
        res = item.capital;
      }
    });
    return res;
  }

  convertCapitalToCountry(capital: string): string {
    let res = "";
    this.props.optionsList.forEach(item => {
      if (item.capital === capital) {
        res = item.name;
      }
    });
    return res;
  }

  answerComponentCallback = async (
    answerObserved: string,
    selectedIndex: number | undefined
  ) => {
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
    this.setState({ showButton: false, isCorrect: undefined, progBar: 0 });
    this.props.callback(); // trigger getting new quiz and render
  };

  render() {
    const { classes } = this.props;
    let QuestionText, ResponseText, ButtonText, EndButton, ProgBar;

    if (window.location.pathname.substr(1, 2) === "jp") {
      if (this.props.mode === 0) {
        QuestionText = (
          <Typography className={classes.title} gutterBottom>
            {this.props.questionCountry}
            <Furigana furigana="しゅと:なん" opacity={1.0}>
              の首都が何だ?
            </Furigana>
          </Typography>
        );
        ResponseText = (
          <Typography>
            {this.state.isCorrect !== undefined &&
              (this.state.isCorrect ? "Correct" : "Wrong")}
          </Typography>
        );
      } else {
        QuestionText = (
          <Typography className={classes.title} gutterBottom>
            <Furigana furigana="いず:こく:しゅと" opacity={1.0}>
              何れ国の首都が
            </Furigana>
            {this.props.questionCapital}だ？
          </Typography>
        );
      }

      ResponseText = (
        <Typography>
          {this.state.isCorrect !== undefined &&
            (this.state.isCorrect ? "正解" : "不正解")}
        </Typography>
      );
      ButtonText = "次の質問";
      EndButton = (
        <Link
          to={{ pathname: "/jp/game/results", state: this.state.gameResults }}
        >
          <Button
            className={
              this.state.showFinishButton ? classes.button : classes.hidden
            }
            variant="contained"
            color="primary"
            size="medium"
          >
            おわり!
          </Button>
        </Link>
      );
    } else {
      QuestionText = (
        <Typography className={classes.title} gutterBottom>
          {this.getQuestion()}
        </Typography>
      );
      ResponseText = (
        <Typography>
          {this.state.isCorrect !== undefined &&
            (this.state.isCorrect ? "Correct" : "Wrong")}
        </Typography>
      );
      ButtonText = "next question";
      EndButton = (
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
      );
    }
    
    if(this.state.progBar === 0) {
      ProgBar = <LinearDeterminate/>
    } else {
      ProgBar = <div></div>
    }

    return (
      <Container maxWidth="sm">
        <Card className={classes.card}>
          <CardContent>{QuestionText}</CardContent>
          {ProgBar}
          <AnswerComponent
            optionsList={
              this.props.mode === 0
                ? this.props.capitalList
                : this.props.countryList
            }
            selectedIndex={this.props.selectedIndex}
            disabled={this.state.showButton}
            callback={this.answerComponentCallback}
          />
          {ResponseText}
          <Typography
            className={this.state.showButton || this.state.showFinishButton ? classes.button : classes.hidden}>You scored {this.state.pointsScored}!</Typography>
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
              {ButtonText}
            </Button>
            {EndButton}
          </CardActions>
        </Card>
      </Container>
    );
  }
}

export default withStyles(styles)(SelectCapitalOrCountry);
