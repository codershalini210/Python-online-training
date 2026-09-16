s = {1,2,3}
s.add(4)
s.add(5)
s.update([25,65,41])
s.remove(1)
print(s)
# s.remove(11)  #since 11 is not in the set its give  an err 
s.discard(11) 
print(s)
s.pop()
print(s)
s.clear()
print(s)