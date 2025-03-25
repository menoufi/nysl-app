import { initializeApp } from "firebase/app";
import { getDatabase, ref, set, onValue } from "firebase/database";
import { getAuth, GoogleAuthProvider, signInWithPopup, signOut } from "firebase/auth";
import { useAuthState } from "react-firebase-hooks/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAlx-nFxT8_gqmdt6MJv3L43AUMQMrJ_ws",
  authDomain: "nysl-app-f54e2.firebaseapp.com",
  projectId: "nysl-app-f54e2",
  storageBucket: "nysl-app-f54e2.appspot.com", 
  messagingSenderId: "56852558633",
  appId: "1:56852558633:web:6682c3f84157d786837d38"
};

const app = initializeApp(firebaseConfig);

const database = getDatabase(app);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export const signInWithGoogle = () => signInWithPopup(auth, provider);
export const signOutUser = () => signOut(auth);
export const useUserState = () => useAuthState(auth);

export const setData = (path, value) => set(ref(database, path));
export const onDataChange = (path, callback) =>
  onValue(ref(database, path), snapshot => {
    callback(snapshot.val());
  });

