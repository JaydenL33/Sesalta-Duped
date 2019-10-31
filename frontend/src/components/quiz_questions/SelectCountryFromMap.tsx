import React from 'react';
import withStyles from '@material-ui/core/styles/withStyles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import AnswerComponent from './AnswerComponent';
import Map from '../Map';

const styles = ({
  card: {
    minWidth: 275,
    marginTop: 50,
  },
  title: {
    fontSize: 24,
    fontWeight: 500,
    fontFamily: 'Helvetica Neue',
  },
  pos: {
    marginBottom: 12,
  },
  button: {
    marginBottom: 5
  }
});

interface IState {
  isCorrect?: boolean,
  isTried: boolean
  countryObserved: string,
  bgColor: string
}

interface IProps {
  gameID?: string,
  countryExpected: string,
  optionsList: string[],
  classes: any,
  callback: any
}

class SelectCountryFromMap extends React.Component<IProps, IState> {
	constructor(props: any) {
		super(props);
		this.state = {
      isCorrect: undefined,
      isTried: false,
      countryObserved: "",
      bgColor: "primary"
		};
  };

  /*
    check with backend
  */
  async answerVerifier() {
    const url = `http://127.0.0.1:5000/api/country/check/?expected=${this.props.countryExpected}&observed=${this.state.countryObserved}&id=${this.props.gameID}`
    const res: Promise<string> = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response: any) => response.json())
    .then((response: any) => {
      console.log(response);
      this.setState({isCorrect: response})
      return response;
    })
    .catch((e) => {
      console.log(e);
    });
    console.log(res);
    console.log(this.props.countryExpected, this.state.countryObserved)
  }

  answerComponentCallback = (countryObserved: string) => {
    console.log("observed: ", countryObserved);
    this.setState({countryObserved: countryObserved})
  }
  
  handleButtonClick = (e: React.SyntheticEvent) => {
    if (this.state.isTried) {
      this.setState({ isTried: false, isCorrect: undefined });
      this.props.callback(); // trigger getting new quiz and render
    } else {
      this.setState({ isTried: true });
      this.answerVerifier(); 
    }
  }

  render() {
    const { classes } = this.props;
    // if (this.props.gameID && this.state.optionsList.length !== 0) {
    return (
      <Container maxWidth="sm">
        <Card className={classes.card}>
        <CardContent>
          {/* Debugging purposes {this.state.countryExpected} {this.state.countryObserved} */}
            <div>
              <Map country={this.props.countryExpected}/>
            </div>
            <Typography className={classes.title} gutterBottom>
                What is the name of the highlighted country?
            </Typography>
        </CardContent>
        <AnswerComponent disabled={this.state.isTried} optionsList={this.props.optionsList} callback={this.answerComponentCallback}/>
        <Typography>{this.state.isCorrect !== undefined && (this.state.isCorrect ?  "Correct": "Wrong")}</Typography>
        <CardActions style={{justifyContent: 'center'}}>
            <Button className={classes.button} 
              variant="contained"
              color={this.state.isTried? "primary": "secondary"}
              size="medium"
              onClick={this.handleButtonClick}
            >
              {this.state.isTried? "next question": "Check" }
            </Button>
        </CardActions>
        </Card>
      </Container>
    );
    // } else {
    //   return null
    // }
	}
}

export default withStyles(styles)(SelectCountryFromMap);