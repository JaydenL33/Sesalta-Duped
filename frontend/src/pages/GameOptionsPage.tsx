import React from "react";
import withStyles from "@material-ui/core/styles/withStyles";
import { createStyles, Theme } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemSecondaryAction from "@material-ui/core/ListItemSecondaryAction";
import ListItemText from "@material-ui/core/ListItemText";
import Checkbox from "@material-ui/core/Checkbox";
import { Link } from "react-router-dom";

const style = (theme: Theme) =>
  createStyles({
    root: {
      display: "flex",
      alignItems: "center",
      alignContent: "center"
    },
    card: {
      marginTop: 40,
      marginBottom: 4,
      maxHeight: 500,
      width: 500,
      [theme.breakpoints.down("lg")]: {
        maxWidth: 400
      }
    },
    title: {
      fontSize: 25
    },
    list: {
      width: "100%",
      display: "block",
      backgroundColor: "white"
    },
    button: {
      display: "block",
      maxWidth: 50,
      marginBottom: 1,
      marginLeft: 1
    }
  });

interface Props {
  classes: any;
  location: any;
}

interface States {
  checked: boolean[];
  selected: number;
}

class OptionsPage extends React.Component<Props, States> {
  constructor(props: Props) {
    super(props);
    this.state = {
      checked: [true, false, false, false, false],
      selected: 0
    };
  }

  handleToggle = (value: number) => () => {
    let newChecked = [false, false, false, false, false];
    newChecked[value] = this.state.checked[value] === false;
    console.log(newChecked);
    console.log(this.state.selected);
    this.setState({
      selected: value,
      checked: newChecked
    });
  };

  render() {
    const { classes } = this.props;
    const URLs: string[] = [
      "/en/game/play",
      "/en/game/play/map",
      "/en/game/play/capital/0", // choose capital from country
      "/en/game/play/capital/1", // choose country from capital
      "/en/game/play/flag"
    ];
    return (
      <Container style={{ justifyContent: "center" }} className={classes.root}>
        <Card className={classes.card}>
          <CardContent>
            <Typography
              className={classes.title}
              color="textSecondary"
              gutterBottom
            >
              Choose Game Mode
            </Typography>
            <List className={classes.list}>
              <ListItem key={0} button>
                <ListItemText primary={"Guess The Country Name"} />
                <ListItemSecondaryAction>
                  <Checkbox
                    edge="end"
                    onChange={this.handleToggle(0)}
                    checked={this.state.checked[0]}
                  />
                </ListItemSecondaryAction>
              </ListItem>
              <ListItem key={1} button>
                <ListItemText primary={"Find The Country On The Map"} />
                <ListItemSecondaryAction>
                  <Checkbox
                    edge="end"
                    onChange={this.handleToggle(1)}
                    checked={this.state.checked[1]}
                  />
                </ListItemSecondaryAction>
              </ListItem>
              <ListItem key={2} button>
                <ListItemText primary={"Guess The Capital City"} />
                <ListItemSecondaryAction>
                  <Checkbox
                    edge="end"
                    onChange={this.handleToggle(2)}
                    checked={this.state.checked[2]}
                  />
                </ListItemSecondaryAction>
              </ListItem>
              <ListItem key={3} button>
                <ListItemText primary={"Guess The Country From Capital City"} />
                <ListItemSecondaryAction>
                  <Checkbox
                    edge="end"
                    onChange={this.handleToggle(3)}
                    checked={this.state.checked[3]}
                  />
                </ListItemSecondaryAction>
              </ListItem>
              <ListItem key={4} button>
                <ListItemText primary={"Guess The National Flag"} />
                <ListItemSecondaryAction>
                  <Checkbox
                    edge="end"
                    onChange={this.handleToggle(4)}
                    checked={this.state.checked[4]}
                  />
                </ListItemSecondaryAction>
              </ListItem>
            </List>
          </CardContent>
          <CardActions style={{ justifyContent: "center" }}>
            <Link
              to={{
                pathname: URLs[this.state.selected],
                state: {
                  publicName: this.props.location.state.publicName
                }
              }}
            >
              <Button
                className={classes.button}
                color="secondary"
                size="medium"
              >
                Start
              </Button>
            </Link>
          </CardActions>
        </Card>
      </Container>
    );
  }
}

export default withStyles(style)(OptionsPage);
