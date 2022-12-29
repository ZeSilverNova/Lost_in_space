input("\033[1;37m\n" + "Press the enter button to scroll the text." + "\033[0m")
print(" ")

input("\033[1;36m\n" + "!!! WARNINGS !!!")
print(" ")

input("Please be aware that pressing the enter button without entering the recquired choices might result in a crash.")
input("The game is also case-sensitive, which mean that your inputs should be written in lower or higher cases accordingly.")
input("Finally, keep in mind that there are no saves since I don't know how to code that yet.")
input("You will however reach several checkpoints during the game where your life will be restored." + "\033[0m")
print(" ")


input("This is an experimental project I made during my free time. Might finish it someday, might not... Who knows.")
input("For now at least I hope you'll enjoy the adventure.")
print(" ")


input("Before we start, let's quickly make acquintance.")

Player_name = input("\033[1;35m\n" + "What is your name ? ")
Name_question = input("\033[1;35m\n" + "Is " + Player_name + " the name you choosed ?" + "\033[1;36m\n" + "[Y]  " + "  [N] ")
Name_answer = Name_question + str("Y")

while Name_question != str("Y"):
    if Name_question != str("Y"):
        if Name_answer != str("Y"):
            Player_name = input("\033[1;35m\n" + "Let me ask you this once again. What is your name ? ")
            Name_question = input("\033[1;35m\n" + "Is " + Player_name + " the name you choosed ?" + "\033[1;36m\n" + "[Y]  " + "  [N] ")
else:
    input("\033[1;37m\n" + "You will be remembered as " + Player_name + "." + "\033[0m")

print(" ")


input("I have no more questions for you " + Player_name + ".")
input("Your new adventure is about to start.")
input("Trust your judgement, follow your instinct and have fun !")
print(" ")


input("\033[1;37m\n" + "Press enter to start.")
print(" ")


def First_chapter ():

    print("Initializing story, please be patient.")
    import time
    my_list = ["." , "   ." , "      ." , "         ." , "            ."]
    for i in my_list:
        time.sleep(0.5)
        print(i)
        print(" ")

    input("\033[1;33m\n" + "\033[1m" + "Lost in space." + "\033[0m")
    print(" ")

    input("You were heading to the moon when your compagny spaceship suddenly got raided by some pirates.")
    input("You knew the whole crew was condemned, and so you promptly left with the emergency shuttle unnoticed.")
    print(" ")

    input("Minutes only after piloting the shuttle, you feel a tremendous impact reverberating through the cabin.")
    input("You quickly glance back to where you came from.")
    input("Your eyes fill with dread as you see the mothership exploding into countless tiny pieces and the pirates heading your way.")
    print(" ")


    Moves = str("UPWARD") , str("DOWNWARD") , str("LEFTWARD") , str("RIGHTWARD" )
    Shuttle_life_points = 8

    print("\033[1;37m\n" + "checkpoint reached" + "\033[0m")
    print(" ")

    input("The pirates are still pretty far, but they're getting closer.")
    input("You firmly grip the handlebars, hoping to distance them.")
    print(" ")

    Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice not in Moves:
        print("\033[1;37m\n" + "The options are UPWARD, DOWNWARD, LEFTWARD and RIGHTWARD" + "\033[0m")
        Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice != str("UPWARD"):
        if Shuttle_life_points == 0:
            input("\033[1;31m\n" + "A violent explosion suddenly overwhelms you.")
            input("You slowly lose consciousness as your shuttle shatters into pieces." + "\033[0m")
            quit()

        elif Shuttle_life_points == 1:
            print("\033[1;31m\n" + "Another laser beam hits your shuttle, starting a fire.")
            print("'Focus " + Player_name + " !!!' You mumble in fear." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points == 2:
            print("\033[1;31m\n" + "You feel a tremendous impact in the cockpit.")
            print("A strident alarm goes off." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points <= 5 and Shuttle_life_points >= 3:
            print("\033[1;31m\n" + "A missile crash into your shuttle. The cabin is now heavily damaged.")
            print("You are starting to panick." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        else:
            print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
            print("The pirates are getting closer." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1


    print("\033[1;32m\n" + "Your shuttle rotates upward, narrowly avoiding enemy lasers." + "\033[0m")
    print("The pirates are still after you.")
    print(" ")

    Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice not in Moves:
        print("\033[1;37m\n" + "The options are UPWARD, DOWNWARD, LEFTWARD and RIGHTWARD" + "\033[0m")
        Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice != str("UPWARD"):
        if Shuttle_life_points == 0:
            input("\033[1;31m\n" + "A violent explosion suddenly overwhelms you.")
            input("You slowly lose consciousness as your shuttle shatters into pieces." + "\033[0m")
            quit()

        elif Shuttle_life_points == 1:
            print("\033[1;31m\n" + "Another laser beam hits your shuttle, starting a fire.")
            print("Focus " + Player_name + " !!! You mumble in fear." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points == 2:
            print("\033[1;31m\n" + "You feel a tremendous impact in the cockpit.")
            print("A strident alarm goes off." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points <= 5 and Shuttle_life_points >= 3:
            print("\033[1;31m\n" + "A missile crash into your shuttle. The cabin is now heavily damaged.")
            print("You are starting to panick." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        else:
            print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
            print("The pirates are getting closer." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1


    print("\033[1;32m\n" + "Your shuttle rotates upward.")
    print("You have just dodged a salvo of missiles, which pulverizes a nearby asteroid." + "\033[0m")
    print("The pirates are still after you.")
    print(" ")

    Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice not in Moves:
        print("\033[1;37m\n" + "The options are UPWARD, DOWNWARD, LEFTWARD and RIGHTWARD" + "\033[0m")
        Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice != str("DOWNWARD"):
        if Shuttle_life_points == 0:
            input("\033[1;31m\n" + "A violent explosion suddenly overwhelms you.")
            input("You slowly lose consciousness as your shuttle shatters into pieces." + "\033[0m")
            quit()

        elif Shuttle_life_points == 1:
            print("\033[1;31m\n" + "Another laser beam hits your shuttle, starting a fire.")
            print("Focus " + Player_name + " !!! You mumble in fear." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points == 2:
            print("\033[1;31m\n" + "You feel a tremendous impact in the cockpit.")
            print("A strident alarm goes off." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points <= 5 and Shuttle_life_points >= 3:
            print("\033[1;31m\n" + "A missile crash into your shuttle. The cabin is now heavily damaged.")
            print("You are starting to panick." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        else:
            print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
            print("The pirates are getting closer." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1


    print("\033[1;32m\n" + "Your shuttle dives down, pushing you further away from the pirates." + "\033[0m")
    print("You still have a long way to go.")
    print(" ")

    Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice not in Moves:
        print("\033[1;37m\n" + "The options are UPWARD, DOWNWARD, LEFTWARD and RIGHTWARD" + "\033[0m")
        Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice != str("DOWNWARD"):
        if Shuttle_life_points == 0:
            input("\033[1;31m\n" + "A violent explosion suddenly overwhelms you.")
            input("You slowly lose consciousness as your shuttle shatters into pieces." + "\033[0m")
            quit()

        elif Shuttle_life_points == 1:
            print("\033[1;31m\n" + "Another laser beam hits your shuttle, starting a fire.")
            print("Focus " + Player_name + " !!! You mumble in fear." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points == 2:
            print("\033[1;31m\n" + "You feel a tremendous impact in the cockpit.")
            print("A strident alarm goes off." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points <= 5 and Shuttle_life_points >= 3:
            print("\033[1;31m\n" + "A missile crash into your shuttle. The cabin is now heavily damaged.")
            print("You are starting to panick." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        else:
            print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
            print("The pirates are getting closer." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1


    print("\033[1;32m\n" + "You continue to dive, dodging enemy fire." + "\033[0m")
    print("You still have a long way to go, but you're doing good.")
    print(" ")

    Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice not in Moves:
        print("\033[1;37m\n" + "The options are UPWARD, DOWNWARD, LEFTWARD and RIGHTWARD" + "\033[0m")
        Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice != str("LEFTWARD"):
        if Shuttle_life_points == 0:
            input("\033[1;31m\n" + "A violent explosion suddenly overwhelms you.")
            input("You slowly lose consciousness as your shuttle shatters into pieces." + "\033[0m")
            quit()

        elif Shuttle_life_points == 1:
            print("\033[1;31m\n" + "Another laser beam hits your shuttle, starting a fire.")
            print("Focus " + Player_name + " !!! You mumble in fear." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points == 2:
            print("\033[1;31m\n" + "You feel a tremendous impact in the cockpit.")
            print("A strident alarm goes off." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points <= 5 and Shuttle_life_points >= 3:
            print("\033[1;31m\n" + "A missile crash into your shuttle. The cabin is now heavily damaged.")
            print("You are starting to panick." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        else:
            print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
            print("The pirates are getting closer." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1


    print("\033[1;32m\n" + "You turn sharply left, after spotting an asteroid belt." + "\033[0m")
    print("You start to wonder how much longer they will hunt you.")
    print(" ")

    Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice not in Moves:
        print("\033[1;37m\n" + "The options are UPWARD, DOWNWARD, LEFTWARD and RIGHTWARD" + "\033[0m")
        Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice != str("RIGHTWARD"):
        if Shuttle_life_points == 0:
            input("\033[1;31m\n" + "A violent explosion suddenly overwhelms you.")
            input("You slowly lose consciousness as your shuttle shatters into pieces." + "\033[0m")
            quit()

        elif Shuttle_life_points == 1:
            print("\033[1;31m\n" + "Another laser beam hits your shuttle, starting a fire.")
            print("Focus " + Player_name + " !!! You mumble in fear." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points == 2:
            print("\033[1;31m\n" + "You feel a tremendous impact in the cockpit.")
            print("A strident alarm goes off." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points <= 5 and Shuttle_life_points >= 3:
            print("\033[1;31m\n" + "A missile crash into your shuttle. The cabin is now heavily damaged.")
            print("You are starting to panick." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        else:
            print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
            print("The pirates are getting closer." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1


    print("\033[1;32m\n" + "What looks like a nearby planet catches your eye as you sneak through the asteroid belt." + "\033[0m")
    print("Maybe if you manage to land...")
    print(" ")

    Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice not in Moves:
        print("\033[1;37m\n" + "The options are UPWARD, DOWNWARD, LEFTWARD and RIGHTWARD" + "\033[0m")
        Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice != str("LEFTWARD"):
        if Shuttle_life_points == 0:
            input("\033[1;31m\n" + "A violent explosion suddenly overwhelms you.")
            input("You slowly lose consciousness as your shuttle shatters into pieces." + "\033[0m")
            quit()

        elif Shuttle_life_points == 1:
            print("\033[1;31m\n" + "Another laser beam hits your shuttle, starting a fire.")
            print("Focus " + Player_name + " !!! You mumble in fear." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points == 2:
            print("\033[1;31m\n" + "You feel a tremendous impact in the cockpit.")
            print("A strident alarm goes off." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points <= 5 and Shuttle_life_points >= 3:
            print("\033[1;31m\n" + "A missile crash into your shuttle. The cabin is now heavily damaged.")
            print("You are starting to panick." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        else:
            print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
            print("The pirates are getting closer." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1


    print("\033[1;32m\n" + "You come out of the asteroid belt and head towards the ground." + "\033[0m")
    print("Only one pirate ship remains behind you.")
    print(" ")

    Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice not in Moves:
        print("\033[1;37m\n" + "The options are UPWARD, DOWNWARD, LEFTWARD and RIGHTWARD" + "\033[0m")
        Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")

    while Move_choice != str("RIGHTWARD"):
        if Shuttle_life_points == 0:
            input("\033[1;31m\n" + "A violent explosion suddenly overwhelms you.")
            input("You slowly lose consciousness as your shuttle shatters into pieces." + "\033[0m")
            quit()

        elif Shuttle_life_points == 1:
            print("\033[1;31m\n" + "Another laser beam hits your shuttle, starting a fire.")
            print("Focus " + Player_name + " !!! You mumble in fear." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points == 2:
            print("\033[1;31m\n" + "You feel a tremendous impact in the cockpit.")
            print("A strident alarm goes off." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        elif Shuttle_life_points <= 5 and Shuttle_life_points >= 3:
            print("\033[1;31m\n" + "A missile crash into your shuttle. The cabin is now heavily damaged.")
            print("You are starting to panick." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1

        else:
            print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
            print("The pirates are getting closer." + "\033[0m")
            Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
            Shuttle_life_points = Shuttle_life_points - 1


    print(" ")
    print(" ")
    input("Sensing sudden danger, you sharply turn to the right.")
    input("A massive salvo of laser fire passes in front of you, barely brushing your shuttle.")
    print(" ")

First_chapter ()


def Second_chapter ():


    print("\033[1;37m\n" + "checkpoint reached" + "\033[0m")
    print(" ")

    input("You somehow end up landing without exploding.")
    input("A quick glance at your shuttle tells you not without surprise that it is now out of service.")
    input("As you survey your surroundings with concern, you notice a huge magnetic storm approaching you.")
    input("Not too far from where you are is what looks like an old military base.")
    input("Not having much choice, you go to this structure.")
    print(" ")

    input("You have an uneasy feeling when you walk through the main entrance.")
    input("It's almost as if something were watching you...")
    print(" ")


    def Vanilla_room_1 ():

        directions = ["LEFTWARD", "BACKWARD"]

        userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "LEFTWARD / BACKWARD " + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are LEFTWARD or RIGHTWARD" + "\033[0m")
            userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "LEFTWARD / BACKWARD " + "\033[0m")
            print(" ")

        if userInput == "LEFTWARD":
            print("You take the corridor on your left.")
            Crossroad ()

        elif userInput == "BACKWARD":
            print("You decide to turn around.")
            Main_entrance ()

        else:
            print("Please enter a valid option.")


    def Vanilla_room_2 ():

        directions = ["FORWARD", "RIGHTWARD", "BACKWARD"]

        userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "FORWARD / RIGHTWARD / BACKWARD " + "\033[0m" + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are FORWARD, RIGHTWARD or BACKWARD." + "\033[0m")
            userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "FORWARD / RIGHTWARD / BACKWARD " + "\033[0m" + "\033[0m")
            print(" ")

        if userInput == "FORWARD":
            print("You keep moving forward.")

            input("\033[1;31m\n" + "Something suddenly stabs you in the back as you try to leave the room, blasting a hole in your chest.")
            print(" ")
            input("'Wh.. at.. !?' You whisper in pain.")
            print(" ")
            input("Your brain can't even process what's happening to you.")
            input("Here sadly ends the story of " + Player_name + "." + "\033[0m")
            quit ()

        elif userInput == "RIGHTWARD":
            print("You head for the right.")
            Vanilla_room_3 ()

        elif userInput == "BACKWARD":
            print("You decide to turn around.")
            Main_entrance ()

        else:
            print("Please enter a valid option.")


    def Vanilla_room_3 ():

        directions = ["FORWARD", "LEFTWARD", "BACKWARD"]

        userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "FORWARD / LEFTWARD / BACKWARD " + "\033[0m" + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are FORWARD, LEFTWARD or BACKWARD." + "\033[0m")
            userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "FORWARD / LEFTWARD / BACKWARD " + "\033[0m" + "\033[0m")
            print(" ")

        if userInput == "LEFTWARD":
            print("You head for the left.")
            print(" ")

            input("You feel a huge wave of energy wash over you as you try to leave the room.")
            input("The world slowly begins to fade as you lose consciousness.")
            input("You find yourself at the front doors when you finally wake up.")
            input("You can no longer exit the building this way since the storm is raging outside.")
            print(" ")
            input("'What was that ?' You ask yourself.")
            Main_entrance ()

        elif userInput == "FORWARD":
            print("You keep moving forward.")
            Vanilla_room_4 ()

        elif userInput == "BACKWARD":
            print("You decide to turn around.")
            Vanilla_room_2 ()

        else:
            print("Please enter a valid option.")


    def Vanilla_room_4 ():

        directions = ["FORWARD", "LEFTWARD", "RIGHTWARD", "BACKWARD"]

        print("\033[1;35m\n" + "You entered an empty room. There is a closed door on each wall.")
        userInput = input("Where are you heading ?" + "\033[1;36m\n" + "FORWARD / LEFTWARD / RIGHTWARD / BACKWARD " + "\033[0m" + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are FORWARD, LEFTWARD, RIGHTWARD or BACKWARD." + "\033[0m")
            input("You entered an empty room.")
            input("There is a sealed door on each wall.")
            userInput = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "FORWARD / LEFTWARD / RIGHTWARD / BACKWARD " + "\033[0m" + "\033[0m")
            print(" ")

        if userInput == "LEFTWARD":
            print("\033[1;32m\n" + "The stairs to the basement were just behind the door." + "\033[0m")
            print(" ")

            input("'Where are we going, " + Player_name + " ?' You wonder with doubt.")
            input("Checking behind you one last time, you decide to go down the stairs..")
            Third_chapter ()

        elif userInput == "FORWARD":
            print("You go to the door in front of you.")
            print(" ")

            input("You feel a huge wave of energy wash over you as you unlock the door.")
            input("The world slowly begins to fade as you lose consciousness.")
            input("You find yourself at the front doors when you finally wake up.")
            input("You can no longer exit the building this way since the storm is raging outside.")
            print(" ")
            input("'What was that ?' You ask yourself.")
            Main_entrance ()

        elif userInput == "RIGHTWARD":
            print("You go to the door on your right.")

            input("\033[1;31m\n" + "Something suddenly stabs you in the back as you hit the door, blasting a hole in your chest.")
            print(" ")
            input("'Wh.. at.. !?' You whisper in pain.")
            print(" ")
            input("Your brain can't even process what's happening to you.")
            input("Here sadly ends the story of " + Player_name + "." + "\033[0m")
            quit ()

        elif userInput == "BACKWARD":
            print("You decide to turn around.")
            Vanilla_room_3 ()

        else:
            print("Please enter a valid option.")


    def Crossroad ():

        directions = ["LEFTWARD", "RIGHTWARD", "BACKWARD"]

        print("\033[1;35m\n" + "You have reached a crossroads, each path leading to a different closed door.")
        userInput = input("Where are you heading ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD / BACKWARD " + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are LEFTWARD, RIGHTWARD or BACKWARD." + "\033[0m")
            input("\033[1;35m\n" + "You have reached a crossroads, each path leading to a different closed door.")
            userInput = input("Where are you heading ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD / BACKWARD " + "\033[0m")
            print(" ")

        if userInput == "LEFTWARD":
            print("You head for the left.")

            input("\033[1;31m\n" + "Something suddenly stabs you in the back as you hit the door, blasting a hole in your chest.")
            print(" ")
            input("'Wh.. at.. !?' You whisper in pain.")
            print(" ")
            input("Your brain can't even process what's happening to you.")
            input("Here sadly ends the story of " + Player_name + "." + "\033[0m")
            quit ()

        elif userInput == "RIGHTWARD":
            print("You head for the right.")
            print(" ")

            input("You feel a huge wave of energy wash over you as you unlock the door.")
            input("The world slowly begins to fade as you lose consciousness.")
            input("You find yourself at the front doors when you finally wake up.")
            input("You can no longer exit the building this way since the storm is raging outside.")
            print(" ")
            input("'What was that ?' You ask yourself.")
            Main_entrance ()

        elif userInput == "BACKWARD":
            print("You decide to turn around.")
            Vanilla_room_1 ()

        else:
            print("Please enter a valid option.")


    def Main_entrance():

        directions = ["LEFTWARD", "RIGHTWARD"]

        print("\033[1;35m\n" + "Two corridors now face you.")
        userInput = input("Where are you heading ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are LEFTWARD or RIGHTWARD" + "\033[0m")
            userInput = input("\033[1;35m\n" + "Two corridors now face you, where are you heading ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")
            print(" ")

        if userInput == "LEFTWARD":
            print("You take the corridor on your left.")
            Vanilla_room_2()

        elif userInput == "RIGHTWARD":
            print("You take the corridor on your right.")
            Vanilla_room_1()

        else:
            print("Please enter a valid option.")

    Main_entrance()

Second_chapter()


def Third_chapter ():

    print("\033[1;37m\n" + "checkpoint reached" + "\033[0m")
    print(" ")

Third_chapter()