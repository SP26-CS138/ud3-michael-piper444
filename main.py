'''
DEVELOPER(S): <Michael Piper>
COLLABORATORS: <anyone who helped you>
DATE: <04/20/2026>
'''

"""
Luiseno flashcard quiz program for language revitalization efforts.

The program quizzes user on several different phrases in Luiseno language
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
    with open("Luiseno.txt", "w") as file:
        file.write("Miyu~Hello\n")
        file.write("Ohoo~Yes\n")
        file.write("Qayno~No\n")

def load_file(Luiseno):
    words = {}

    with open (Luiseno , 'r') as file:
        for line in file:
            line = line.strip()
            luiseno , english = line.split("~")
            words[luiseno] = english
    return words




##########################################
# MAIN PROGRAM:
##########################################
# <replace this line with your main program>
