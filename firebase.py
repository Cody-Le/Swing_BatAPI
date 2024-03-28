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

def reset_leaderboard():
    doc_ref = db.collection("weekly_scores")


def delete_collection(coll_ref, batch_size):
    if batch_size == 0:
        return

    docs = coll_ref.list_documents(page_size=batch_size)
    deleted = 0

    for doc in docs:
        print(f"Deleting doc {doc.id} => {doc.get().to_dict()}")
        doc.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)


def save_general(general_info: dict):
    doc_ref = db.collection("general").document("general")
    doc_ref.set(general_info)

def get_general():
    pass