import React from 'react';
import { createStyles, Theme, makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';

interface IState {}

interface IProps {
	optionsList: string[],
	callback: any
 }


export default class SimpleList extends React.Component<IProps, IState> {

	constructor(props: any) {
		super(props)
	};

	public setOption(option: string) {
		this.props.callback(option)
	}

	render() {
		return (
			<div>
				<List component="nav" aria-label="main mailbox folders">
					{this.props.optionsList.map((option, index) => {
						return <ListItem key={index} button onClick={() => this.setOption(option)}>
						   <ListItemText primary={option} />
					   </ListItem>;
                  	})}
				</List>
			</div>
		);
	}
}
