from flask import Flask
from flask import request
from firebase import add_highscore
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/highscore", methods=["POST"])
def upload_highscore():
    if(request.method != "POST"):
        return {"status":"request error: not post"}
    form = request.form
    print(form)
    if(not check_form_valid(form)):
        return {"status":"request error: lacks or contains invalid keys"}
    add_highscore(form["uid_token"], form["highscore"], form["skin"], form["name"])

    return {"status": "upload successfully"}

#Check for form contains all the neccesary keys
def check_form_valid(form : dict) -> bool:
    require_keys = ["highscore", "skin", "name", "uid_token"]
    for key in require_keys:
        if(not key in form.keys()):
            return False
    return True
