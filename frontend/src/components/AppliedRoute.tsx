import React from "react";
import { Route } from "react-router-dom";


interface RouteProps {
  component: any,
  props: any
  path: string,
  exact: boolean,
}

// This component creates a Route where the child component that it renders contains the passed in props.
const AppliedRoute: React.FC<RouteProps> = ({ component: C, props: cProps, ...rest }) =>
  <Route {...rest} render={props => <C {...props} {...cProps} />} />;

export default AppliedRoute;