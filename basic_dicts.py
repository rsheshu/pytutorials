dd = {}
dd[1] = 0
newdict = {"key1": 0, "key2": 2, "key3": 3}

#3 printing only the keys ( please check the syntax)
for key in newdict:
    print(newdict[key])

for key1, val1 in newdict.items():
    print(key1)
    print(val1)

print(newdict)
newdict.keys()
newdict.values()
print(newdict.items())

sqrDics = {vars : vals **2 for vars, vals in zip([x for x in range(1,10)],range(10))}
print(sqrDics)