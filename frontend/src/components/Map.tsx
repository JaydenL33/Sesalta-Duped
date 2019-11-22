import React, { Component } from "react";
import IconButton from '@material-ui/core/IconButton';
import AddIcon from '@material-ui/icons/Add';
import RemoveIcon from '@material-ui/icons/Remove';
import {
  ComposableMap,
  ZoomableGroup,
  Geographies,
  Geography
} from "react-simple-maps";
import Grid from '@material-ui/core/Grid';


const wrapperStyles = {
  // width: "100%",
  // maxWidth: 980,
  margin: "0 auto"
};

interface MapProp {
  country?: string;
  callback?: any;
  initialScale: number;
}

interface IState {
  highlighted: string;
  hovered: boolean;
  selected: string;
  zoom: number;
  prevCountry: string | undefined;
}

class Map extends Component<MapProp, IState> {
  constructor(props: MapProp) {
    super(props);
    this.state = {
      highlighted: "",
      hovered: false,
      selected: "",
      zoom: props.initialScale,
      prevCountry: "",
    };
  }
  // static getDerivedStateFromProps(nextProps: MapProp, state: IState) {
  //   if (state.prevCountry !== undefined && state.prevCountry !== nextProps.country ) {
  //     console.log("changed")
  //     console.log(nextProps.country)
  //     console.log(state.prevCountry)
  //     return {
  //       zoom: 1
  //     };
  //   }
  //   return null;
  // }
  zoomIn = () => {
    if (this.state.zoom >= 5) return
    this.setState({
      zoom: this.state.zoom * 2,
    })
  }
  zoomOut = () => {
    this.setState({
      zoom: this.state.zoom / 2,
    })
  }
  handleMove = (geo: any) => {
    if (this.state.hovered) return;
    this.setState({
      hovered: true,
      highlighted: geo.properties.NAME
    });
  };
  handleLeave = (geo: any) => {
    this.setState({
      highlighted: "",
      hovered: false
    });
  };
  handleOnClick = (geo: any) => {
    // my way of separating the two game modes
    if (!this.props.country) this.props.callback(geo.properties.NAME_LONG);
    this.setState({
      selected: geo.properties.NAME
      // highlighted: geo.properties.NAME
    });
  };
  valuetext = (value: number) => {
    return `${value}`;
  }
  render() {
    return (
      <div style={wrapperStyles}>
        <Grid container spacing={2} style={{ justifyContent: "center" }}>
          <Grid item>
            <IconButton color="secondary" size="small" onClick={this.zoomOut}>
              <RemoveIcon />
            </IconButton>
          </Grid>
          <Grid item>
            <IconButton color="secondary" size="small" onClick={this.zoomIn}>
              <AddIcon />
            </IconButton>
          </Grid>
        </Grid>
        <ComposableMap
          projectionConfig={{
            scale: 205,
            rotation: [-10,0,0]
          }}
          width={980}
          height={620}
          style={{
            width: "100%",
            height: "auto"
          }}
        >
          <ZoomableGroup zoom={this.state.zoom} center={[10, 10]}>
            <Geographies
              geography="https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json"
              disableOptimization
            >
              {(geographies, projection) =>
                geographies.map((geography: any, i) => (
                  <Geography
                    key={i}
                    cacheId={geography.properties.ISO_A3 + i}
                    geography={geography}
                    projection={projection}
                    // onMouseMove={this.handleMove}
                    // onMouseLeave={this.handleLeave}
                    onClick={this.handleOnClick}
                    style={{
                      default: {
                        fill:
                          geography.properties.NAME_LONG ===
                          `${this.props.country}`
                            ? "#D02020"
                            : "#F0EAD6",
                        stroke:
                          geography.properties.NAME_LONG === `${this.props.country}`
                            ? "#D02020"
                            : "#B2A27D",
                        strokeWidth:
                            geography.properties.NAME_LONG === `${this.props.country}`
                              ? 4
                              : 0.5,
                        outline: "none",
                        transition: "all 250ms"
                      },
                      hover: {
                        fill: "#FF6F61",
                        stroke: "#9E1030",
                        strokeWidth: 1,
                        outline: "none",
                        transition: "all 250ms"
                      },
                      pressed: {
                        fill: "#DD4132",
                        stroke: "#9E1030",
                        strokeWidth: 1,
                        outline: "none",
                        transition: "all 250ms"
                      }
                    }}
                  />
                ))
              }
            </Geographies>
          </ZoomableGroup>
        </ComposableMap>
      </div>
    );
  }
}

export default Map;
