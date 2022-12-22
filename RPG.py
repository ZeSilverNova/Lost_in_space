input("\033[1;36m\n" + "Press the enter button to scroll the text.")
print(" ")

input("!!! WARNINGS !!!")
print(" ")

input("Please be aware that pressing the enter button without entering the recquired answers might result in a crash.")
input("Entering letters instead of numbers may pose problems later, as you progress through the story.")
input("The game is also case-sensitive, which mean that answers should be written in lower or higher cases accordingly." + "\033[0m")
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
print("\033[1;37m\n" + "Initializing story, please be patient.")
import time
my_list = ['.', '.', '.', '.', '.']
for i in my_list:
    time.sleep(0.5)
    print(i)


input("\033[1;33m\n" + "\033[1m" + "Lost in space." + "\033[0m" )
print(" ")


def First_chapter ():

    input("You were heading to the moon when your compagny spaceship suddenly got raided by some pirates.")
    input("You knew the whole crew was condemned, and so you promptly left with the emergency shuttle unnoticed.")
    print(" ")

    input("Minutes only after piloting the shuttle, you feel a tremendous impact.")
    input("You quickly glance back to where you came from.")
    input("Your eyes fill with dread as you see the mothership exploding into tiny pieces and the pirates following you.")
    print(" ")