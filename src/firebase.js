import { initializeApp } from "firebase/app";
import {
  getDatabase,
  ref,
  set,
  onValue,
  push
} from "firebase/database";
import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
  signOut
} from "firebase/auth";
import { useAuthState } from "react-firebase-hooks/auth";
import { useList } from "react-firebase-hooks/database";
import {
  getStorage,
  ref as storageRef,
  uploadBytes,
  getDownloadURL
} from "firebase/storage";


const firebaseConfig = {
  apiKey: "AIzaSyAlx-nFxT8_gqmdt6MJv3L43AUMQMrJ_ws",
  authDomain: "nysl-app-f54e2.firebaseapp.com",
  databaseURL: "https://nysl-app-f54e2-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "nysl-app-f54e2",
  storageBucket: "nysl-app-f54e2.firebasestorage.app",
  messagingSenderId: "56852558633",
  appId: "1:56852558633:web:6682c3f84157d786837d38",
  measurementId: "G-SBKXE6RTL2"
};

const app = initializeApp(firebaseConfig);

const database = getDatabase(app);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();
const storage = getStorage(app);

export const signInWithGoogle = () => signInWithPopup(auth, provider);
export const signOutUser = () => signOut(auth);
export const useUserState = () => useAuthState(auth);


export const useGameMessages = (gameId) =>
  useList(ref(database, `messages/${gameId}`));

export const addMessage = (gameId, message) => {
  const newMessageRef = push(ref(database, `messages/${gameId}`));
  return set(newMessageRef, {
    ...message,
    timestamp: Date.now()
  });
};


export const uploadPicture = (path, file) =>
  uploadBytes(storageRef(storage, path), file);

export const getPictureUrl = (fileRef) =>
  getDownloadURL(fileRef);

export const savePictureData = (gameId, data) =>
  push(ref(database, `pictures/${gameId}`), {
    ...data,
    timestamp: Date.now()
  });

export const useGamePictures = (gameId) =>
  useList(ref(database, `pictures/${gameId}`));


export const setData = (path, value) =>
  set(ref(database, path), value);

export const onDataChange = (path, callback) =>
  onValue(ref(database, path), snapshot => {
    callback(snapshot.val());
  });

  export { storage };

















