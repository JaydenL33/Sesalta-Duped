import React from "react";
import firebase from "firebase";
import useAuth from "../utils/AuthContext";
import StyledFirebaseAuth from "react-firebaseui/StyledFirebaseAuth";
import Button from "@material-ui/core/Button";
import { useHistory } from "react-router-dom";

export default function LoginButton() {
  const { isLoading, user, signin, signout } = useAuth();
  const history = useHistory();

  const uiConfig: any = {
    // Configure FirebaseUI.
    // Popup signin flow rather than redirect flow.
    signInFlow: "popup",
    // We will display Google as auth providers.
    signInOptions: [firebase.auth.GoogleAuthProvider.PROVIDER_ID],
    callbacks: {
      // Avoid redirects after sign-in.
      signInSuccessWithAuthResult: () => {
        setTimeout(() => {
          history.push("/");
        }, 1000);
      }
    }
  };

  return !!user ? (
    <Button color="inherit" onClick={signout} style={{ cursor: "pointer" }}>
      Sign Out
    </Button>
  ) : (
    <StyledFirebaseAuth uiConfig={uiConfig} firebaseAuth={firebase.auth()} />
  );
}
