import random
import sys
import os
import time
import Tkinter as tk
import tkFileDialog
os.system("mode con: cols=90 lines=40")

students = {}
num = 0
run = True
hwToBeColl = 0

def fileRead():
    try:
        root = tk.Tk()
        root.withdraw()
        myFile = tkFileDialog.askopenfile(filetypes=[("Text files","*.txt")])
        global num
        for line in myFile:
            num = num + 1
            students[num] = line
        pickRandom()
    except IOError:
        print("Could not open that file...")
        ans = raw_input("Would you like to check for file again? (y/n)")
        if(ans.lower() == "y"):
            return
        elif(ans.lower() == "n"):
            exit()
        else:
            print("Invalid input, running again")
def pickRandom():
    global hwToBeColl, run, num
    if(hwToBeColl >= num):
        print("Collect HW from all students")
    else:
        for x in range(0, hwToBeColl):
            randomnum, student = random.choice(students.items())
            print(str(randomnum) + ". " + students[randomnum])
            del students[randomnum]
    ans = raw_input("\nWould you like to run again? (y/n)")
    if(ans.lower() == "y"):
        return
    else:
        print("Closing...")
        time.sleep(1)
        run = False



def main():
    global run, hwToBeColl
    while(run == True):
        try:
            hwToBeColl = int(raw_input("How many Students homework would you like to collect?"))
        except ValueError:
            print("Must be an integer")
            return
        fileRead()

main()
