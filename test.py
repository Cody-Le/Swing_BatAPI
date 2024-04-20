import requests



url = "http://127.0.0.1:5000/topscores"

data = {
    "uid_token" : "chickee",
    "highscore" : 100,
    "skin" : "default",
    "name" : "chillaboh"
}

print(data)
#post_response = requests.post(url, data = data)
post_response = requests.get(url)
print(post_response.json())