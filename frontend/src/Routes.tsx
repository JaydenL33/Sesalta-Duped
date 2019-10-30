import React from "react";
import { Switch, BrowserRouter, Route } from "react-router-dom";
import GamePlayPage from "./pages/GamePlayPage";
// import GameModePage from "./pages/GameModePage";
import GameOptionsPage from "./pages/GameOptionsPage";
import AppliedRoute from "./components/AppliedRoute";
import NotFound from "./pages/NotFound";
// import AuthenticatedRoute from "./components/AuthenticatedRoute";
// import UnauthenticatedRoute from "./components/UnauthenticatedRoute";

interface RouteProps {
  appProps: any,
}

const Routes : React.FC<RouteProps> = 
 ({ appProps }) =>
  <BrowserRouter>
    <Switch>
      {/* <AppliedRoute path="/" exact component={Home} props={childProps} /> */}
      {/* <AppliedRoute path="/mode" exact component={GameModePage} props={appProps} /> */}
      <AppliedRoute path="/game/play" exact component={GamePlayPage} props={appProps} />
      <AppliedRoute path="/game/options" exact component={GameOptionsPage} props={appProps} />
      { /*  catch all unmatched routes */ }
      <Route component={NotFound} />
    </Switch>
  </BrowserRouter>;

export default Routes ;