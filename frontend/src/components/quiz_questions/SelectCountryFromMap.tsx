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
  countryObserved: string,
}

interface IProps {
  gameID?: string,
  countryExpected: string,
  optionsList: string[],
  classes: any
}

class SelectCountryFromMap extends React.Component<IProps, IState> {
	constructor(props: any) {
		super(props);
		this.state = {
      isCorrect: undefined,
      countryObserved: "",
		};
  };

  answerVerifier() {
    console.log(this.props.countryExpected, this.state.countryObserved)
  }

  answerComponentCallback = (countryObserved: string) => {
    console.log("observed: ", countryObserved);
    this.setState({countryObserved: countryObserved})
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
        <AnswerComponent optionsList={this.props.optionsList} callback={this.answerComponentCallback}/>
        <CardActions style={{justifyContent: 'center'}}>
            <Button className={classes.button} variant="contained" color="primary" onClick={this.answerVerifier.bind(this)} size="medium">Next</Button>
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