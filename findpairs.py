pairList = [1, 5, 3, 9, 8, 2, 7, 9, 2, 9]

sumx = 10
seen_set = set()
output_set = set()

for vals in pairList:
    nos = sumx - vals
    if vals in seen_set:
        output_set.add((max(vals, nos), min(vals, nos)))
    else:
        seen_set.add(nos)
print(output_set)
