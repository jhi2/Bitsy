####imports####
import webbrowser
import os
####functions####

    
####starter####
nme = input("Hello! What's your name?\n")
print("Hello, %s\nMy name is Bitsy, Your personal PC asistant" %nme)
##### Main loop #####
while True:
    ##### asks what to do#####
    thing = input("What would you like to do, %s\n" %nme)
    ##### splits the input for procesesing #####
    tg2 = thing.lower()
    inst = tg2.split(" ")
    if "open" in inst:
        pth = input("Enter the path of the file you would like to run:\n")
        webbrowser.open(pth)
    if "control panel" in inst:
        os.system("opensettings.bat")