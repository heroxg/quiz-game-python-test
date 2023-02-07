print("Welcome to my computer quiz")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
print("Okay! Let's play")
score = 0

answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("what does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("what does RAM stands for? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer = input("what does PSU stands for? ").lower()
if answer == "power supply":
    print("correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str((score/4) * 100) + "%.")
