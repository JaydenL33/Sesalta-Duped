import React from "react";
import { withStyles, Theme } from "@material-ui/core/styles";
import {
  Container,
  Box,
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
  Button,
  Paper
} from "@material-ui/core";
import mainLogo from "../assets/sesaltaLogo.png";
import Typography from "@material-ui/core/Typography";
import { Link as RouterLink } from "react-router-dom";
// import Link from "@material-ui/core/Link";
import { Link } from "react-router-dom";
import axios from "axios";
import CircularProgress from "@material-ui/core/CircularProgress";
import StarsIcon from '@material-ui/icons/Stars';

const styles = (theme: Theme) => ({
  root: {},
  img: {
    padding: 10,
    flex: 1,
    width: 225,
    height: 200,
    resizeMode: "contain"
  },
  paper: {
    marginTop: theme.spacing(3),
    width: "100%",
    overflow: "auto",
    marginBottom: theme.spacing(2)
  },
  button: {
    margin: 5
  },
  spinner: {
    display: "block",
    marginTop: theme.spacing(10)
  }
});

interface QuestionData {
  expected_answer: string;
  observed_answers: string[];
  points: number;
  potentional: number;
  question_num: number;
}

interface IState {
  gameData: QuestionData[];
  trophies: string[];
  finalScore: number;
  rivalData: string;
  isLoading: boolean;
}
interface IProps {
  classes: any;
  location: any;
}

class ResultsPage extends React.Component<IProps, IState> {
  constructor(props: any) {
    super(props);
    this.state = {
      gameData: [],
      finalScore: 0,
      rivalData: "",
      isLoading: true,
      trophies: [],
    };
  }
  async componentDidMount() {
    console.log("Mounting GRP");
    try {
      console.log(this.props.location.state);
      const gameResults = this.props.location.state.stateData;
      let scoreSum = 0;
      for (const questionData of gameResults) {
        console.log(questionData.points);
        scoreSum += questionData.points;
      }
      
      const rivalUrl = `${process.env.REACT_APP_API_URL}/api/rank_rival_and_distance_to_rival/?game_id=${this.props.location.state.gameID}&user_name=${this.props.location.state.publicName}`;
      const result = await axios.get(rivalUrl);
      console.log(result.data, "rival data");
      
      const gameID = this.props.location.state.gameID;
      const trophyUrl = `${process.env.REACT_APP_API_URL}/api/game/trophies/?user=${this.props.location.state.publicName}&game=${gameID}`;
      const res = await axios.get(trophyUrl);
      let response = res.data;
      console.log("this is the trophy response", response);
      
      for (const trophyData of response) {
        console.log(trophyData.name);
        this.setState({ trophies: [ ...this.state.trophies, trophyData.name] });
      }
      
      this.setState({
        gameData: this.props.location.state.stateData,
        finalScore: scoreSum,
        rivalData: result.data.rival_info,
        isLoading: false
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    const { classes } = this.props;
    let TrophyHeader;
    
    if(this.state.trophies.length > 0) {
      if(this.state.trophies.length === 1) {
        TrophyHeader = <Typography variant="h4" color="textSecondary">
            <StarsIcon /> You also obtained {this.state.trophies.length} trophy! 
            <StarsIcon />
          </Typography>;
      } else {
        TrophyHeader = <Typography variant="h4" color="textSecondary">
            <StarsIcon /> You also obtained {this.state.trophies.length} trophies! 
            <StarsIcon />
          </Typography>;
      }
    }
    
    return (
      <Container maxWidth="md" className={classes.root}>
        <Box component="span" m={1}>
          <img src={mainLogo} className={classes.img} alt="Logo" />
        </Box>
        {this.state.isLoading ? (
          <div className={classes.spinner}>
            <CircularProgress />
          </div>
        ) : (
          <div>
            <Typography variant="h4" color="textSecondary">
              You scored {this.state.finalScore} points!
            </Typography>
            <Typography variant="h5" color="textSecondary">
              {this.state.rivalData}
            </Typography>
            <Paper className={classes.paper}>
              <Table
                className={classes.table}
                size="small"
                aria-label="a dense table"
              >
                <TableHead>
                  <TableRow>
                    <TableCell align="left">Question Number</TableCell>
                    <TableCell align="left">Expected Answer</TableCell>
                    <TableCell align="left">Last Answer Given</TableCell>
                    <TableCell align="left">Attempts</TableCell>
                    <TableCell align="right">Points Received</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {this.state.gameData.map(
                    (questionData: QuestionData, index: number) => {
                      return (
                        <TableRow key={index}>
                          <TableCell align="left" component="th" scope="row">
                            {index + 1}
                          </TableCell>
                          <TableCell align="left">
                            {questionData.expected_answer}
                          </TableCell>
                          <TableCell align="left">
                            {
                              questionData.observed_answers[
                                questionData.observed_answers.length - 1
                              ]
                            }
                          </TableCell>
                          <TableCell align="left">
                            {questionData.observed_answers.length}
                          </TableCell>
                          <TableCell align="right">
                            {questionData.points}
                          </TableCell>
                        </TableRow>
                      );
                    }
                  )}
                </TableBody>
              </Table>
            </Paper>
            {TrophyHeader}
            <ul list-style-type="none">
              {this.state.trophies.map(name => <li>{name}</li>)}
            </ul>
            <div>
              <Link
                to={{
                  pathname: "/en/leaderboard"
                }}
              >
                <Button
                  variant="contained"
                  color="primary"
                  className={classes.button}
                >
                  Leaderboard
                </Button>
              </Link>
              <Link
                to={{
                  pathname: "/en/game/options",
                  state: {
                    publicName: this.props.location.state.publicName
                  }
                }}
              >
                <Button
                  variant="contained"
                  color="secondary"
                  className={classes.button}
                >
                  Play Again
                </Button>
              </Link>
            </div>
          </div>
        )}
      </Container>
    );
  }
}

export default withStyles(styles, { withTheme: true })(ResultsPage);
