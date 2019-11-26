
import React, { useEffect } from "react";
import { Theme, createStyles, makeStyles } from "@material-ui/core/styles";
import Chip from '@material-ui/core/Chip';
import FaceIcon from '@material-ui/icons/Face';
import DoneIcon from '@material-ui/icons/Done';
import axios from "axios";


interface Iprops {
  name: string;  
}

interface State {
  data: any;
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      width: "100%",
      margin: theme.spacing(1),
      // overflowX: 'auto',
      flexGrow: 1,
      display: 'flex',
      justifyContent: 'left',
    },
  })
);

/**
 * return a list of trophyies of a user
 */
export default function Trophy(props: Iprops) {
  const classes = useStyles();
  // const generateTrophies = async () => {
  //   await axios
  //   .get(`${process.env.REACT_APP_API_URL}/api/user/trophies?user=${props.name}`)
  //   .then(function(response) {
  //     console.log(response);
  //     return response.data;
  //   })
  // }
  const [state, setState] = React.useState<State>({
    data: []
  });
  useEffect(() => {
    console.log(props.name);
    axios
    .get(`${process.env.REACT_APP_API_URL}/api/user/trophies/?user=${props.name}`)
    .then(function(response) {
      console.log(response);
      let data = response.data;
      setState({
        data
      });
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className={classes.root}>
      {
        state.data && state.data.forEach((info: { date: string; name: string }) => {
          return <Chip
            icon={<FaceIcon />}
            label={info.name}
            clickable
            color="primary"
            deleteIcon={<DoneIcon />}
            variant="outlined"
          />
        })
      }
    </div>
  )
}