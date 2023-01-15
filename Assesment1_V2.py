import random

def room1():
    safe_code = []
    while len(safe_code) < 3:
        code = random.randint(3, 12)
        if code not in safe_code:
            safe_code.append(code)

    codes_cracked = 0
    attemptsMade = 0

    while codes_cracked < 3 and attemptsMade < 3:
        for x in safe_code:
            print("The code is", x)
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                if num2 == 1:
                    raise ValueError("You can't pick one for the second number")
                    break
                if num1 / num2 == x:
                    print("Code cracked")
                    ++ codes_cracked
                if num1 / num2 != x:
                    print("Incorrect code")
                    ++ attemptsMade
            except ValueError:
                print("That is not a number")
                break

    else:
        print("Safe opened")
        return
nextStage = False

while nextStage == False:
    gameStart = input("""You awake from a deep sleep and find yourself in a barren, pentagon shaped room. There is 
    a door on each wall of the room, including a large steel door labeled 'E' with a four code lock. On this door, there
     is a small note that reads: 'Forfeit your life, or challenge the Pentagon'. Do you accept the challenge? """)

    try:

        if gameStart.lower() in ["y", "yes"]:
            print("""With not many other options, you yell at the top of your lungs that you accept this challenge.
            Suddenly, your hear four the sound of four locks unlocking. Aside from the large metal door, you realise
            that the other doors are unlocked, labeled from A to D. Which door will you check first?""")
            nextStage = True

        elif gameStart.lower() in ["n", "no"]:
            print("""With how incredibly silly this situation is, you simply tear up the note and begin looking for
            alternate escape routes. Soon after, the ground begins to quake and a hole slowly begins to extend to the
            edges of the room. With nowhere to run, you wait for your inevitable demise, as you finally sink into
            the hole; the deep dark abyss, where your tale ends...""")
            nextStage = False

        else:
            raise ValueError("I can't have that as an answer!")
    except :
            print("I can't have that as an answer!")
            nextStage = False

while nextStage == True:
    doorChoice = input()
    if doorChoice.lower() == "a":
        room1()


