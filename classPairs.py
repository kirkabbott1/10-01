import random

def rndmPairs():
    dcList = ["curt", "Eli", "Juanito", "Carebear", "Kevin", "Copes", "Rob", "Jesslynn", "Key", "Jason", "Ben", "Trista", "Matt", "Autumn", "Dom", "ShooHAY"]

    previousDict = {'Carebear': 'Copes', 'Dom': 'Kevin', 'curt': 'Jesslynn', 'Key': 'Autumn', 'Jason': 'ShooHAY', 'Juanito': 'Rob', 'ShooHAY': 'Matt', 'Eli': 'Trista'}

    pairsDict = {}


    while len(dcList) > 0:
        #for random index of range, respective name is popped out
        rng1 = random.randrange(0, len(dcList))
        name1 = dcList.pop(rng1)

        rng2 = random.randrange(0, len(dcList))
        name2 = dcList.pop(rng2)

        if (name1, name2) and (name2, name1) not in previousDict.items():
        #  name2 value paired to name1 key in pairsDict
            pairsDict[name1] = name2
        # print dc
        else:
            continue

    i = 1
    for key, value in pairsDict.items():
        print "Pair %d: %s and %s" % (i, key, value)
        i += 1
rndmPairs()
