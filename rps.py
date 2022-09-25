import random as rand
win_score = int(input("Points to win: "))
p_score = 0
c_score = 0
counter = 0
rps = ["r", "p", "s"]
history = []
rules = {
    "p": "r",
    "r": "s",
    "s": "p"
}
while p_score<win_score and c_score < win_score:
    counter += 1
    player = str(input("r,p,s: "))
    cpu = rand.choice(rps)
    history.append(str(counter) + ".turn: " + player + "," + cpu)
    if player == rules[cpu]:
        c_score += 1
        print("CPU scores \n score: " + str(p_score) + ", " + str(c_score))
    elif cpu == rules[player]:
        p_score += 1
        print("Player scores \n score: " + str(p_score) + ", " + str(c_score))
    else:
        print("tie \n score: " + str(p_score) + ", " + str(c_score))
    print(history)
if p_score > c_score:
    print("Player wins \n score: " + str(p_score) + ", " + str(c_score))
else:
    print("CPU wins \n score: " + str(p_score) + ", " + str(c_score))
print(history)
