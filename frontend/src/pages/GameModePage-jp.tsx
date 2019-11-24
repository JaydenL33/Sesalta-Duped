import React from "react";
import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";
import { Container, Box, Chip } from "@material-ui/core";
import jpLogo from "../assets/sesaltaLogo-jp.png";
import Typography from "@material-ui/core/Typography";
import { useHistory } from "react-router-dom";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {},
    card: {
      marginTop: theme.spacing(5),
      marginBottom: theme.spacing(4),
      maxHeight: 400
    },
    title: {
      fontFamily: [
        '-apple-system',
        'BlinkMacSystemFont',
        '"Segoe UI"',
        'Roboto',
        '"Helvetica Neue"',
        'Arial',
        'sans-serif',
        '"Apple Color Emoji"',
        '"Segoe UI Emoji"',
        '"Segoe UI Symbol"',
      ].join(','),
    },
    list: {
      width: "100%",
      display: "block",
      backgroundColor: theme.palette.background.paper
    },
    button: {
      display: "block",
      maxWidth: 50,
      marginBottom: theme.spacing(),
      marginLeft: theme.spacing()
    },
    img: {
      padding: 10,
      flex: 1,
      width: 225,
      height: 200,
      resizeMode: "contain"
    },
    horizontalItems: {
      paddingTop: 50,
      padding: 20,
      flex: 1,
      display: "flex",
      // alignItems: 'center',
      justifyContent: "center",
      [theme.breakpoints.down('sm')]: {
        display: "block",
      },
    },
    chip: {
      padding: 50,
      margin: 5,
      maxWidth: 220,
      [theme.breakpoints.down('sm')]: {
        maxWidth: 200,
      },
    }
  })
);

interface Props {
  classes: any;
}

export default function GameHome(props: Props) {
  const classes = useStyles(props);
  const history = useHistory();

  return (
    <Container maxWidth="md" className={classes.root}>
      <Box component="span" m={1}>
        <img src={jpLogo} className={classes.img} alt="Logo" />
      </Box>
      <Typography variant="h2" color="textSecondary">
        ようこそセサルタへ!
      </Typography>
      <div className={classes.horizontalItems}>
        <Chip
          clickable
          onClick={() => history.push("/jp/game/options")}
          color="secondary"
          className={classes.chip}
          label="シングルプレイ"
        />
      </div>
    </Container>
  );
}
