import React from 'react';
import withStyles from '@material-ui/core/styles/withStyles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
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
  countrySelected: string,
  countryToFind: string
}

interface IProps { }

class SelectCountryOnMap extends React.Component<IProps, IState> {

  public getRandomCountry() {
    // axios call
    return 'New Zealand';
  }

  public sendDataToBackend() {
    console.log(this.state.countryToFind, this.state.countrySelected)
  }
  componentWillMount() {
    let country = this.getRandomCountry();
    this.setState({ countryToFind: country });
  }

	constructor(props: any) {
		super(props)
		this.state = {
      isCorrect: undefined,
      countryToFind: '',
      countrySelected: '',
		};
  };
  
  mapCallback = (countryClicked: string) => {
    this.setState({ countrySelected: countryClicked })
  }

	render() {
		return (
      <Container maxWidth="sm">
        <Card >
        <CardContent>
          Debugging purposes {this.state.countrySelected} {this.state.countryToFind}
            <div>
              <Map callback={this.mapCallback}/>
            </div>
            <Typography color="textSecondary" gutterBottom>
                Find {this.state.countryToFind} 
            </Typography>
        </CardContent>
        <CardActions>
            <Button onClick={this.sendDataToBackend.bind(this)} size="small">Next</Button>
        </CardActions>
        </Card>
    </Container>
		);
	}
}

export default withStyles(styles)(SelectCountryOnMap)