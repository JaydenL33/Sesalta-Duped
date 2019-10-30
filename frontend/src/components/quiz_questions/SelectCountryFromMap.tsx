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
import { withTheme, Theme } from '@material-ui/core/styles';

const styles = (theme: Theme) => ({
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
  countryExpected: string,
  countryObserved: string,
  optionsList: string[],
  gameID?: string,
}

interface IProps {
  gameID: string,
  classes: any
}

class SelectCountryFromMap extends React.Component<IProps, IState> {
	constructor(props: any) {
		super(props);
		this.state = {
      isCorrect: undefined,
      countryExpected: '',
      optionsList: [],
      countryObserved: '',
      gameID: "",
		};
  };

  public getRandomCountryAndOptions() {
    // axios call
    return { countryExpected: 'New Zealand', optionsList: ['New Zealand', 'Australia', 'India', 'Vietnam']};
  }

  public answerVerifier() {
    console.log(this.state.countryExpected, this.state.countryObserved)
  }

  async componentDidMount() {
    this.setState({
      gameID : this.props.gameID,
    })
  }

  componentWillMount() {
    let countryAndOptions = this.getRandomCountryAndOptions();
    this.setState({ countryExpected: countryAndOptions.countryExpected, optionsList: countryAndOptions.optionsList });
  }

  answerComponentCallback = (countryObserved: string) => {
    this.setState({countryObserved: countryObserved})
  }


	render() {
    const { classes } = this.props;

		return (
      <Container maxWidth="sm">
        <Card className={classes.card}>
        <CardContent>
          {/* Debugging purposes {this.state.countryExpected} {this.state.countryObserved} */}
            <div>
              <Map country={this.state.countryExpected}/>
            </div>
            <Typography className={classes.title} gutterBottom>
                 What is the name of the highlighted country?
            </Typography>
        </CardContent>
        <AnswerComponent optionsList={this.state.optionsList} callback={this.answerComponentCallback}/>
        <CardActions style={{justifyContent: 'center'}}>
            <Button className={classes.button} variant="contained" color="primary" onClick={this.answerVerifier.bind(this)} size="medium">Next</Button>
        </CardActions>
        </Card>
    </Container>
		);
	}
}

export default withStyles(styles)(withTheme(SelectCountryFromMap));