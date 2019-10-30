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
    marginTop: 30,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 24,
  },
  pos: {
    marginBottom: 12,
  },
});

interface IState {
  isCorrect?: boolean,
  countryExpected: string,
  countryObserved: string,
  optionsList: string[],
}

interface IProps { }

class SelectCountryFromMap extends React.Component<IProps, IState> {

  public getRandomCountryAndOptions() {
    // axios call
    return { countryExpected: 'New Zealand', optionsList: ['New Zealand', 'Australia', 'India', 'Vietnam']};
  }

  public answerVerifier() {
    console.log(this.state.countryExpected, this.state.countryObserved)
  }
  componentWillMount() {
    let countryAndOptions = this.getRandomCountryAndOptions();
    this.setState({ countryExpected: countryAndOptions.countryExpected, optionsList: countryAndOptions.optionsList });
  }

  answerComponentCallback = (countryObserved: string) => {
    this.setState({countryObserved: countryObserved})
  }

	constructor(props: any) {
		super(props)
		this.state = {
            isCorrect: undefined,
            countryExpected: '',
            optionsList: [],
            countryObserved: '',
		};
  };

	render() {
		return (
      <Container maxWidth="sm">
        <Card >
        <CardContent>
          Debugging purposes {this.state.countryExpected} {this.state.countryObserved}
            <div>
              <Map country={this.state.countryExpected}/>
            </div>
            <Typography color="textSecondary" gutterBottom>
                 What is the name of the highlighted country?
            </Typography>
        </CardContent>
        <AnswerComponent optionsList={this.state.optionsList} callback={this.answerComponentCallback}/>
        <CardActions>
            <Button onClick={this.answerVerifier.bind(this)} size="small">Next</Button>
        </CardActions>
        </Card>
    </Container>
		);
	}
}

export default withStyles(styles)(SelectCountryFromMap);