import React, { useContext } from 'react';
import { withStyles, Theme } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { Link as RouterLink } from 'react-router-dom';
import Link from '@material-ui/core/Link';
import Popover from '@material-ui/core/Popover';

import FormatListNumberedIcon from '@material-ui/icons/FormatListNumbered';
import IconButton from '@material-ui/core/IconButton';
import firebase from 'firebase';
import useAuth from '../utils/AuthContext';
import LoginButton from './LoginButton';

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
  classes: any;
}

interface S {
  isEnglish: boolean;
  anchorEl: HTMLButtonElement | null;
}

class NavBar extends React.Component<P, S> {
  constructor(props: P) {
    super(props);
    if (window.location.pathname.substr(1, 2) === 'en') {
      this.state = {
        isEnglish: true,
        anchorEl: null,
      };
    } else if (window.location.pathname.substr(1, 2) === 'jp') {
      this.state = {
        isEnglish: false,
        anchorEl: null,
      };
    } else {
      this.state = {
        isEnglish: true,
        anchorEl: null,
      };
    }
  }

  handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    this.setState({ anchorEl: event.currentTarget });
  };

  handleClose = () => this.setState({ anchorEl: null });

  render() {
    const { classes } = this.props;
    const { isEnglish, anchorEl } = this.state;
    const open = Boolean(anchorEl);
    const id = open ? 'simple-popover' : undefined;
    let LangButton;
    let HomeLink;

    if (isEnglish) {
      LangButton = (
        <Button
          color="inherit"
          onClick={() => this.setState({ isEnglish: false })}
        >
          <Link color="inherit" component={RouterLink} to="/jp/game">
            ENG
          </Link>
        </Button>
      );
      HomeLink = (
        <Link color="inherit" component={RouterLink} to="/en/game">
          Sesalta
        </Link>
      );
    } else {
      LangButton = (
        <Button
          color="inherit"
          onClick={() => this.setState({ isEnglish: true })}
        >
          <Link color="inherit" component={RouterLink} to="/en/game">
            日本語
          </Link>
        </Button>
      );
      HomeLink = (
        <Link color="inherit" component={RouterLink} to="/jp/game">
          セサルタ
        </Link>
      );
    }

    return (
      <div className={classes.root}>
        <AppBar position="static">
          <Toolbar>
            {LangButton}
            <IconButton color="inherit">
              <Link color="inherit" component={RouterLink} to="/en/leaderboard">
                <FormatListNumberedIcon />
              </Link>
            </IconButton>
            <Typography variant="h6" className={classes.title}>
              {HomeLink}
            </Typography>
            <LoginButton />
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

export default withStyles(styles, { withTheme: true })(NavBar);
