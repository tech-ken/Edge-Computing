import pyrebase
import os

dirpathSecrets = os.getcwd() + "/firebase_secrets.json"

firebaseConfig = {
  "apiKey": "AIzaSyCCL8LNWfr2Ri2wSOV8rjlbxZ4S1SWRWco",
  "authDomain": "tum-food-app.firebaseapp.com",
  "databaseURL": "https://tum-food-app.firebaseio.com",
  #"projectId": "tum-food-app",
  "storageBucket": "tum-food-app.appspot.com",
  #"messagingSenderId": "811530983997",
  #"appId": "1:811530983997:web:12889ab162f54f3f1be854",
  #"measurementId": "G-ZTTXZQNQE8",
  "serviceAccount": dirpathSecrets
}

#not used
firestoreConfig = {
  "type": "service_account",
  "project_id": "tum-food-app",
  "private_key_id": "deleted due to confidential information",
  "private_key": "deleted due to confidential information",
  "client_email": "tum-food-app-firestore@tum-food-app.iam.gserviceaccount.com",
  "client_id": "113945342687711934984",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tum-food-app-firestore%40tum-food-app.iam.gserviceaccount.com"
}


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()
