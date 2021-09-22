import requests

r = requests.get("http://localhost:8080/all")

rPost = requests.post(url="http://localhost:8080/add",json={
    "profileName": "112",
    "profileHandle": "cobra2.0",
    "profileIconUrl": "who other thatn cobra",
    "tagLine": "cobra",
    "followers": "32M"
},
                      )
print(rPost.status_code)
print(rPost.text)

print("List of all profiles are")
print(r.status_code)
print(r.text)