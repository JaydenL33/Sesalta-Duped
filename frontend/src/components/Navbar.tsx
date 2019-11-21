import React from 'react';
import { withStyles, Theme } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { Link as RouterLink } from 'react-router-dom'
import Link from '@material-ui/core/Link';
import FormatListNumberedIcon from '@material-ui/icons/FormatListNumbered';
import IconButton from '@material-ui/core/IconButton';

const styles = (theme: Theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
    justifyContent: "center"
  },
});

interface P {
  classes: any
}

interface S {
  isEnglish: boolean;
}

class NavBar extends React.Component<P,S> {
  constructor(props: P) {
    super(props);
    if(window.location.pathname.substr(1, 2) === "en") {
      this.state = {isEnglish: true};
    } else if(window.location.pathname.substr(1, 2) === "jp") {
      this.state = {isEnglish: false};
    } else {
      this.state = {isEnglish: true};
    }
  }

  render() {
    const { classes } = this.props;
    const isEnglish = this.state.isEnglish;
    let LangButton;
    let HomeLink;
    let LoginButton;

    if(isEnglish) {
      LangButton = <Button color="inherit" onClick={() => this.setState({ isEnglish: false })}>
        <Link color="inherit" component={RouterLink} to="/jp/game">ENG</Link>
      </Button>;
      HomeLink = <Link color="inherit" component={RouterLink} to="/en/game">Sesalta</Link>;
      LoginButton = <Button color="inherit">Login</Button>;
    } else {
      LangButton = <Button color="inherit" onClick={() => this.setState({ isEnglish: true })}>
        <Link color="inherit" component={RouterLink} to="/en/game">日本語</Link>
      </Button>;
      HomeLink = <Link color="inherit" component={RouterLink} to="/jp/game">セサルタ</Link>;
      LoginButton = <Button color="inherit">ログイン</Button>;
    }

    return (
      <div className={classes.root}>
        <AppBar position="static">
          <Toolbar>
            {LangButton}
            <IconButton color="inherit">
              <Link color="inherit" component={RouterLink} to="/en/leaderboard"><FormatListNumberedIcon/></Link>
            </IconButton>
            <Typography variant="h6" className={classes.title} >
              {HomeLink}
            </Typography>
            {LoginButton}
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

export default withStyles(styles, { withTheme: true })(NavBar);
