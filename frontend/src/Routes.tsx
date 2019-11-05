import React from "react";
import { Switch, Route } from "react-router-dom";
import { Redirect } from 'react-router';
import NotFound from "./pages/NotFound";
import GamePlayPage from "./pages/GamePlayPage";
import GamePlayPageMap from "./pages/GamePlayPageMap";
import GameModePage from "./pages/GameModePage";
import GameModePageJp from "./pages/GameModePage-jp";
import GameOptionsPage from "./pages/GameOptionsPage";
import GameOptionsPageJp from "./pages/GameOptionsPage-jp";
import GamePlayPageCapital from "./pages/GamePlayPageCapital";
import AppliedRoute from "./components/AppliedRoute";
// import AuthenticatedRoute from "./components/AuthenticatedRoute";
// import UnauthenticatedRoute from "./components/UnauthenticatedRoute";

interface RouteProps {
  appProps: any,
}

const Routes : React.FC<RouteProps> = 
 ({ appProps }) =>
    <Switch>
      <Route exact path="/" render={() => (
        <Redirect to="/en"/>
      )} props={appProps}/>
      <AppliedRoute path="/en" exact component={GameModePage} props={appProps} />
      <AppliedRoute path="/en/game/play" exact component={GamePlayPage} props={appProps} />
      <AppliedRoute path="/en/game/play/map" exact component={GamePlayPageMap} props={appProps} />
      <AppliedRoute path="/en/game/play/capital" exact component={GamePlayPageCapital} props={appProps} />
      <AppliedRoute path="/en/game/options" exact component={GameOptionsPage} props={appProps} />
      <AppliedRoute path="/en/game" exact component={GameModePage} props={appProps} />
      <AppliedRoute path="/jp/game" exact component={GameModePageJp} props={appProps} />
      <AppliedRoute path="/jp/game/options" exact component={GameOptionsPageJp} props={appProps} />
      { /*  catch all unmatched routes */ }
      <Route component={NotFound} />
    </Switch>

export default Routes ;
