import React from 'react';
import MaterialTable, { Column } from 'material-table';
import Container from '@material-ui/core/Container';
import { Theme, createStyles, makeStyles } from '@material-ui/core/styles';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import axios from 'axios';

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
  name: string | undefined; // player's name
  isauthenticated: boolean;
}

interface Props {
  name: string | undefined; // player's name
  isauthenticated: boolean;
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      width: '100%',
      marginTop: theme.spacing(5),
      overflowX: 'auto',
    },
    tabs: {
      flexGrow: 1,
    },
  }),
);

// component from: https://material-table.com/#/docs/all-props
export default function MaterialTableDemo(props: Props) {
  const classes = useStyles();
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
      { name: 'Mehmet', date: '2019-11-14', score: 999, mode: 0 },
      { name: 'Frozen yoghurt', date: '2019-11-14', score: 900, mode: 1 },
      { name: 'Eclair', date: '2019-11-14', score: 900, mode: 1 },
      { name: 'Cupcake', date: '2019-11-14', score: 850, mode: 4 },
      { name: 'Ice cream sandwichcake', date: '2019-11-14', score: 850, mode: 4 },
      { name: 'Ice cream sandwich', date: '2019-11-10', score: 600, mode: 3 },
      { name: 'Gingerbread', date: '2019-11-13', score: 850, mode: 2 },
      { name: 'Gingerbread', date: '2019-11-13', score: 850, mode: 2 },
    ],
    title: "Global Ranking",
    name: props.name,
    isauthenticated: true, // should be props.isauthenticated
  });

  const [value, setValue] = React.useState(1);
  const handleChange = (event: React.ChangeEvent<{}>, newValue: number) => {
    setValue(newValue);
    if (value === 0 && props.name) {
    // setState({
    //   ...state,
    //   data: getPlayerData(state.name)
    // });
    } else {
    // setState({
    //   ...state,
    //   data: getGlobalData()
    // });
    }
  };

  // Make a request for a player's record with a given publicName
  const getPlayerData = async (publicName: string) => 
  await axios.get(`http://127.0.0.1:5000/api/score?publicName=${publicName}`)
  .then(function (response) {
    console.log(response);
    return response.data;
  })
  .catch(function (error) {
    console.log(error);
  });

  // TODO
  // Make a request to get all game records
  // const getGlobalData = async () => ...

  return (
    <Container maxWidth="lg" className={classes.root}>
      <Tabs
        value={value}
        onChange={handleChange}
        indicatorColor="primary"
        textColor="primary"
        centered
      >
        <Tab label="Player Ranking" disabled={!state.isauthenticated}/>
        <Tab label="Global Ranking" />
      </Tabs>
      <MaterialTable
        title={state.title}
        columns={state.columns}
        data={state.data}
        options={{
          search: true,
          filtering: true,
          pageSize: 10
        }}
      />
    </Container>
  );
}
