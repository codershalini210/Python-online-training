users = ["a","b","c","a","d","c","e","f"]
seen = set()
for u in users:
    if(u in seen):
        print(u," already seen")
    else:
        print(u," new user added")
        seen.add(u)
        