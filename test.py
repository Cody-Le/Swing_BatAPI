import requests



url = "http://127.0.0.1:5000/highscore"

data = {
    "uid_token" : "chickee",
    "highscore" : 100,
    "skin" : "default",
    "name" : "chillaboh"
}

print(data)
post_response = requests.post(url, data = data)
print(post_response.json())