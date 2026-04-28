'''
DEVELOPER(S): <Michael Piper>
COLLABORATORS: <anyone who helped you>
DATE: <04/20/2026>
'''

"""
Luiseno word list program

The program shows users a list of Luiseno words and their corresponding English equivalent.
"""

##########################################
# IMPORTS:
##########################################
import random


##########################################
# FUNCTIONS:
##########################################
# <replace this line with function definitions, each needs a description>
def create_file():
    ''''Creates file with english and luiseno vocab'''
    with open("Luiseno.txt", "w") as file:
        file.write("Miyu~Hello\n")
        file.write("Ohoo~Yes\n")
        file.write("Qayno~No\n")

def load_file(Luiseno):
    words = {}
    '''loads luiseno and english voacb into dictionary'''
    with open (Luiseno , 'r') as file:
        for line in file:
            line = line.strip()
            luiseno , english = line.split("~")
            words[luiseno] = english
    return words


#dictionary was chosen for the key-value relationship between english and luiseno words

##########################################
# MAIN PROGRAM:
##########################################
# <replace this line with your main program>
def main():
    file_name = "Luiseno.txt"
    create_file()
    load_file(file_name)
    while True:
        print("Welcome to menu: ")
        print("1. See words")
        print("2. Exit")

        user_input = input("Please enter your choice")
        if user_input == "1" or user_input.startswith("t"):
            words = load_file(file_name)
            for luiseno, english in words.items():
                print(luiseno, "=", english)
        elif user_input.startswith("2") or user_input.startswith("e"):
            print("Thanks for checking out the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()


            