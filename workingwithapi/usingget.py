import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
response.raise_for_status()
data = response.json()
print(type(data))
# print(data)
print(data[0])
print(type(data[0]))