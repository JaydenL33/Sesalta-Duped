import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import {
  Container,
  Box,
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell
} from "@material-ui/core";
import mainLogo from "../assets/sesaltaLogo.png";
import Typography from "@material-ui/core/Typography";
import { any } from "prop-types";

const styles = {
  root: {},
  img: {
    padding: 10,
    flex: 1,
    width: 225,
    height: 200,
    resizeMode: "contain"
  }
};

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
      const gameResults = this.props.location.state;
      let scoreSum = 0;
      for (const questionData of gameResults) {
        console.log(questionData.points);
        scoreSum += questionData.points;
      }
      this.setState({
        gameData: this.props.location.state,
        finalScore: scoreSum
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    const { classes } = this.props;
    return (
      <Container maxWidth="md" className={classes.root}>
        <Box component="span" m={1}>
          <img src={mainLogo} className={classes.img} alt="Logo" />
        </Box>
        <Typography variant="h4" color="textSecondary">
          You scored {this.state.finalScore} points!
        </Typography>
        <div>
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
                      <TableCell align="right">{questionData.points}</TableCell>
                    </TableRow>
                  );
                }
              )}
            </TableBody>
          </Table>
        </div>
      </Container>
    );
  }
}

export default withStyles(styles)(ResultsPage);
