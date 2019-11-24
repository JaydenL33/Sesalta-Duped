import React from 'react';
import firebase from 'firebase';
import useAuth from '../utils/AuthContext';
import StyledFirebaseAuth from 'react-firebaseui/StyledFirebaseAuth';
import Button from '@material-ui/core/Button';


export default function LoginButton() {
  const { isLoading, user, signin, signout } = useAuth();

  const uiConfig: any = {
    // Configure FirebaseUI.
    // Popup signin flow rather than redirect flow.
    signInFlow: 'popup',
    // We will display Google as auth providers.
    signInOptions: [firebase.auth.GoogleAuthProvider.PROVIDER_ID],
    callbacks: {
      // Avoid redirects after sign-in.
      signInSuccessWithAuthResult: () => false,
    },
  };
  
  let LogoutText;
  
  if (window.location.pathname.substr(1, 2) === 'jp') {
    LogoutText = "サインアウト";
  } else {
    LogoutText = "Sign Out";
  }

  return !!user ? (
    <Button
      color="inherit"
      onClick={signout} style={{ cursor: 'pointer' }}
    >
      {LogoutText}
    </Button>
    
  ) : (
    <StyledFirebaseAuth uiConfig={uiConfig} firebaseAuth={firebase.auth()} />
  );
}
