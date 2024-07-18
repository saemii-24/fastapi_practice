import requests

# res = requests.get("http://127.0.0.1:8000/items/sample")

# print(res.status_code)
# print(res.text)

#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/docs


res = requests.get("http://127.0.0.1:8000/items")

print(res.status_code)
print(res.text)

postRequest = requests.post("http://127.0.0.1:8000/items/", json={
  "name":"티셔츠", "price":2000, "description":"흰 티셔츠"
})

print(postRequest.status_code)
print(postRequest.text)

headerRes = requests.get("http://127.0.0.1:8000/sample/", headers={"Authorization": "bearer A1B2C3D4"})

print(headerRes.status_code)
print(headerRes.text)
print(headerRes.headers)