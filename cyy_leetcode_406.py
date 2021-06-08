people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
people.sort(key=lambda x:(-x[0],x[1]))
print(people)
res=[]
for p in people:
    res.insert(p[1],p)
print(res)