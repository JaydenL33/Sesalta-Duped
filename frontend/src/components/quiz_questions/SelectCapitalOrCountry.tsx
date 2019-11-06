import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import AnswerComponent from "./AnswerComponent";

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
}

interface Option {
  name: string;
  capital: string;
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
      showButton: false
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

    console.log("these are the game results", gameResults);
    const currentQuestion = gameResults.length;
    if (
      gameResults[currentQuestion - 1].observed_answers.length > 1 ||
      correctBoolean === 1
    ) {
      console.log("setting show button");
      this.setState({ showButton: true });
    }
  }

  convertCapitalToCountry(capital: string) {
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
          </CardActions>
        </Card>
      </Container>
    );
  }
}

export default withStyles(styles)(SelectCapitalOrCountry);
