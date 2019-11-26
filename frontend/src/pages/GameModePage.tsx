import React, { useEffect } from "react";
import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";
import { Container, Box, Chip } from "@material-ui/core";
import mainLogo from "../assets/sesaltaLogo.png";
import Typography from "@material-ui/core/Typography";
import { useHistory } from "react-router-dom";
import useAuth from "../utils/AuthContext";
import axios from "axios";
import LoginForm from "../components/LoginForm";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";

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
        "-apple-system",
        "BlinkMacSystemFont",
        '"Segoe UI"',
        "Roboto",
        '"Helvetica Neue"',
        "Arial",
        "sans-serif",
        '"Apple Color Emoji"',
        '"Segoe UI Emoji"',
        '"Segoe UI Symbol"'
      ].join(",")
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
      [theme.breakpoints.down("sm")]: {
        display: "block"
      }
    },
    chip: {
      padding: 50,
      margin: 5,
      maxWidth: 220,
      [theme.breakpoints.down("sm")]: {
        maxWidth: 200
      }
    }
  })
);

interface IProps {
  classes: any;
}
interface IState {
  dialog: boolean;
  publicName: string;
  userEmail: string;
}

export default function GameHome(props: IProps) {
  const classes = useStyles(props);
  const history = useHistory();
  const { user }: any = useAuth();
  const [value, setValue] = React.useState(1);

  const [state, setState] = React.useState<IState>({
    dialog: false,
    publicName: "",
    userEmail: ""
  });

  const checkUserToOpenDialog = async (user: any) => {
    let result = false;
    let publicName = state.publicName;
    // localStorage.setItem('localStoragePublicName', state.publicName);
    let email = state.userEmail;
    if (user) {
      console.log(user.uid);
      email = user.email;
      const url = `${process.env.REACT_APP_API_URL}/api/user/get_id/?email=${user.email}`;
      const response = await axios.get(url);
      if (response.data === "None") result = true;
      else {
        result = false;
        publicName = response.data;
        // localStorage.setItem('localStoragePublicName', publicName);
        email = user.email;
      }
    } else {
      publicName = "not_a_user";
      // localStorage.setItem('localStoragePublicName', publicName);
    }
    console.log(result, "the res", publicName);
    setState({
      dialog: result,
      publicName: publicName,
      userEmail: email
    });
    localStorage.setItem('localStoragePublicName', publicName);
  };

  useEffect(() => {
    console.log("does this run in redirect");
    checkUserToOpenDialog(user);
    // console.log(dialogResult, "wfsdfsfs");
  }, []);

  const [open, setOpen] = React.useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = async (e: any) => {
    // console.log(e.target.value);
    // console.log(user);
    console.log(state.publicName, state.userEmail);
    let response = await axios.get(
      `${process.env.REACT_APP_API_URL}/api/user/update_name/?name=${state.publicName}&email=${state.userEmail}`
    );
    console.log(response.data);
    if (response.data == "0") {
      return;
    }
    setState({
      dialog: false,
      publicName: state.publicName,
      userEmail: state.userEmail
    });
    localStorage.setItem('localStoragePublicName', state.publicName);
  };

  const onChange = (e: any) => {
    // console.log(e.target.value);
    setState({
      dialog: state.dialog,
      publicName: e.target.value,
      userEmail: state.userEmail
    });
    localStorage.setItem('localStoragePublicName', state.publicName);
  };

  return (
    <Container maxWidth="md" className={classes.root}>
      <div>
        <Dialog
          open={state.dialog}
          onClose={handleClose}
          aria-labelledby="form-dialog-title"
        >
          <DialogTitle id="form-dialog-title">
            Just a bit more information before you can start playing!
          </DialogTitle>
          <DialogContent>
            <TextField
              autoFocus
              margin="dense"
              id="name"
              label="3 Character Public Name"
              // type="email"
              fullWidth
              onChange={e => onChange(e)}
              inputProps={{ maxLength: 3 }}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={e => handleClose(e)} color="primary">
              Lets Go!
            </Button>
          </DialogActions>
        </Dialog>
      </div>

      <Box component="span" m={1}>
        <img src={mainLogo} className={classes.img} alt="Logo" />
      </Box>
      <Typography className={classes.title} variant="h2" color="textSecondary">
        Welcome To Sesalta!
      </Typography>
      <div className={classes.horizontalItems}>
        <Chip
          clickable
          onClick={() =>
            {
              history.push({
                pathname: "/en/game/options",
                state: { 
                  publicName: state.publicName,
                }
              })
              localStorage.setItem('localStoragePublicName', state.publicName);
            }
          }
          color="secondary"
          className={classes.chip}
          label="Play"
        />
      </div>
    </Container>
  );
}
