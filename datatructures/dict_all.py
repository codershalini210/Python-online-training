# d = {"name":"a","age":25}
# print(d)
# d.clear() # removes all the key value pair from your dictionary
# print(d)
# .................................................
# d = {"name":"a","age":25}
# e=d # copies ref only
# e = d.copy()  #creates shallow copy of dict.
# print("d :",d)
# print("e: ",e)
# e["name"] = "alex"
# print("d :",d)
# print("e: ",e)
# ---------------------
d={"name":"Alex","age":25,"Email":"Alex@gmail.com"}
print(d)
# d.pop("Email")
# print(d)
d["Contact"]="45665464"
d["Address"]="123,kdlfj"
print(d.popitem()," got removed")
print(d)