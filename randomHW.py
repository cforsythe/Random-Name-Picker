import random
import sys
import os
import time
import Tkinter as tk
import tkFileDialog
os.system("mode con: cols=90 lines=40")

students = {} ##dict of all students
num = 0 ##number of students
run = True ##state of program
hwToBeColl = 0 ##how many HW need to be collected

def fileRead():
    try:
        root = tk.Tk() ##tkinter window
        root.withdraw() ##removes tkinter window that comes along with filedialog
        myFile = tkFileDialog.askopenfile(filetypes=[("Text files","*.txt")]) ##filedialog window for user to select txt file
        global num ##uses global num
        for line in myFile: ##checks every line in file
            num = num + 1 ##increments number of students
            students[num] = line ##writes student number and name into a text file
        pickRandom()
    except IOError:
        print("Could not open that file...") ##if it cant open file
        ans = raw_input("Would you like to check for file again? (y/n)") ##determines if user wants to try and pick a text file again
        if(ans.lower() == "y"): ##if user types yes it runs the program again
            return
        elif(ans.lower() == "n"): ##if user types no exits program
            exit()
        else:   ##if user enters something besides y/n
            print("Invalid input, running again")
def pickRandom(): ##picks random student and prints name, number
    global hwToBeColl, run, num ##simply using global vars
    if(hwToBeColl >= num): ##if trying to pick = or greater than amount of students in class
        print("Collect HW from all students")
    else:
        for x in range(0, hwToBeColl): ##does this for the amount of students that need to be picked
            randomnum, student = random.choice(students.items()) ##randomly picks a student from the dict and inserts key, value into randomnum, student
            print(str(randomnum) + ". " + students[randomnum]) ##Prints the number and name of student in dict
            del students[randomnum] ##deletes student and num from dict so it cant be picked twice
    ans = raw_input("\nWould you like to run again? (y/n)") ##determines if user needs to run again
    if(ans.lower() == "y"): ##runs the while loop all over again
        return
    else: ##if the user doesnt type y the program ends
        print("Closing...")
        time.sleep(1)
        run = False



def main():
    global run, hwToBeColl
    while(run == True): ##infinite loop unless user specifies they are done
        try:  ##this just makes sure the input is an integer otherwise makes user enter number again
            hwToBeColl = int(raw_input("How many Students homework would you like to collect?")) ##input from user
        except ValueError: ##triggers if input is not a number
            print("Must be an integer")
            return
        fileRead()

main()
