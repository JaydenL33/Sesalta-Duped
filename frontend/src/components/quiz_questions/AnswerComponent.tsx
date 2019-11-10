import React from "react";
import List from "@material-ui/core/List";
import { ListItem, ListItemText } from "@material-ui/core";

interface IState {
  // selectedIndex: any,
}

interface IProps {
  optionsList: string[];
  callback: any;
  disabled: boolean;
  selectedIndex?: number | undefined;
}

export default class SimpleList extends React.Component<IProps, IState> {
  constructor(props: any) {
    super(props);
    // this.state = {
    // 	selectedIndex: undefined,
    // };
  }

  render() {
    return (
      <div>
        <List component="nav" aria-label="main mailbox folders">
          {this.props.optionsList.map((option, index) => {
            return (
              <ListItem
                key={index}
                selected={this.props.selectedIndex === index}
                button
                onClick={() => this.handleListItemClick(option, index)}
                disabled={this.props.disabled}
              >
                <ListItemText primary={option} />
              </ListItem>
            );
          })}
        </List>
      </div>
    );
  }

  public handleListItemClick = (option: string, index: number) => {
    this.props.callback(option, index);
    // this.setState({selectedIndex: index});
  };
}
