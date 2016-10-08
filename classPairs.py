import random
import pickle
from os.path import exists

dcList = ["curt", "Eli", "Juanito", "Carebear", "Kevin", "Copes", "Rob", "Jesslynn", "Key", "Json", "Ben", "Trista", "Matt", "Autumn", "Dom", "ShooHAY"]


print 'loading previous pairs'
previous_file = open('previous.pickle', 'r')
previousDict = pickle.load(previous_file)
print previousDict
# previous_file.close()

# previousDict = {'Carebear': 'Copes', 'Dom': 'Kevin', 'curt': 'Jesslynn', 'Key': 'Autumn', 'Json': 'ShooHAY', 'Juanito': 'Rob', 'ShooHAY': 'Matt', 'Eli': 'Trista'}

def rndmPairs():

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
    previous_file = open('previous.pickle', 'a')
    pickle.dump(pairsDict, previous_file)
    previous_file.close()
    # print 'previousdict saved'
    # print previousDict
    # print pairsDict

rndmPairs()
