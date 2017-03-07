import numpy as np
newset = set() ## unordered
newlist =[ 1,2,4,999,8888,547,7,8999,0,0,999,8888,7]
s2 =[ 5,210,8,999,8888,547,7,8999,50,10,999,88588,17]
newset = set(newlist)
print(newset)
newset.add("555")
print(newset)

lister = [12,"46",'sting', 12.45,54.23,99,-198]
arr = np.asarray(lister)
print(arr)
# set operations
newset.intersection_update(s2)
newset.symmetric_difference(s2)
newset.difference(s2)
newset.union(s2)
newset2 = newset.copy()