import random as rand

statistics_sum={

}
history = []
throw_sum = 0
while throw_sum < 1000:
    for a in range(2):
        throw = rand.randint(2,12)
        history.append(throw)
        if str(throw) not in statistics_sum:
            statistics_sum[str(throw)] = 0
        statistics_sum[str(throw)] += throw
    throw_sum = sum(statistics_sum.values())
for a in range(len(statistics_sum)):
    statistics_sum[str(a+2)] = statistics_sum[str(a+2)]/(a+2)
print(statistics_sum)
print("Most common value: " + str(max(statistics_sum, key=statistics_sum.get)))
print(sum(history)/len(history))
print(history)
for a in range(len(statistics_sum)):
    print("Sum of all " + str(a+2) + "'s: " + str(statistics_sum[str(a+2)]*(a+2)))