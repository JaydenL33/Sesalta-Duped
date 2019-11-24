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
import { Furigana } from "furigana-react";
import mainLogo from "../assets/sesaltaLogo-jp.png";
import Typography from "@material-ui/core/Typography";
import { Link as RouterLink } from 'react-router-dom'
import Link from '@material-ui/core/Link';

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
    width: '100%',
    overflow: 'auto',
    marginBottom: theme.spacing(2),
  },
  button: {
    margin: 5,
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
  finalScore: number;
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
      finalScore: 0
    };
  }
  async componentDidMount() {
    console.log("Mounting GRP");
    try {
      const gameResults = this.props.location.state.stateData;
      let scoreSum = 0;
      for (const questionData of gameResults) {
        console.log(questionData.points);
        scoreSum += questionData.points;
      }
      this.setState({
        gameData: this.props.location.state.stateData,
        finalScore: scoreSum
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    const { classes } = this.props;
    let PointText, TableHeaders;
    
    if(window.location.pathname.substr(1,2) === "jp") {
      PointText = <Typography variant="h4" color="textSecondary">
            あなたは
            {this.state.finalScore}
            <Furigana furigana="とくてん" opacity={1.0}>得点しました！</Furigana>
        </Typography>;
      TableHeaders = <TableRow>
                <TableCell align="left">
                  <Furigana furigana="しつもん" opacity={1.0}>
                    質問
                  </Furigana></TableCell>
                <TableCell align="left">
                  <Furigana furigana="しょき:こた" opacity={1.0}>
                    所期の答え
                  </Furigana></TableCell>
                <TableCell align="left">
                  <Furigana furigana="こた:さ:あ" opacity={1.0}>
                    答えを差し上げた
                  </Furigana></TableCell>
                <TableCell align="left">
                  <Furigana furigana="こころ:すう" opacity={1.0}>
                    試み数
                  </Furigana></TableCell>
                <TableCell align="right">
                  <Furigana furigana="とくてん" opacity={1.0}>
                    得点
                  </Furigana></TableCell>
              </TableRow>
    } else {
      PointText = <Typography variant="h4" color="textSecondary">
          You scored {this.state.finalScore} points!
        </Typography>
      TableHeaders = <TableRow>
                <TableCell align="left">Question Number</TableCell>
                <TableCell align="left">Expected Answer</TableCell>
                <TableCell align="left">Last Answer Given</TableCell>
                <TableCell align="left">Attempts</TableCell>
                <TableCell align="right">Points Received</TableCell>
              </TableRow>
    }
    
    return (
      <Container maxWidth="md" className={classes.root}>
        <Box component="span" m={1}>
          <img src={mainLogo} className={classes.img} alt="Logo" />
        </Box>
        {PointText}
        <Paper className={classes.paper}>
          <Table
            className={classes.table}
            size="small"
            aria-label="a dense table"
          >
            <TableHead>
              {TableHeaders}
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
                      <TableCell align="right">{questionData.points}</TableCell>
                    </TableRow>
                  );
                }
              )}
            </TableBody>
          </Table>
        </Paper>
        <div>
          <Button variant="contained" color="primary" className={classes.button}>
            <Link color="inherit" component={RouterLink} to="/jp/leaderboard">リーダーボード</Link>
          </Button>
          <Button variant="contained" color="secondary" className={classes.button}>
            <Link color="inherit" component={RouterLink} to="/jp/game/options">再びプレー</Link>
          </Button>
        </div>
      </Container>
    );
  }
}

export default withStyles(styles)(ResultsPage);
