input("\033[1;36m\n" + "Press the enter button to scroll the text.")
print(" ")

input("!!! WARNINGS !!!")
print(" ")

input("Please be aware that pressing the enter button without entering the recquired answers might result in a crash.")
input("Entering letters instead of numbers may pose problems later, as you progress through the story.")
input("The game is also case-sensitive, which mean that answers should be written in lower or higher cases accordingly." )
input("Finally, there are no saves since I don't know how to code that yet." + "\033[0m")
print(" ")


input("This is an experimental project I made during my free time. Might finish it someday, might not... Who knows.")
input("For now at least I do hope you'll enjoy the adventure.")
print(" ")


input("Before we start, let me ask you a few questions.")

Player_name = input("\033[1;35m\n" + "What is your name ? ")
Name_question = input("\033[1;35m\n" + "Is " + Player_name + " the name you choosed ?" + "\033[1;36m\n" + "[Y]  " + "  [N] ")
Name_answer = Name_question + str("Y")
while Name_question != str("Y"):
    if Name_question != str("Y"):
        if Name_answer != str("Y"):
            Player_name = input("\033[1;35m\n" + "Let me ask you this once again. What is your name ? ")
            Name_question = input("\033[1;35m\n" + "Is " + Player_name + " the name you choosed ?" + "\033[1;36m\n" + "[Y]  " + "  [N] ")
else:
    input("\033[1;37m\n" + "You will be remembered as " + Player_name + ".")


Player_age = input("\033[1;35m\n" + "How old is " + Player_name + " ? ")
Age_question = input("\033[1;35m\n" + "Is " + Player_name + " " + Player_age + " years old ?" + "\033[1;36m\n" + "[Y]  " + "  [N] ")
Age_answer = Age_question + str("Y")
while Age_question != str("Y"):
    if Age_question != str("Y"):
        if Age_answer != str("Y"):
            Player_age = input("\033[1;35m\n" + "Let me ask you this once again. How old is " + Player_name + " ? ")
            Age_question = input("\033[1;35m\n" + "Is " + Player_name + " " + Player_age + " years old ?" + "\033[1;36m\n" + "[Y]  " + "  [N] ")
else:
    input("\033[1;37m\n" + Player_name + " is " + Player_age + " years old." + "\033[0m")

print(" ")


input(Player_name + ". Your adventure is about to start.")
input("Trust your judgement, follow your instinct and have fun !")
print(" ")


input("\033[1;37m\n" + "Press enter to start.")
print("\033[1;37m\n" + "Initializing story, please be patient.")
import time
my_list = ['.', '.', '.', '.', '.']
for i in my_list:
    time.sleep(1)
    print(i)


input("\033[1;33m\n" + "\033[1m" + "Lost in space." + "\033[0m" )
print(" ")



input("You were heading to the moon when your compagny spaceship suddenly got raided by some pirates.")
input("You knew the whole crew was condemned, and so you promptly left with the emergency shuttle unnoticed.")
print(" ")

input("Minutes only after piloting the shuttle, you feel a tremendous impact.")
input("You quickly glance back to where you came from and your eyes fill with dread as you see the mothership exploding and the pirates following you.")
input(" ")