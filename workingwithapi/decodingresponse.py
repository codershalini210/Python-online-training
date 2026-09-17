import requests
url = "https://jsonplaceholder.typicode.com/posts/"
# https://jsonplaceholder.typicode.com/posts/10
params = {"id":1}
response = requests.get(url,params)
data = response.json()
# print(type(data))
# if isinstance(data,list) and data:
#     print(data[0])
#     print(data[0].keys())
#     print("Total no of records ",len(data))
# elif isinstance(data,dict):
#     print(data.keys())

for post in data:
    title = post.get("title","untitled")
    body = post.get("body","NO content")
    print("title : ",title," \n body : ",body)
    print("______________________________")

