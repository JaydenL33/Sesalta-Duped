import React from "react";
import firebase from "firebase/app";
import "firebase/auth";
// import axios from "axios";
// import LoginForm from "../components/LoginForm";

const firebaseConfig = {
  apiKey: process.env.REACT_APP_apiKey,
  authDomain: process.env.REACT_APP_authDomain,
  databaseURL: process.env.REACT_APP_databaseURL,
  projectId: process.env.REACT_APP_projectId,
  storageBucket: process.env.REACT_APP_storageBucket,
  messagingSenderId: process.env.REACT_APP_messagingSenderId,
  appId: process.env.REACT_APP_appId
};

AuthProvider.actions = {
  setUser: "SET_USER",
  toggleLoading: "TOGGLE_LOADING"
};

const reducer = (state: any, action: any) => {
  switch (action.type) {
    case AuthProvider.actions.setUser:
      return {
        user: action.payload.user,
        isInitiallyLoading: false,
        isLoading: false
      };
    case AuthProvider.actions.toggleLoading:
      return {
        ...state,
        isLoading: action.payload.value
      };
    default:
      throw new Error(`No case for type ${action.type} found.`);
  }
};

const AuthContext = React.createContext(undefined);

export function AuthProvider({ initialUser, children }: any) {
  const [state, dispatch] = React.useReducer(reducer, {
    isInitiallyLoading: true,
    isLoading: false,
    user: null
  });

  const signingInSoDontDispatchOnAuthStateChange = React.useRef(false);
  React.useEffect(() => {
    // Setup Firebase authentication state observer and get user data.
    if (!firebase.apps.length) {
      firebase.initializeApp(firebaseConfig);
    }

    firebase.auth().onAuthStateChanged(async function(user) {
      if (user) {
        // User is signed in.
        console.log("if");
        if (signingInSoDontDispatchOnAuthStateChange.current) {
          console.log("the other if");
          signingInSoDontDispatchOnAuthStateChange.current = false;
          return;
        }

        dispatch({
          type: AuthProvider.actions.setUser,
          payload: {
            user
          }
        });
        // gonna check if user exists in the backend, if not then ask for public name
        // console.log(user.email);

        // const url = `${process.env.REACT_APP_API_URL}/api/user/get_id/?email=${user.email}`;
        // const response = await axios.get(url);
        // if (response.data === "None") {
        // }

        // console.log(response, "the res");
      } else {
        // User is signed out.
        console.log("else");
        dispatch({
          type: AuthProvider.actions.setUser,
          payload: {
            user: null
          }
        });
      }
      console.log("on state changed");
    });
  }, []);

  const signin = () => {
    toggleLoading(true);

    return firebase
      .auth()
      .signInWithPopup(new firebase.auth.GoogleAuthProvider())
      .catch(function(error) {
        // Handle Errors here.
        const errorCode = error.code;
        const errorMessage = error.message;
        console.log("errorCode", errorCode, "errorMessage", errorMessage);
      });
  };

  const signout = () => {
    toggleLoading(true);

    firebase
      .auth()
      .signOut()
      .then(function() {
        // Sign-out successful.
        toggleLoading(false);
      })
      .catch(function(error) {
        // An error happened.
        toggleLoading(false);
      });
  };

  const toggleLoading = (isLoading: boolean) => {
    dispatch({
      type: AuthProvider.actions.toggleLoading,
      payload: {
        value: isLoading
      }
    });
  };

  const value = {
    user: initialUser || state.user,
    signin,
    signout,
    isLoading: state.isLoading
  };

  return state.isInitiallyLoading ? null : (
    // @ts-ignore
    <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
  );
}

export default function useAuth() {
  const context = React.useContext(AuthContext);

  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }

  return context;
}
