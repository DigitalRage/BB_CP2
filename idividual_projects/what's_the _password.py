#BB 1st Random Password Generator Project
#Import libraries
import random
#Make main function
def run():
    types = {"Upercase Characters": True, "Lowercase Characters": True, "Numbers": True, "Special Characters": True}
    for i in types:
        while True:
            action = input(f"Will you use {i}? (Y/N)\n>").strip().lower()
            if action == "y": types[i] = True; break
            elif action == "n": types[i] = False; break
            else: print("Try again")
    print(types)
    def char_add(): 
        return
def main(): 
    while True:
        #asks if the user wants to use or exit
        choice = input("1. Generate Passwords\n2. Exit\n>")
        #checks if it is a valid number
        if choice == '1': run()
        elif choice == '2': print("Goodbye!"); break
        else: print("wrong choice. try again")

    #asks the user for amount of characters
    #asks what types of characters to use
    #use ascii values for random password generator
    #put the generated characters in a tuple
    #return the tuple

    #Run main
main()