print("hello!")
print("lets do math!")
score = "0"
answer1 = input("What is 1 + 1?")

if answer1 == "2":
    print("Correct!")
    score = score+1
else:
    print("Incorrect!")
print("Your score is", answer1)
#start level 2
print("To level 2!")
answer2 = input("what is 7 plus 2?")
if answer2 == "9":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("its getting harder!")
if answer2 == "9" and answer1 == "2":
    print("If you get this question correct you will get double points!")

answer3 = input("What is 10 - 6?")
if answer3 == "4":
    if answer2 == "9" and answer1 == "2":
        print("yay! you got all three questions correct. You have acheived a streak of 3. Keep on going for more prizes! :)")
        score += 2
    else:
        print("you got it right!")
        score += 1
else:
    print("wrong! good try!")
print("Your score is ", score)
print("This is the end for now! Your score was " ,score, "! I update this a few times too! so don't worry!")
