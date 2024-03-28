import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("swingbat-bdb0a-firebase-adminsdk-4ug1i-289382d2da.json")

app = firebase_admin.initialize_app(cred)
db = firestore.client()



def add_highscore(uid, highscore, skin, name):
    print("adding highscore")
    doc_ref = db.collection("weekly_scores").document(uid)
    doc_ref.set({
        "highscore": highscore,
        "skin": skin,
        "name": name
    })
    pass

