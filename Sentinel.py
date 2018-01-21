#!/bin/python  

# Files
import TraningSentinelCore

# Standard Libraries
import os
from time import sleep

CLEAR = os.system('clear')

def main():
    CLEAR
    title()
    
    print("1) Network mode\n2) System mode\n3) Exit")

    choice = int(input("What would you like to do?: "))
    
    if choice == 1:
        network_mode()
    elif choice == 2:
        system_mode()
    elif choice == 3:
        print ("Exiting...")
        exit(0)
    else:
        print("Wrong command")
        main()


def network_mode():
    redirect()
    # TODO: For prototype get array of open ports form victim. This will be used for exam.


def system_mode():
    CLEAR
    pathToFile = input("Please specify the path to the file")

    program = 1
    sc = TraningSentinelCore.SentinelCore([1, 5, 5])
    sc.sgd(program, 30, 10, 3.0)

    

def redirect():
    print("Module is not implemented yet\nRedirecting...")
    sleep(1)
    main()



def title():
    """
    This is just the title when the program is run.
    It spells out a big ol' "SENTINEL"
    """
    title_list = [" _______  _______  __    _  _______  ___  __    _  _______  ___     ",
    "|       ||       ||  |  | ||       ||   ||  |  | ||       ||   |    ",
    "|  _____||    ___||   |_| ||_     _||   ||   |_| ||    ___||   |    ",
    "| |_____ |   |___ |       |  |   |  |   ||       ||   |___ |   |    ",
    "|_____  ||    ___||  _    |  |   |  |   ||  _    ||    ___||   |___ ",
    " _____| ||   |___ | | |   |  |   |  |   || | |   ||   |___ |       |",
    "|_______||_______||_|  |__|  |___|  |___||_|  |__||_______||_______|"]

    for l in title_list:
        print(l)
    print("")


main()

