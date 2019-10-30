import React from 'react';
import List from '@material-ui/core/List';
import { ListItem, ListItemText, ListItemSecondaryAction, Checkbox } from '@material-ui/core';

interface IState {
	selectedIndex: any,
}

interface IProps {
	optionsList: string[],
	callback: any
 }


export default class SimpleList extends React.Component<IProps, IState> {
	constructor(props: any) {
		super(props);
		this.state = {
			selectedIndex: undefined,
		};
  	};

	render() {
		return (
			<div>
				<List component="nav" aria-label="main mailbox folders">
					{this.props.optionsList.map((option, index) => {
						return <ListItem key={index} selected={this.state.selectedIndex == index} button onClick={() => this.handleListItemClick(index,option)}>
						   <ListItemText primary={option} />
					   </ListItem>;
                  	})}
				</List>
			</div>
		);
	}

	public handleListItemClick = (index: number, option: string) => {
		this.props.callback(option);
		this.setState({selectedIndex: index});
	};
}
