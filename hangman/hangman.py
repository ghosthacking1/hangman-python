import random
import os
import math
print("made by:")
print(""" ______  _______ _______ _     _      _______ _     _  _____  _______ _     _ _______ _______
 |     | |______ |______ |____/       |______ |_____| |     | |       |_____| |_____|    |  
 |_____| |       |______ |    \_      ______| |     | |_____| |_____  |     | |     |    |   """)
path = str(os.getcwd())
cwd = open(path + "\\categories.txt")
print("""what category would you like to play?
%s""" % cwd.read())
category = input()
errors = 0
found = []
try:
    line = (random.choice(open(path + "\\" + category + ".txt").readlines()))
    for character in line:
        if character==" ": found.append("-")
        elif character != "\n": found.append("_")
    while(any("_" in s for s in found) and (errors < 7)):
        print(found)
        answer = input()

        current = line.find(answer) 
        if current != -1:
            while (current != -1):
                found[current] = answer
                current = line.find(answer, current+1)
        else:
            errors += 1
            print(answer + " is not correct and you have " + str(7 - errors) + " more tries")
            if errors==1:
                print("x--------x"
                )
            if errors==2:
                print("""|x--------x
|         
|
|
|""")  
            if errors==3:
                print("""|x--------x
|         |
|
|
|""")
            if errors==4:
                print("""|x--------x
|         |
|         0
|
|""")
            if errors==5:
                print("""|x--------x
|         |
|         0
|        /|\\
|
|""")
            if errors==6:
                print("""|x--------x
|         |
|         0
|        /|\\
|         \\
|""")
            if errors==7:
                print("""|x--------x
|         |
|         0
|        /|\\
|        / \\
|""")

    if errors >= 3:
        print("you lost")
    else:
        print("you won with " + str(errors) + " errors")
except:
    print("category " + category + " not found")
