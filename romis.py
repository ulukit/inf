import random as rand

statistics_sum={
 "1": 0,
 "2": 0,
 "3": 0,
 "4": 0,
 "5": 0,
 "6": 0,
}

sum_dice = 0
history = []

while sum_dice < 1000:
    sum_dice = statistics_sum["1"] + statistics_sum["2"] * 2 + statistics_sum["3"] * 3 \
          + statistics_sum["4"] * 4 + statistics_sum["5"] * 5 + statistics_sum["6"] * 6
    throw = rand.randint(1, 6)
    history.append(throw)
    statistics_sum[str(throw)] += 1

print(statistics_sum)
print("Most common throw: " + max(statistics_sum, key=statistics_sum.get))
print(history)
print(sum(history)/len(history))
print("sum of 1's: " + str(statistics_sum["1"]) + "\n" + "sum of 2's: " + str(statistics_sum["2"]*2) + "\n" +\
      "sum of 3's: " + str(statistics_sum["3"]*3) + "\n" + "sum of 4's: " + str(statistics_sum["4"]*4) + "\n" +\
      "sum of 5's: " + str(statistics_sum["5"]*5) + "\n" + "sum of 6's: " + str(statistics_sum["6"]*6) + "\n")