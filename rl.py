# rl.py
# attempt at reinforcement learning
from random import randint

values = {}
#values = {(1, 2):3,
#    (4, 5):6
#}
#print(values)
#print(values[(4, 4)])
# [currscore, action taken]: reward

for i in range(50):
    currscore = randint(10, 22)
    if ((currscore, 1) not in values):
        if ((currscore, 2) not in values):
            print("Neither exist, try option 2")
            values[(currscore, 2)] = 2
        else:
            print("2 exists, try option 1")
            values[(currscore, 1)] = 1
    elif ((currscore, 2) not in values):
        print("2 doesn't exist, try option 2")
        values[(currscore, 2)] = 2
    else:
        print("both exist, try the better one")

print("")
print("")
print(values)
