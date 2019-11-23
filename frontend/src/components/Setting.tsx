import React from 'react';
// import FormLabel from '@material-ui/core/FormLabel';
import FormControl from '@material-ui/core/FormControl';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Switch from '@material-ui/core/Switch';
import TextField from '@material-ui/core/TextField';
import { Theme, createStyles, makeStyles } from "@material-ui/core/styles";
// import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      margin: theme.spacing(1),
      // overflowX: 'auto',
      display: 'flex',
      // flexWrap: 'wrap',
      // width: 300,
    },
    container: {
    },
  })
);

interface Iprops {
  callback?: any;     // may not need
  shared: boolean  // need this coz toggle needs an initial value
}

export default function Setting(props: Iprops) {
  const [state, setState] = React.useState({
    share: props.shared,
    name: "",
  });

  const classes = useStyles();

  const handleToggleChange = (name: string) => (event: React.ChangeEvent<HTMLInputElement>) => {
    setState({ ...state, [name]: event.target.checked });
    console.log("send request here or use callback")
  };
  const handleChange = (name: string) => (event: React.ChangeEvent<HTMLInputElement>) => {
    setState({ ...state, [name]: event.target.value });
  };
  const handleSubmit = () => (event: React.KeyboardEvent<HTMLInputElement>) => {
    console.log(`Pressed keyCode ${event.key}`);
    if (event.key === 'Enter') {
      console.log("send request here or use callback")
      // props.callback(state.name); // ask parent to make requests
    }
  }

  return (
    <FormControl className={classes.root} component="fieldset">
      <FormGroup>
        <FormControlLabel
          control={<Switch checked={state.share} onChange={handleToggleChange('share')} value="gilad" />}
          label="Share my scores to global score board?"
        />
        <FormControlLabel
          control={
            <TextField variant="outlined" onKeyPress={handleSubmit()} onChange={handleChange('name')} placeholder="Enter new name" />
          }
          label=""
        />
      </FormGroup>
    </FormControl>
  );
}