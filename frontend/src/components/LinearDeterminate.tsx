import React from 'react';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import LinearProgress from '@material-ui/core/LinearProgress';

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      width: '100%',
    },
  }),
);

interface IProps {
  questionAnswered: boolean;
}

export default function LinearDeterminate() {
  const classes = useStyles();
  const [completed, setCompleted] = React.useState(100);

  React.useEffect(() => {
    function progress() {
      setCompleted(oldCompleted => {
        if (oldCompleted === 0) {
          // Action to open 'next question' button
        }
        const diff = 8.4;
        return Math.max(oldCompleted - diff, 0);
      });
    }

    const timer = setInterval(progress, 1000);
    return () => {
      clearInterval(timer);
    };
  }, []);

  return (
    <div className={classes.root}>
      <LinearProgress variant="determinate" value={completed} color="secondary" />
    </div>
  );
}
