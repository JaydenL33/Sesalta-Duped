import React from 'react';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import ListItemText from '@material-ui/core/ListItemText';
import Checkbox from '@material-ui/core/Checkbox';
import { Link as RouterLink} from 'react-router-dom'

const useStyles = makeStyles((theme: Theme) => 
  createStyles({
    root: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      alignContent: 'center'
    },
    card: {
      marginTop: theme.spacing(5),
      marginBottom: theme.spacing(4),
      maxHeight: 500,
      minWidth: 300,
    },
    title: {
      fontSize: 25,
    },
    list: {
      width: '100%',
      display: 'block',
      backgroundColor: theme.palette.background.paper,
    },
    button: {
      display: 'block',
      maxWidth: 50,
      marginBottom: theme.spacing(),
      marginLeft: theme.spacing(),
    },
  }),
);

interface Props {
  classes: any
}

export default function QuizElement(props: Props) {
  const classes = useStyles(props);
  const [checked, setChecked] = React.useState([1]);

  const handleToggle = (value: number) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];
    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }
    setChecked(newChecked);
  };

  return (
    <Container className={classes.root} >
      <Card className={classes.card} >
        <CardContent>
          <Typography className={classes.title} color="textSecondary" gutterBottom>
            Choose given information & solution
          </Typography>
          <List className={classes.list}>
            <ListItem key={0} button>
              <ListItemText primary={'country name'} />
              <ListItemSecondaryAction>
                <Checkbox
                  edge="end"
                  onChange={handleToggle(0)}
                  checked={checked.indexOf(0) !== -1}
                />
              </ListItemSecondaryAction>
            </ListItem>
            <ListItem key={1} button>
              <ListItemText primary={'world map'} />
              <ListItemSecondaryAction>
                <Checkbox
                  edge="end"
                  onChange={handleToggle(1)}
                  checked={checked.indexOf(1) !== -1}
                />
              </ListItemSecondaryAction>
            </ListItem>
            <ListItem key={2} button>
              <ListItemText primary={'caputal city'} />
              <ListItemSecondaryAction>
                <Checkbox
                  edge="end"
                  onChange={handleToggle(2)}
                  checked={checked.indexOf(2) !== -1}
                />
              </ListItemSecondaryAction>
            </ListItem>
            <ListItem key={3} button>
              <ListItemText primary={'national flag'} />
              <ListItemSecondaryAction>
                <Checkbox
                  edge="end"
                  onChange={handleToggle(3)}
                  checked={checked.indexOf(3) !== -1}
                />
              </ListItemSecondaryAction>
            </ListItem>
          </List>
          </CardContent>
        <CardActions style={{justifyContent: 'center'}}>
          <Button 
            component={RouterLink}
            to="/game/play"
            size="medium"
            className={classes.button}
            color="secondary"
          >
            Start
          </Button>
        </CardActions>
      </Card>
    </Container>
  );
}
