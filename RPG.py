input("\033[1;37m\n" + "Press the enter button to scroll the text." + "\033[0m")
print(" ")

input("\033[1;36m\n" + "!!! WARNINGS !!!")
print(" ")

input("Please be aware that pressing the enter button without entering the recquired answers might result in a crash.")
input("Entering letters instead of numbers may pose problems later, as you progress through the story.")
input("The game is also case-sensitive, which mean that answers should be written in lower or higher cases accordingly.")
input("Finally, keep in mind that there are no saves since I don't know how to code that yet.")
input("You will however reach several checkpoints where your life will be restored." + "\033[0m")
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


    Restart_options = str("Y"), str("N")
    Moves = str("UPWARD") , str("DOWNWARD") , str("LEFTWARD") , str("RIGHTWARD" )
    Shuttle_life_points = 10

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

        elif Shuttle_life_points <= 1:
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

First_chapter()