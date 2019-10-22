import React, { Component } from "react";
import {
  ComposableMap,
  ZoomableGroup,
  Geographies,
  Geography
} from "react-simple-maps";

const wrapperStyles = {
  width: "100%",
  maxWidth: 980,
  margin: "0 auto"
};

interface MapProp {
  country: string;
}

class Map extends Component<MapProp> {
  state = {
    highlighted: "",
    hovered: false
  };
  handleMove = (geo: any) => {
    if (this.state.hovered) return;
    this.setState({
      hovered: true,
      highlighted: geo.properties.NAME
    });
  };
  handleLeave = () => {
    this.setState({
      highlighted: "",
      hovered: false
    });
  };
  render() {
    return (
      <div style={wrapperStyles}>
        <ComposableMap
          projectionConfig={{
            scale: 205,
            rotation: [-11, 0, 0]
          }}
          width={980}
          height={551}
          style={{
            width: "100%",
            height: "auto"
          }}
        >
          <ZoomableGroup center={[10, 20]} disablePanning>
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
                    onMouseMove={this.handleMove}
                    onMouseLeave={this.handleLeave}
                    style={{
                      default: {
                        fill:
                          geography.properties.NAME === `${this.props.country}`
                            ? "#DD4132"
                            : "#F0EAD6",
                        stroke:
                          geography.properties.NAME ===
                          this.state.highlighted
                            ? "#9E1030"
                            : "#B2A27D",
                        strokeWidth: 0.75,
                        outline: "none",
                        transition: "all 250ms"
                      },
                      hover: {
                        fill: "#FF6F61",
                        stroke: "#9E1030",
                        strokeWidth: 0.75,
                        outline: "none",
                        transition: "all 250ms"
                      },
                      pressed: {
                        fill: "#DD4132",
                        stroke: "#9E1030",
                        strokeWidth: 0.75,
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
