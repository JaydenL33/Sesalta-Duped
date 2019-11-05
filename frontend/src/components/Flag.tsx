import React, { Component } from 'react';

const wrapperStyles = {
  width: '100%',
  height: 'auto',
  display: 'block',
  minHeight: 200,
  maxWidth: '100%',
  margin: '0 auto',
};

interface Country {
  name: string;
  iso_a2: string;
}

interface FlagProp {
  country?: Country;
  callback?: any;
}

class Flag extends Component<FlagProp> {
  state = {
    hovered: false,
  };

  handleMove = (geo: any) => {
    if (this.state.hovered) return;
    this.setState({
      hovered: true,
    });
  };

  handleLeave = (country: any) => {
    this.setState({
      hovered: false,
    });
  };

  handleOnClick = () => {
    // my way of separating the two game modes
    if (this.props.callback && this.props.country)
      this.props.callback(this.props.country.name);
  };

  render() {
    return (
      <>
        {this.props.country ? (
          <div style={wrapperStyles} onClick={this.handleOnClick}>
            <img
              style={{ border: '1px solid black' }}
              src={`https://lipis.github.io/flag-icon-css/flags/4x3/${this.props.country.iso_a2.toLowerCase()}.svg`}
            />
          </div>
        ) : (
          <div style={wrapperStyles}/>
        )}
      </>
    );
  }
}

export default Flag;
