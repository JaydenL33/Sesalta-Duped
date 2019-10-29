import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import AnswerComponent from './AnswerComponent';
import Map from './Map';

const useStyles = makeStyles({
  card: {
    minWidth: 275,
    marginTop: 30,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 24,
  },
  pos: {
    marginBottom: 12,
  },
});

export default function QuizElement() {
  const classes = useStyles();

  return (
    <Container maxWidth="sm">
        <Card className={classes.card} >
        <CardContent>
            <Typography className={classes.title} color="textSecondary" gutterBottom>
                What is the name of the highlighted country?
            </Typography>
            <div>
              <Map country="Australia"/>
            </div>
        </CardContent>
        <AnswerComponent/>
        <CardActions>
            <Button size="small">Next</Button>
        </CardActions>
        </Card>
    </Container>
  );
}
