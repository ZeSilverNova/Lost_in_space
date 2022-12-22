input("\033[1;36m\n" + "Press the enter button to scroll the text.")
print(" ")

input("WARNINGS !!!")
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


input(Player_name + ". You are about to start a brand new adventure.")
input("Be honest with your answers, trust your instincts and have fun !")
print(" ")


input("\033[1;37m\n" + "Press enter to start.")


input("\033[1;33m\n" + "\033[1m" + "A code from which you are the hero." + "\033[0m")
print(" ")

