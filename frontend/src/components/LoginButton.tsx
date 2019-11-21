import React from 'react';
import firebase from 'firebase';
import useAuth from '../utils/AuthContext';
import StyledFirebaseAuth from 'react-firebaseui/StyledFirebaseAuth';

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

  return !!user ? (
    <a onClick={signout} style={{ cursor: 'pointer' }}>
      Sign Out
    </a>
  ) : (
    <StyledFirebaseAuth uiConfig={uiConfig} firebaseAuth={firebase.auth()} />
  );
}
