import React from 'react';
import { withStyles, Theme } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import LanguageIcon from '@material-ui/icons/Language';
import { Link as RouterLink } from 'react-router-dom'
import Link from '@material-ui/core/Link';

const styles = (theme: Theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
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
    this.state = {isEnglish: true};
  }

  render() {
    const { classes } = this.props;
    const isEnglish = this.state.isEnglish;
    let LangButton;
    let HomeLink;

    if(isEnglish) {
      LangButton = <button onClick={() => this.setState({ isEnglish: false })}>ENG</button>;
      HomeLink = <Link color="inherit" component={RouterLink} to="/en/game">Sesalta</Link>;
    } else {
      LangButton = <button onClick={() => this.setState({ isEnglish: true })}>日本語</button>;
      HomeLink = <Link color="inherit" component={RouterLink} to="/jp/game">セサルタ</Link>;
    }

    return (
      <div className={classes.root}>
        <AppBar position="static">
          <Toolbar>
            {LangButton}
            <Typography variant="h6" className={classes.title} >
              {HomeLink}
            </Typography>
            <Button color="inherit">Login</Button>
          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

export default withStyles(styles, { withTheme: true })(NavBar);
