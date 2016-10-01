import random

dc = ["curt", "Eli", "Juanito", "Carebear", "Kevin", "Copes", "Rob", "Jesslynn", "Key", "Jason", "Ben", "Trista", "Matt", "Autumn", "Dom", "ShooHAY"]

pairsDict = {}


while len(dc) > 0:
    #for randomly created indices, respective names are popped out
    rng1 = random.randrange(0, len(dc))
    name1 = dc.pop(rng1)
    print rng1
    print name1

    rng2 = random.randrange(0, len(dc))
    name2 = dc.pop(rng2)
    print rng2
    print name2
    # selecetd names are paired in Dict
    pairsDict[name1] = name2


for key, value in pairsDict.items():
    print "Pair: %s and %s" % (key, value)
