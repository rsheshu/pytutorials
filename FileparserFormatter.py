import datetime


def makeSentence(wordline):
    tot = len(wordline)
    fname = ""
    if wordline:
        for nameword in wordline[1:(tot-2)]:
           fname += nameword + " "
        president_name = fname + " " + wordline[0]
        year_servered = wordline[-2] + "  to  " + wordline[-1]
        Sentence = "{president} was president from {years} \n".format(president=president_name,years=year_servered)
        sortedDict[datetime.datetime.strptime(wordline[-2], '%m/%d/%Y')] = Sentence
        sortedlist.append(Sentence)

        fileptr.write(Sentence)
        return Sentence



def process(singleline):
    words = singleline.split()
    #print(lastname)
    newsent = makeSentence(words)
    return newsent
sortedlist = []
sortedDict = {}

fileptr = open('output.txt','w')
with open("data.txt") as filereader:
    newline = ""
    for eachline in filereader:
        newline = process(eachline)

#sortedlist = sorted(sortedlist, key=lambda x: (x[-19:-26]))
print(sortedlist)
sortptr = open("sorted.txt", 'w')
keylist = sortedDict.keys()
keylist.sort()
newList = []

for keys in keylist:
    print(sortedDict[keys])
    sortptr.write(sortedDict[keys])


