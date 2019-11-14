import React, { useEffect } from 'react';
import MaterialTable, { Column } from 'material-table';
import Container from '@material-ui/core/Container';
import { Theme, createStyles, makeStyles } from '@material-ui/core/styles';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import axios from 'axios';
import CircularProgress from '@material-ui/core/CircularProgress';

interface Row {
  name: string;
  date: string;
  score: number;
  mode: number;
}

interface TableState {
  columns: Array<Column<Row>>;
  data: Row[];
  title: string;
  name: string // player's name
  isauthenticated: boolean;
  isLoading: boolean;
}

interface Props {
  name: string; // player's name
  isauthenticated: boolean;
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      width: '100%',
      marginTop: theme.spacing(5),
      // overflowX: 'auto',
    },
    tabs: {
      flexGrow: 1,
    },
    spinner: {
      display: 'block',
      marginTop: theme.spacing(10),
    },
  }),
);

// component from: https://material-table.com/#/docs/all-props
export default function MaterialTableDemo(props: Props) {
  const classes = useStyles();
  const [value, setValue] = React.useState(1);
  // handle tab change
  const handleChange = async (event: React.ChangeEvent<{}>, newValue: number) => {
    console.log(value);
    setValue(newValue);
    await addNewDataToState(newValue);
  };
  const [state, setState] = React.useState<TableState>({
    columns: [
      { title: 'Name', field: 'name' },
      { title: 'Date', field: 'date' },
      { title: 'Score', field: 'score', defaultSort: "desc"},
      {
        title: 'Mode',
        field: 'mode',
        lookup: { 0: 'Country -> Map', 1: 'Map -> Country', 2: 'Capital -> Country', 3: 'Country -> Capital', 4: 'Flag -> Country'},
      },
    ],
    data: [ // this is the data we need to put into table
      // { name: 'Mehmet', date: '2019-11-14', score: 999, mode: 0 },
      // { name: 'Frozen yoghurt', date: '2019-11-14', score: 900, mode: 1 },
      // { name: 'Eclair', date: '2019-11-14', score: 900, mode: 1 },
      // { name: 'Cupcake', date: '2019-11-14', score: 850, mode: 4 },
      // { name: 'Ice cream sandwichcake', date: '2019-11-14', score: 850, mode: 4 },
      // { name: 'Ice cream sandwich', date: '2019-11-10', score: 600, mode: 3 },
      // { name: 'Gingerbread', date: '2019-11-13', score: 850, mode: 2 },
      // { name: 'Gingerbread', date: '2019-11-13', score: 850, mode: 2 },
    ],
    title: "",
    name: "prasadsuniquename", // should be sth like props.name
    isauthenticated: true, // should be sth like props.isauthenticated
    isLoading: true,
  });

  const addNewDataToState = async (newValue: number) => {
    setState({
      ...state,
      isLoading: true
    });
    // if (newValue === 0 && props.name) {
    if (newValue === 0) {
      setState({
        ...state,
        data: await getPlayerData(state.name),
        isLoading: false
      });
      console.log(state)
    } else if (newValue === 1) {
      setState({
        ...state,
        data: await getGlobalData(),
        isLoading: false
      });
    }
  }

  // passing an empty array as second argument triggers the callback in useEffect only after the initial render
  // thus replicating `componentDidMount` lifecycle behaviour
  useEffect(() => {
    addNewDataToState(1);
    console.log('mount it!');
  }, []);
  
  // Make a request for a player's record with a given publicName
  const getPlayerData:any = async (name: string) => 
  await axios.get(`http://127.0.0.1:5000/api/getPlayersScoreboard?name=${name}`)
  .then(function (response) {
    console.log(response.data);
    // modify to array structure
    let data: Row[] = [];
    Object.values(response.data).map((item: any)=> {
      let row: Row = {
        name: name,
        date: "2019-11-14", // should be item.Date
        score: item.Score,
        mode: 0
      }
      data.push(row);
    })
    console.log(data)
    return data;
  })
  .catch(function (error) {
    console.log(error);
  });

  // Make a request to get all game records
  const getGlobalData:any = async () => 
  await axios.get(`http://127.0.0.1:5000/api/getGlobalLeaderboard`)
  .then(function (response) {
    console.log(response.data);
    // modify to array structure
    let data: Row[] = [];
    Object.entries(response.data).map((user: any)=> {
      let name = user[0];
      console.log(user[1])
      Object.values(user[1]).map((item: any)=> {
        let row: Row = {
          name: name,
          date: "2019-11-14", // should be item.Date
          score: item.Score,
          mode: 0
        }
        data.push(row);
      });
    });
    console.log(data)
    return data;
  })
  .catch(function (error) {
    console.log(error);
  });

  return (
    <Container maxWidth="lg" className={classes.root}>
      <Tabs
        value={value}
        onChange={handleChange}
        indicatorColor="primary"
        textColor="primary"
        centered
      >
        <Tab label="My Score" disabled={!state.isauthenticated}/>
        <Tab label="leaderboard" />
      </Tabs>
      { state.isLoading ? 
        <div className={classes.spinner}>
          <CircularProgress />
        </div>
      : <MaterialTable
          title={state.title}
          columns={state.columns}
          data={state.data}
          options={{
            search: true,
            filtering: true,
            pageSize: 10
          }}
        />
      }
    </Container>
  );
}
