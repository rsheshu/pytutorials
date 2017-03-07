from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

newcaster = """The NASA man credited with writing the most influential paper on flying cars and its feasibility as an
urban transport vehicle, back in 2010, is joining Uber to change our daily commute forever.
Uber gave the most serious signal of intent amongst big companies trying to launch a flying taxi to conquer traffic jams
 once and for all. The Silicon Valley transportation network startup headed by Travis Kalanick hired Mark Moore, a veteran
 NASA engineer, from right under the noses of Google and Airbus -- the other big companies trying to launch their own flying car.
Moore is credited with writing the definitive 2010 paper exploring the feasibility of helicopter-like flying vehicles for
short-haul urban flight
What made Mark Moore walk away from NASA with just one year before he’s eligible for retirement, ditching a substantial
 amount of his pension and free medical insurance for life? He thinks Uber’s vision for VTOL (vertical take-off and landing)
  vehicles for commute is an intriguing one """
newdict = {}
words = newcaster.split()
for word in words:
    if word.lower() in newdict.keys():
        newdict[word.lower()] += 1
    else:
        newdict[word.lower()] = 1
print(newdict)

tempdict = newdict
maxset = list()

for cnt in range(1,6):
    keyy = max(tempdict, key=tempdict.get)
    maxset.append((keyy, tempdict[keyy]))
#    maxset.insert(0, (keyy, tempdict[keyy]))
    ## maxset((keyy, tempdict[keyy]))
    del tempdict[keyy]
print(maxset)





cc = Counter(words)
## print(cc)
print(cc.most_common(5))

defdict = defaultdict(lambda: 0)
defdict["key"] = 10
defdict["key1"] = 10
defdict["key2"] = 10
print(defdict["newKey"])

orddict1 = OrderedDict()
orddict1[1] = 11
orddict1[2] = 22


orddict2 = OrderedDict()
orddict2[1] = 22
orddict2[2] = 11

print(orddict1)
print(orddict2)

Dog = namedtuple('Dog', "name breed color")
Sammy = Dog(name="Sammy",breed="Hsdky",color="Red")
print(Sammy.breed)
