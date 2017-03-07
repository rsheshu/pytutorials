from collections import OrderedDict
encodeStr = "AAAAbbbbEEEeeRRRRRRrrgggggTTTT"

encodeDict = OrderedDict()
for letters in encodeStr:
    if letters in encodeDict:
        encodeDict[letters] += 1
    else:
        encodeDict[letters] = 1
newStr = str()
for k, v in encodeDict.items():
    newStr = newStr + str(k) + str(v)

print(newStr)