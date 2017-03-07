added = lambda x,y: x + y
print(added(9, 6))

numbers = lambda x: x**2
#numbers = lambda x,y: x*y
#
# for nos in [1, 23, 4, 5, 8]:
#     print(numbers(nos))
newlist1 = [1, 23, 4, 5, 8]
newlist2 = [10, 11, 4, 7, 8, 10,23]
mappedlist = list(filter(numbers, newlist1))

print(mappedlist)

## newno = reduce(max,newlist)

def primenum(numx):
    for i in range(2, numx-1):
        if numx % i == 0:
            return False
        return True

primee = lambda numx: primenum(numx)
mappedlist = list(filter(primee, newlist2))
print(mappedlist)

ziplist = list(zip(newlist1, newlist2))
print(ziplist)

dict = {"k1": 1}
dict1 = {"K2": 2}
