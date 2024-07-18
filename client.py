import requests

res = requests.get("http://127.0.0.1:8000/items/sample")

print(res.status_code)
print(res.text)

#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/docs

