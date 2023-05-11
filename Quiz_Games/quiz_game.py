print("Welcome to *Test Your Computer Knowledge!* ")

playing = input("Do you want to proceed to the questions? ")

if playing.lower() != "yes":
    quit()
    
print("Let the games begin!")
score = 0

Answer = input("Does vi create a file? ").lower()
if Answer == "yes":
    print('correct!')
    score +=1
else:
    print('incorrect')
Answer = input("What does CPU stand for? ")
if Answer.upper() == "central processing unit":
    print('correct!')
    score +=1
else:
    print('incorrect')
    
Answer = input("What does GPU stand for? ")
if Answer.upper() == "graphic processing unit":
    print('correct!')
    score +=1
else:
    print('incorrect')
    
print("You got " + str(score) + " points")

print("You got " + str((score/3)*100) + " points")