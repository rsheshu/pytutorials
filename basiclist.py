my_list = [100, 300, 200, 100, 300, 100]
print(my_list)

nodumps = set(my_list)
nodumps.remove(max(nodumps))
print(max(nodumps))

my_list += ["this is new list"] * 2
print(my_list)
my_list.append("new apped")
print(my_list)
my_list.pop(1)  # using the index to pop
# my_list.sort()
my_list.reverse()
newzero = [0] * 3
print(newzero)

print(my_list.append(newzero))
print(my_list.extend(nodumps))
# my_list.remove(1)
my_list.pop()
# my_list.index(1)
my_list = []
# my_list.insert("6")
my_list.insert(0,10)
my_list.insert(0,20)
my_list.insert(0,30)
my_list.insert(0,40)
my_list.insert(0,50)
my_list.insert(0,60)
print(my_list)




