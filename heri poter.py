import random as rand

wizards = 180
car = [0, 0, 0, 0, 0, 0]
train = [[0] * 6 for i in range(35)]

while wizards > 0:
    x, y = rand.randint(0, 34), rand.randint(0, 5)
    if not train[x][y] == 1:
        train[x][y] = 1
        wizards -= 1
print(train)
changed = []
dementors = 14
while dementors > 0:
    x, y = rand.randint(0, 34), rand.randint(0, 5)
    if not train[x][y] == 0:
        train[x][y] = 0
        if x + 1 not in changed:
            changed.append(x + 1)
        dementors -= 1
print(train)
print(changed)
