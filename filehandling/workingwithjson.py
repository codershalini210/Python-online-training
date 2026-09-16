# import json
# data ={
#     "title":"First Article",
#     "desc":"Description of first article",
#     "status":"Pending"
# }
# with open("./data/articles.json","w") as f:
#     json.dump(data,f,indent=4)
# print("data written to articles.json")

# ........................
import json
with open("./data/articles.json","r") as f :
    data = json.load(f)
    print(data)
