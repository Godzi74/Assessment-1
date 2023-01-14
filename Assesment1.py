
while True:
    gameStart = input.lower("""You awake from a deep sleep and find yourself in a barren, pentagon shaped room. There is 
    a door on each wall of the room, including a large steel door with a four code lock. On this door, there is a small
     note that reads: 'Forfeit your life, or challenge the Pentagon'. Do you accept the challenge? """)

    if gameStart in ["y", "yes"]:
        print("""With not many other options, you yell at the top of your lungs that you accept this challenge.
        Suddenly, your hear four the sound of four locks unlocking. Aside from the large metal door, you realise
        that the other doors are unlocked. Which door will you enter first?""")
