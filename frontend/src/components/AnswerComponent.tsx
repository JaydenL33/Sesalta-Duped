import React from 'react';
import { createStyles, Theme, makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
// import ListItemIcon from '@material-ui/core/ListItemIcon';
// import Divider from '@material-ui/core/Divider';
// import InboxIcon from '@material-ui/icons/Inbox';
// import DraftsIcon from '@material-ui/icons/Drafts';



// function ListItemLink(props: ListItemProps<'a', { button?: true }>) {
//   return <ListItem button component="a" {...props} />;
// }



interface IState {
	isCorrect?: boolean
}

interface IProps { }


export default class SimpleList extends React.Component<IProps, IState> {

	constructor(props: any) {
		super(props)
		this.state = {
			isCorrect: undefined,
		};

	};

	render() {
		console.log(this.state);
		return (
			<div>
				<List component="nav" aria-label="main mailbox folders">
					<ListItem button onClick={() => this.setState({ isCorrect: false })}>
						<ListItemText primary="New Zealand" />
					</ListItem>
					<ListItem button onClick={() => this.setState({ isCorrect: true })}>
						<ListItemText primary="Australia" />
					</ListItem>
					<ListItem button onClick={() => this.setState({ isCorrect: false })}>
						<ListItemText primary="Austria" />
					</ListItem>
					<ListItem button onClick={() => this.setState({ isCorrect: false })}>
						<ListItemText primary="China" />
					</ListItem>
				</List>
				<List component="nav" aria-label="secondary mailbox folders">
					{this.state.isCorrect !== undefined &&
						(this.state.isCorrect ? (<p>Correct!</p>) : (<p>Incorrect!</p>))}
				</List>
			</div>
		);
	}
}
