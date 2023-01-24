import random

input("\033[1;37m\n" + "Press the enter button to scroll the text." + "\033[0m")
print(" ")

input("\033[1;36m\n" + "!!! WARNINGS !!!")
print(" ")

input("Please be aware that pressing the enter button without entering the required choices might result in a crash.")
input("The game is also case-sensitive, which mean that your inputs should be written in lower or higher cases accordingly.")
input("Finally, keep in mind that there are no saves for added difficulty.")
input("You will however reach several checkpoints during the game where your life will be restored." + "\033[0m")
print(" ")

input("This is an experimental project I made during my free time. Might finish it someday, might not... Who knows.")
input("For now at least I hope you'll enjoy the adventure.")
print(" ")

input("Before we start, let's quickly make acquaintance.")


Player_name = input("\033[1;35m\n" + "What is your name ? ")
Name_question = input("\033[1;35m\n" + "Is " + Player_name + " the name you chose ?" + "\033[1;36m\n" + "[Y]  " + "  [N] ")
Name_answer = Name_question + str("Y")

while Name_question != str("Y"):
    if Name_question != str("Y"):
        if Name_answer != str("Y"):
            Player_name = input("\033[1;35m\n" + "Let me ask you this once again. What is your name ? ")
            Name_question = input("\033[1;35m\n" + "Is " + Player_name + " the name you chose ?" + "\033[1;36m\n" + "[Y]  " + "  [N] ")
else:
    input("\033[1;37m\n" + "You will be remembered as " + Player_name + "." + "\033[0m")


print(" ")

input("I have no more questions for you " + Player_name + ".")
input("Your new adventure is about to start.")
input("Trust your judgement, follow your instinct and have fun !")
print(" ")

input("\033[1;37m\n" + "Press enter to start.")
print(" ")

Shuttle_life_points = 7

Player_max_health = 19
Player_life_points = 19
Curse = Player_life_points - 1

Monster_life_points = 19
Monster_base_form = 2
Monster_first_form = Monster_base_form + 2
Monster_second_form = Monster_first_form + 2


def First_chapter():

    print("Initializing story, please be patient.")
    import time
    my_list = [".", "   .", "      .", "         .", "            ."]
    for i in my_list:
        time.sleep(0.5)
        print(i)
        print(" ")

    input("\033[1;33m\n" + "\033[1m" + "Lost in space." + "\033[0m")
    print(" ")
    print(" ")

    input("You were heading to the moon when your company spaceship suddenly got raided by some pirates.")
    input("You knew the whole crew was condemned, and so you promptly left with the emergency shuttle unnoticed.")
    print(" ")

    input("Minutes only after piloting the shuttle, you feel a tremendous impact reverberating through the cabin.")
    input("You quickly glance back to where you came from.")
    input("Your eyes fill with dread as you see the mothership exploding into countless tiny pieces and the pirates heading your way.")

    def Sequence_1():

        print("\033[1;37m\n" + "checkpoint reached" + "\033[0m")
        print(" ")

        input("The pirates are still pretty far, but they're getting closer.")
        input("You firmly grip the handlebars, hoping to distance them.")

        global Shuttle_life_points

        Moves = ["UPWARD", "DOWNWARD", "LEFTWARD", "RIGHTWARD"]

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
                print("You are starting to panic." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

            else:
                print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
                print("The pirates are getting closer." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

        print("\033[1;32m\n" + "Your shuttle rotates upward, narrowly avoiding enemy lasers." + "\033[0m")
        print("The pirates are still after you.")

    Sequence_1()

    def Sequence_2():

        global Shuttle_life_points

        Moves = ["UPWARD", "DOWNWARD", "LEFTWARD", "RIGHTWARD"]

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
                print("You are starting to panic." + "\033[0m")
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

    Sequence_2()

    def Sequence_3():

        global Shuttle_life_points

        Moves = ["UPWARD", "DOWNWARD", "LEFTWARD", "RIGHTWARD"]

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
                print("You are starting to panic." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

            else:
                print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
                print("The pirates are getting closer." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

        print("\033[1;32m\n" + "Your shuttle dives down, pushing you further away from the pirates." + "\033[0m")
        print("You still have a long way to go.")

    Sequence_3()

    def Sequence_4():

        global Shuttle_life_points

        Moves = ["UPWARD", "DOWNWARD", "LEFTWARD", "RIGHTWARD"]

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
                print("You are starting to panic." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

            else:
                print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
                print("The pirates are getting closer." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

        print("\033[1;32m\n" + "You continue to dive, dodging enemy fire." + "\033[0m")
        print("You still have a long way to go, but you're doing good.")

    Sequence_4()

    def Sequence_5():

        global Shuttle_life_points

        Moves = ["UPWARD", "DOWNWARD", "LEFTWARD", "RIGHTWARD"]

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
                print("You are starting to panic." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

            else:
                print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
                print("The pirates are getting closer." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

        print("\033[1;32m\n" + "You turn sharply left, after spotting an asteroid belt." + "\033[0m")
        print("You start to wonder how much longer they will hunt you.")

    Sequence_5()

    def Sequence_6():

        global Shuttle_life_points

        Moves = ["UPWARD", "DOWNWARD", "LEFTWARD", "RIGHTWARD"]

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
                print("You are starting to panic." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

            else:
                print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
                print("The pirates are getting closer." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

        print("\033[1;32m\n" + "What looks like a nearby planet catches your eye as you sneak through the asteroid belt." + "\033[0m")
        print("Maybe if you manage to land...")

    Sequence_6()

    def Sequence_7():

        global Shuttle_life_points

        Moves = ["UPWARD", "DOWNWARD", "LEFTWARD", "RIGHTWARD"]

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
                print("You are starting to panic." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

            else:
                print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
                print("The pirates are getting closer." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

        print("\033[1;32m\n" + "You come out of the asteroid belt and head towards the ground." + "\033[0m")
        print("Only one pirate ship remains behind you.")

    Sequence_7()

    def Sequence_8():

        global Shuttle_life_points

        Moves = ["UPWARD", "DOWNWARD", "LEFTWARD", "RIGHTWARD"]

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
                print("You are starting to panic." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

            else:
                print("\033[1;31m\n" + "You feel laser blasts hitting your shuttle.")
                print("The pirates are getting closer." + "\033[0m")
                Move_choice = input("\033[1;35m\n" + "Where are you heading ?" + "\033[1;36m\n" + "UPWARD / DOWNWARD / LEFTWARD / RIGHTWARD " + "\033[0m")
                Shuttle_life_points = Shuttle_life_points - 1

        print(" ")
        input("Sensing sudden danger, you sharply turn to the right.")
        input("A massive salvo of laser fire passes in front of you, barely brushing your shuttle.")

    Sequence_8()


First_chapter()


def Second_chapter():

    print("\033[1;37m\n" + "checkpoint reached" + "\033[0m")
    print(" ")

    input("You somehow end up landing without exploding.")
    input("A quick glance at your shuttle tells you not without surprise that it is now out of service.")
    input("As you survey your surroundings with concern, you notice a huge magnetic storm approaching you.")
    input("Not too far from where you are is what looks like an old military base.")
    input("Not having much choice, you go to this structure.")
    print(" ")

    input("You have an uneasy feeling when you walk through the main entrance.")
    input("It's almost as if something was watching you...")

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
            Crossroad()

        else:
            print("You decide to turn around.")
            Main_entrance()

    def Vanilla_room_2():

        directions = ["FORWARD", "RIGHTWARD", "BACKWARD"]

        userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "FORWARD / RIGHTWARD / BACKWARD " + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are FORWARD, RIGHTWARD or BACKWARD." + "\033[0m")
            userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "FORWARD / RIGHTWARD / BACKWARD " + "\033[0m")
            print(" ")

        if userInput == "FORWARD":
            print("You keep moving forward.")

            input("\033[1;31m\n" + "Something suddenly stabs you in the back as you try to leave the room, blasting a hole in your chest.")
            print(" ")

            input("'Wh.. at.. !?' You whisper in pain.")
            print(" ")

            input("Your brain can't even process what's happening to you.")
            input("Here sadly ends the story of " + Player_name + "." + "\033[0m")
            quit()

        elif userInput == "RIGHTWARD":
            print("You head for the right.")
            Vanilla_room_3()

        else:
            print("You decide to turn around.")
            Main_entrance()

    def Vanilla_room_3():

        directions = ["FORWARD", "LEFTWARD", "BACKWARD"]

        userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "FORWARD / LEFTWARD / BACKWARD " + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are FORWARD, LEFTWARD or BACKWARD." + "\033[0m")
            userInput = input("\033[1;35m\n" + "You entered an empty room, where are you heading ?" + "\033[1;36m\n" + "FORWARD / LEFTWARD / BACKWARD " + "\033[0m")
            print(" ")

        if userInput == "LEFTWARD":
            print("You head for the left.")
            print(" ")

            input("You feel a huge wave of energy wash over you as you try to leave the room.")
            input("The world slowly begins to fade as you lose consciousness.")
            print(" ")

            input("You find yourself at the front doors when you finally wake up.")
            input("You can no longer exit the building this way since the storm is raging outside.")
            print(" ")

            input("'What was that ?' You ask yourself.")
            Main_entrance()

        elif userInput == "FORWARD":
            print("You keep moving forward.")
            Vanilla_room_4()

        else:
            print("You decide to turn around.")
            Vanilla_room_2()

    def Vanilla_room_4():

        directions = ["FORWARD", "LEFTWARD", "RIGHTWARD", "BACKWARD"]

        print("\033[1;35m\n" + "You entered an empty room. There is a closed door on each wall.")
        userInput = input("Where are you heading ?" + "\033[1;36m\n" + "FORWARD / LEFTWARD / RIGHTWARD / BACKWARD " + "\033[0m")
        print(" ")

        while userInput not in directions:
            print("\033[1;37m\n" + "The options are FORWARD, LEFTWARD, RIGHTWARD or BACKWARD." + "\033[0m")
            print(" ")

            print("\033[1;35m\n" + "You entered an empty room. There is a closed door on each wall.")
            userInput = input("Where are you heading ?" + "\033[1;36m\n" + "FORWARD / LEFTWARD / RIGHTWARD / BACKWARD " + "\033[0m")
            print(" ")

        if userInput == "LEFTWARD":
            input("You find stairs leading to the basement.")
            print(" ")

            input("'Where are we going, " + Player_name + " ?' You wonder with doubt.")
            print(" ")
            input("Checking behind you one last time, you decide to go down the stairs.")

        elif userInput == "FORWARD":
            print("You go to the door in front of you.")
            print(" ")

            input("You feel a huge wave of energy wash over you as you try to leave the room.")
            input("The world slowly begins to fade as you lose consciousness.")
            print(" ")

            input("You find yourself at the front doors when you finally wake up.")
            input("You can no longer exit the building this way since the storm is raging outside.")
            print(" ")

            input("'What was that ?' You ask yourself.")
            Main_entrance()

        elif userInput == "RIGHTWARD":
            print("You go to the door on your right.")

            input("\033[1;31m\n" + "Something suddenly stabs you in the back as you hit the door, blasting a hole in your chest.")
            print(" ")

            input("'Wh.. at.. !?' You whisper in pain.")
            print(" ")

            input("Your brain can't even process what's happening to you.")
            input("Here sadly ends the story of " + Player_name + "." + "\033[0m")
            quit()

        else:
            print("You decide to turn around.")
            Vanilla_room_3()

    def Crossroad():

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
            quit()

        elif userInput == "RIGHTWARD":
            print("You head for the right.")
            print(" ")

            input("You feel a huge wave of energy wash over you as you try to leave the room.")
            input("The world slowly begins to fade as you lose consciousness.")
            print(" ")

            input("You find yourself at the front doors when you finally wake up.")
            input("You can no longer exit the building this way since the storm is raging outside.")
            print(" ")

            input("'What was that ?' You ask yourself.")
            Main_entrance()

        else:
            print("You decide to turn around.")
            Vanilla_room_1()

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

        else:
            print("You take the corridor on your right.")
            Vanilla_room_1()

    Main_entrance()


Second_chapter()


def Third_chapter():

    def Sequence_1():

        global Player_life_points
        escape_choices = ["LEFTWARD", "RIGHTWARD"]

        print("\033[1;37m\n" + "checkpoint reached" + "\033[0m")
        print(" ")

        input("Finally arrived at the basements, you quickly look around you.")
        input("A long dimly lit hallway faces you.")
        input("This path does not inspire confidence in you. You however have no choice but to follow it.")
        print(" ")

        input("You decide to leave, but something bothers you.")
        input("You can't help but feel watched.")
        print(" ")

        input("'kkkkkkrrrrrrrrrr...'")
        print(" ")

        input("A winding rustle now reaches your ears.")
        input("A shudder of horror grips you as you take one last look over your shoulder.")
        input("Two pairs of blazing eyes stare intently at you from the top of the stairs.")
        print(" ")

        input("Not giving you time to think about it, you immediately start running down the hall.")
        print(" ")

        input("You hear a dull noise.")
        input("You don't even have to look back to realize that this thing is after you, and it doesn't wish you well.")

        print("\033[1;35m\n" + "Your instincts suddenly warn you of impending danger as you run away.")
        escape_direction = input("Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        while escape_direction not in escape_choices:
            print("\033[1;37m\n" + "The options are LEFTWARD or RIGHTWARD" + "\033[0m")
            escape_direction = input("\033[1;35m\n" + "Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        if escape_direction == "LEFTWARD":
            print("\033[1;32m\n" + "You instantly jump to the left, perfectly dodging a sneak attack from the thing." + "\033[0m")

        elif escape_direction == "RIGHTWARD":
            print("\033[1;31m\n" + "You instantly jump to the right, but are too slow to completely avoid the blow.")
            print("A razor-sharp blade grazes your legs, also confirming your intuition." + "\033[0m")
            Player_life_points = Player_life_points - 1


        print("You straighten up quickly and resume your escape.")

        print("\033[1;35m\n" + "Your instincts suddenly warn you of impending danger as you run away.")
        escape_direction = input("Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        while escape_direction not in escape_choices:
            print("\033[1;37m\n" + "The options are LEFTWARD or RIGHTWARD" + "\033[0m")
            escape_direction = input("\033[1;35m\n" + "Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        if escape_direction == "LEFTWARD":
            print("\033[1;31m\n" + "You instantly jump to the left, but are too slow to completely avoid the blow.")
            print("A razor-sharp blade grazes your arms. This thing clearly wants you dead." + "\033[0m")
            Player_life_points = Player_life_points - 1

        elif escape_direction == "RIGHTWARD":
            print("\033[1;32m\n" + "You instantly jump to the right, perfectly dodging a sneak attack from the thing." + "\033[0m")


        print("You straighten up once more and resume your escape.")

        print("\033[1;35m\n" + "Your instincts suddenly warn you of impending danger as you run away.")
        escape_direction = input("Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        while escape_direction not in escape_choices:
            print("\033[1;37m\n" + "The options are LEFTWARD or RIGHTWARD" + "\033[0m")
            escape_direction = input("\033[1;35m\n" + "Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        if escape_direction == "LEFTWARD":
            print("\033[1;31m\n" + "You instantly jump to the left, but are too slow to completely avoid the blow.")
            print("A razor-sharp blade grazes your chest. Was it aiming for the heart ?" + "\033[0m")
            Player_life_points = Player_life_points - 1

        elif escape_direction == "RIGHTWARD":
            print("\033[1;32m\n" + "You instantly jump to the right, perfectly dodging a sneak attack from the thing." + "\033[0m")


        print("You see a locked door a few steps away.")

        print("\033[1;35m\n" + "Your instincts suddenly warn you of impending danger as you run away.")
        escape_direction = input("Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        while escape_direction not in escape_choices:
            print("\033[1;37m\n" + "The options are LEFTWARD or RIGHTWARD" + "\033[0m")
            escape_direction = input("\033[1;35m\n" + "Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        if escape_direction == "LEFTWARD":
            print("\033[1;32m\n" + "You instantly jump to the left, perfectly dodging a sneak attack from the thing." + "\033[0m")

        elif escape_direction == "RIGHTWARD":
            print("\033[1;31m\n" + "You instantly jump to the right, but are too slow to completely avoid the blow.")
            print("A razor-sharp blade grazes your head, cutting your hair in the process." + "\033[0m")
            Player_life_points = Player_life_points - 1


        print("You start to burn out when you almost get to the door.")

        print("\033[1;35m\n" + "Your instincts suddenly warn you of impending danger as you run away.")
        escape_direction = input("Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        while escape_direction not in escape_choices:
            print("\033[1;37m\n" + "The options are LEFTWARD or RIGHTWARD" + "\033[0m")
            escape_direction = input("\033[1;35m\n" + "Where are you jumping ?" + "\033[1;36m\n" + "LEFTWARD / RIGHTWARD " + "\033[0m")

        if escape_direction == "LEFTWARD":
            print("\033[1;31m\n" + "You instantly jump to the left, but are too slow to completely avoid the blow.")
            print("A razor-sharp blade grazes your hips. You're starting to bleed." + "\033[0m")
            print(" ")
            Player_life_points = Player_life_points - 1

        elif escape_direction == "RIGHTWARD":
            print("\033[1;32m\n" + "You instantly jump to the right, perfectly dodging a sneak attack from the thing." + "\033[0m")
            print(" ")

    Sequence_1()

    def Sequence_2():

        input("Running towards the door, you rush to the other side before slamming it.")
        input("You grab one of the many wooden planks strewn on the ground in order to block it.")
        input("Your relief however quickly fades when you find that this room has no other way out.")
        input("You start looking for potential weapons.")
        print(" ")

        input("A pile of old documents suddenly falls to the ground right in front of your feet.")
        input("You take a quick look at it.")
        input('A highlighted passage catches your eye.')
        input("It says :")
        print(" ")

        input("'Nobody thought experiment thirty-six would survive.")
        input("All it took was one small mistake...'")
        print(" ")

        input("A violent knock at the door tears you away from your reading.")
        input("You frantically resume your search.")
        input("When all hope seemed lost, you suddenly discover a wardrobe locked with a digital padlock.")
        input("You try to guess the combination.")

        Guess_number = "316"
        Guess_chances = 5
        Number_of_guesses = 0

        Gun = False
        Katana = False
        Flamethrower = False
        Wooden_board = True

        def Weapon_choice_section():

            global Gun
            global Katana
            global Flamethrower
            global Wooden_board

            input("You hasten to open the wardrobe.")
            input("Three different weapons were lying inside.")

            Weapon_list = {"THE GUN": False, "THE GLOWING KATANA": False, "THE FLAMETHROWER": False, "Wooden Board": True}
            Weapon_choice = input("\033[1;35m\n" + "Which one are you choosing ?" + "\033[1;36m\n" + "THE GUN / THE GLOWING KATANA / THE FLAMETHROWER " + "\033[0m")
            print(" ")

            while Weapon_choice not in Weapon_list:
                print("\033[1;37m\n" + "Choose one of the selectable weapons." + "\033[0m")
                Weapon_choice = input("\033[1;35m\n" + "Which one are you choosing ?" + "\033[1;36m\n" + "THE GUN / THE GLOWING KATANA / THE FLAMETHROWER " + "\033[0m")
                print(" ")

            if Weapon_choice == "THE GUN":
                input("The doors abruptly give way under the repeated blows of the thing.")
                input("You grab the gun and quickly reload it.")
                input("You however were only able to find 10 bullets in total.")
                print(" ")

                Gun = True
                Katana = False
                Flamethrower = False
                Wooden_board = False

            elif Weapon_choice == "THE GLOWING KATANA":
                input("The doors abruptly give way under the repeated blows of the thing.")
                input("\033[1;31m\n" + "Excruciating pain goes through you as soon as you take the katana out of its sheath." + "\033[0m")
                print(" ")

                input("No longer having the luxury of thinking about it, you grit your teeth and prepare for battle.")
                print(" ")

                Gun = False
                Katana = True
                Flamethrower = False
                Wooden_board = False

            else:
                input("The doors abruptly give way under the repeated blows of the thing.")
                input("You proudly brandish the flamethrower towards the creature.")
                input("You however notice that the tank is almost empty.")
                print(" ")

                Gun = False
                Katana = False
                Flamethrower = True
                Wooden_board = False


        Player_guess = input("\033[1;35m\n" + "The padlock appears to have a three digit combination. " + "\033[0m")

        while Number_of_guesses < Guess_chances and Player_guess != Guess_number:
            if Number_of_guesses < Guess_chances:
                if Player_guess != Guess_number:
                    print("\033[1;31m\n" + "You hear another violent slam at the door.")
                    print("They probably won't last much longer." + "\033[0m")
                    Player_guess = input("\033[1;35m\n" + "The padlock appears to have a three digit combination. " + "\033[0m")
                    Number_of_guesses = Number_of_guesses + 1

        if Player_guess == Guess_number:
            input("\033[1;32m\n" + "Your eyes widen with relief as the padlock gives way under your fingers." + "\033[0m")
            print(" ")
            Weapon_choice_section()

        else:
            print(" ")
            input("The doors abruptly give way under the repeated blows of the thing.")
            input("Having found no weapons in the room, you pick up one of the many planks of wood that litter the floor.")
            print(" ")

    Sequence_2()

    def Sequence_3():

        def Fight_sequence():

            global Player_life_points
            global Curse

            global Monster_life_points
            global Monster_base_form
            global Monster_first_form
            global Monster_second_form

            global Gun
            global Katana
            global Flamethrower
            global Wooden_board

            input("While letting out a shrill cry, the creature rushes at you.")
            print(" ")

            Player_options = ["FIGHT", "DODGE"]
            Max_wooden_board_uses = 6
            Wooden_board_count = 0

            Player_choice = input("\033[1;35m\n" + "You have to think fast ! " + "\033[1;36m\n" + "FIGHT / DODGE " + "\033[0m")

            while Player_choice not in Player_options:
                print("\033[1;37m\n" + "The options are FIGHT or DODGE" + "\033[0m")

                Player_choice = input("\033[1;35m\n" + "You have to think fast ! " + "\033[1;36m\n" + "FIGHT / DODGE " + "\033[0m")

            if Player_choice == ["FIGHT"]:
                while Player_life_points > 0 and Monster_life_points > 0:
                    if Monster_life_points > 10:

                        if Gun:
                            input("You deal X damage to monster.")
                            input("Monster deal X damage to you.")

                        elif Katana:
                            input("You deal X damage to monster.")
                            input("You take X curse damage.")
                            input("Monster deal X damage to you.")

                        elif Flamethrower:
                            input("You deal X damage to monster.")
                            input("Monster take X burn damage.")
                            input("Monster deal X damage to you.")

                        elif Wooden_board:

                            if Wooden_board_count < Max_wooden_board_uses:
                                input("You deal X damage to monster.")
                                input("Monster deal X damage to you.")
                                input("Your wooden board break, you pick up another one.")

                                Wooden_board_count + 1

                            elif Wooden_board_count == Max_wooden_board_uses:
                                input("You go bare hands.")
                                input("You deal X damage to monster.")
                                input("You take X backfire damage.")
                                input("Monster deal X damage to you.")

                    elif Monster_life_points > 5 and Monster_life_points <= 10:

                        if Gun:
                            input("You deal X damage to monster.")
                            input("Monster deal X damage to you.")

                        elif Katana:
                            input("You deal X damage to monster.")
                            input("You take X curse damage.")
                            input("Monster deal X damage to you.")

                        elif Flamethrower:
                            input("You deal X damage to monster.")
                            input("Monster take X burn damage.")
                            input("Monster deal X damage to you.")

                        elif Wooden_board:

                            if Wooden_board_count < Max_wooden_board_uses:
                                input("You deal X damage to monster.")
                                input("Monster deal X damage to you.")
                                input("Your wooden board break, you pick up another one.")

                                Wooden_board_count + 1

                            elif Wooden_board_count == Max_wooden_board_uses:
                                input("You deal X damage to monster.")
                                input("You take X backfire damage.")
                                input("Monster deal X damage to you.")

                    elif Monster_life_points <= 5:

                        if Gun:
                            input("Monster deal X damage to you.")
                            input("You deal X damage to monster.")

                        elif Katana:
                            input("Monster deal X damage to you.")
                            input("You deal X damage to monster.")
                            input("You take X curse damage.")

                        elif Flamethrower:
                            input("Monster deal X damage to you.")
                            input("You deal X damage to monster.")
                            input("Monster take X burn damage.")

                        elif Wooden_board:

                            if Wooden_board_count < Max_wooden_board_uses:
                                input("Monster deal X damage to you.")
                                input("You deal X damage to monster.")
                                input("Your wooden board break, you pick up another one.")

                                Wooden_board_count + 1

                            elif Wooden_board_count == Max_wooden_board_uses:
                                input("Monster deal X damage to you.")
                                input("You deal X damage to monster.")
                                input("You take X backfire damage.")

            else:

                Dodge_result = random.choice(["succeed", "fail"])
                if Dodge_result == "succeed":
                    return True
                else:
                    return False

                while Player_life_points > 0 and Monster_life_points > 0:
                    if Monster_life_points > 10:
                        if Dodge_result:
                            continue

                        else:
                            input("You took X damage.")

                    elif Monster_life_points > 5 and Monster_life_points <= 10:

                        if Dodge_result:
                            continue

                        else:
                            input("You took X damage.")

                    elif Monster_life_points <= 5:

                        if Dodge_result:
                            continue

                        else:
                            input("You took X damage.")

            if Player_life_points == 0:

                input("\033[1;31m\n" + "Throwing your weapons away, the creature violently propels you against the ground.")
                input("You hear a dull crack, immediately followed by immeasurable pain.")
                input("The faces of your children suddenly come to mind as its jaws close in on your ribs.")
                print(" ")

                input("'Ci.. a.. h..'.")
                print(" ")

                input("A tear rolls down your cheek as even the pain fades.")
                print(" ")

                input("Here sadly ends the story of " + Player_name + "." + "\033[0m")
                quit()

            elif Monster_life_points == 0:

                input("\033[1;32m\n" + "A deep relief grips you as the creature breathes its last." + "\033[0m")
                print(" ")
                
        def Third_choice():

            Crucial_options = ["FIGHT", "WAIT"]

            Crucial_choice = input("\033[1;35m\n" + "What are you going to do ? " + "\033[1;36m\n" + "FIGHT / WAIT " + "\033[0m")

            while Crucial_choice not in Crucial_options:
                print("\033[1;37m\n" + "The options are FIGHT or WAIT" + "\033[0m")

                Crucial_choice = input("\033[1;35m\n" + "What are you going to do ? " + "\033[1;36m\n" + "FIGHT / WAIT " + "\033[0m")

            if Crucial_choice == "FIGHT":
                print(" ")
                input("Somehow freeing yourself from your uncomfortable position, you swiftly pick up your weapons and face the creature.")
                Fight_sequence()

            else:
                print(" ")
                input("A long silence ends up settling between you.")
                input("You don't dare blink anymore.")
                input("The sounds of your heartbeat become deafening.")
                input("You're almost losing track of time...")

                input("\033[1;32m\n" + "Realizing you mean it no harm, the creature eventually slowly backtracks." + "\033[0m")

        def Second_choice():

            global Player_life_points
            Crucial_options = ["FIGHT", "WAIT"]

            Crucial_choice = input("\033[1;35m\n" + "What are you going to do ? " + "\033[1;36m\n" + "FIGHT / WAIT " + "\033[0m")

            while Crucial_choice not in Crucial_options:
                print("\033[1;37m\n" + "The options are FIGHT or WAIT" + "\033[0m")

                Crucial_choice = input("\033[1;35m\n" + "What are you going to do ? " + "\033[1;36m\n" + "FIGHT / WAIT " + "\033[0m")

            if Crucial_choice == "FIGHT":
                print(" ")
                input("You angrily shout at the creature.")
                Fight_sequence()

            else:
                input("\033[1;31m\n" + "Suddenly jumping in your direction, the creature crashes hard into you, knocking you to the ground." + "\033[0m")
                print(" ")

                input("Slipping from your hands, your weapons fall steps away from you.")
                input("A dull ache makes you briefly close your eyes.")
                input("The creature's face slowly approaches yours.")
                input("You feel its gaze inspecting you intently.")

                Player_life_points = Player_life_points - 5
                Third_choice()

        def First_choice():

            global Player_life_points
            Crucial_options = ["FIGHT", "WAIT"]


            input("Only now that you are facing the creature do you realize how in trouble you are.")
            input("Pushing back the rubble of the door, it stares intently at you with his four burning eyes.")
            input("Smoke comes out of its mouth and an acrid stench reaches your nostrils.")
            input("A gaping wound in its chest catches your attention.")

            Crucial_choice = input("\033[1;35m\n" + "What are you going to do ? " + "\033[1;36m\n" + "FIGHT / WAIT " + "\033[0m")

            while Crucial_choice not in Crucial_options:
                print("\033[1;37m\n" + "The options are FIGHT or WAIT" + "\033[0m")

                Crucial_choice = input("\033[1;35m\n" + "What are you going to do ? " + "\033[1;36m\n" + "FIGHT / WAIT " + "\033[0m")

            if Crucial_choice == "FIGHT":
                print(" ")
                input("You angrily shout at the creature.")
                Fight_sequence()

            else:
                input("\033[1;31m\n" + "The creature violently throws something in your direction, stabbing your right thigh." + "\033[0m")
                print(" ")

                input("Clenching your teeth in pain, you can only watch your blood slowly dripping onto the floor.")
                input("You realize in horror that you have been struck by what looks like a sharp human bone.")
                input("Perhaps it belonged to the former inhabitants of these places ?")

                Player_life_points = Player_life_points - 5
                Second_choice()

        First_choice()

    Sequence_3()


Third_chapter()


def Fourth_chapter():

    input("Collapsing to the ground, you curl into yourself to calm your nerves.")
    input("Your wounds itch, but you have nothing at hand to heal them.")
    input("Stress and exhaustion suddenly overwhelm you.")
    input("Your eyes slowly close.")
    print(" ")

    input("'And now " + Player_name + ",' you whisper softly, 'what do we do ?'")
    print(" ")

    input("Left bruised, scared and hungry, you are suddenly gripped by despair as those three words endlessly echoes in your mind.")
    print(" ")

    input("You are lost.")
    print(" ")

    input("You are lost in the vastness of the universe.")
    print(" ")

    input("You are lost in space.")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

    input("To be continued...")
    quit()


Fourth_chapter()
