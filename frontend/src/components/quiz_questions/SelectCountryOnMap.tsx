import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import Map from "../Map";

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
  }
};

interface IState {
  isCorrect?: boolean;
  countryObserved: string;
  isTried: boolean;
}

interface IProps {
  gameID?: string;
  countryExpected: string;
  classes: any;
  callback: any;
}

class SelectCountryOnMap extends React.Component<IProps, IState> {
  constructor(props: any) {
    super(props);
    this.state = {
      isCorrect: undefined,
      countryObserved: "",
      isTried: false
    };
  }

  async answerVerifier() {
    const url = `http://127.0.0.1:5000/api/country/check/?expected=${this.props.countryExpected}&observed=${this.state.countryObserved}&id=${this.props.gameID}`;
    const res: Promise<string> = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    })
      .then((response: any) => response.json())
      .then((response: any) => {
        console.log(response);
        this.setState({ isCorrect: response });
        return response;
      })
      .catch(e => {
        console.log(e);
      });
    console.log(res);
    console.log(this.props.countryExpected, this.state.countryObserved);
  }

  handleNextQuestion = () => {
    this.setState({ isTried: false, isCorrect: undefined });
    this.props.callback(); // trigger getting new quiz and render
  };

  handleMapClickCallback = (countryClicked: string) => {
    this.setState({ countryObserved: countryClicked, isTried: true }, () => {
      this.answerVerifier();
    });
  };

  render() {
    const { classes } = this.props;
    return (
      <Container maxWidth="sm">
        <Card className={classes.card}>
          <CardContent>
            <div>
              <Map callback={this.handleMapClickCallback} />
            </div>
            <Typography color="textSecondary" gutterBottom>
              Find {this.props.countryExpected}
            </Typography>
          </CardContent>
          <Typography>
            {this.state.isCorrect !== undefined &&
              (this.state.isCorrect ? "Correct" : "Wrong")}
          </Typography>
          <CardActions style={{ justifyContent: "center" }}>
            {this.state.isTried === true && (
              <Button
                className={classes.button}
                variant="contained"
                color="primary"
                size="medium"
                onClick={this.handleNextQuestion}
              >
                Next Question
              </Button>
            )}
          </CardActions>
        </Card>
      </Container>
    );
  }
}

export default withStyles(styles)(SelectCountryOnMap);
