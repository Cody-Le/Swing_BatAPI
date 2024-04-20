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

def read_top100():
    scores = db.collection("weekly_scores").order_by("highscore", direction=firestore.Query.DESCENDING).limit(10).stream()
    rank = 1
    ranked_doc = {"doc": []}
    for score in scores:
        ranked_doc["doc"].append(score.to_dict())

    return ranked_doc

def read_rank(uid):
    scores = db.collection("weekly_scores").order_by("highscore", direction=firestore.Query.DESCENDING).get()
    rank = 1
    for score in scores:
        if(score.id == uid):
            return {"status": 1, "message": "successful", "rank": rank, "highscore" : score.to_dict()["highscore"]}
        rank += 1

    return {"status": -1, "message": "no player"}

def reset_leaderboard():
    collect_ref = db.collection("weekly_scores")
    delete_collection(collect_ref)


#Function copied from the firebase document website lol :D
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


if(__name__ == "__main__"):
    print(read_top100())