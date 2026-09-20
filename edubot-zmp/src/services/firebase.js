import firebase from 'firebase/app';
import 'firebase/database';

const firebaseConfig = { databaseURL: "https://gamhoctap-default-rtdb.asia-southeast1.firebasedatabase.app" };

if (!firebase.apps.length) {
  firebase.initializeApp(firebaseConfig);
}

export const db = firebase.database();
export default firebase;
