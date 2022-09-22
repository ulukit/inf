import random as rand
words = ["vampir", "bubulak", "femboy", "gremlin", "krumple"]
word = words[rand.randint(0,len(words)-1)]
guess = []
lives = 5
mistakes = lives
#print(word)
for a in range(len(word)):
    guess.append("_")
while lives > 0 and "_" in guess:
    print("You made " + str(mistakes - lives) + " mistakes and have " + str(lives) + " lives")
    for a in range(len(guess)):
        print(guess[a], end=" ")
    print("\n")
    letter = str.lower(input("Guesss a letter: "))
    if word.find(letter) == -1:
        lives -= 1
        print("Wrong guess")
    elif letter in guess:
        lives -= 1
        print("Pismeno si uz hadal")
    else:
        position = [i for i in range(len(word)) if word.startswith(letter, i)]
        for c in range(len(position)):
            guess[position[c]] = letter
if lives == 0:
    print("You lost and made " + str(mistakes - lives) + " mistakes")
else:
    print("You won and made " + str(mistakes - lives) + " mistakes")