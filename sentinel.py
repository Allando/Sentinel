#!/bin/python  

import SentinelCore


def main():
    title()
    
    print("1) Attack Mode\n2) Training Mode\n3) Exit")
    

    choice = int(input("What would you like to do?: "))
    
    if choice == 1: attack_mode()
    elif choice == 2: training_mode()
    elif choice == 3:
        print ("Exiting...")
        exit(0)
    else:
        print("Wrong command")


def attack_mode():
    print("attack module is not implementet yet")
    main()


def training_mode():
    print("training module is not implementet yet")
    main()


"""
This is just the title when the program is run.
It spells out a big ol' "SENTINEL"
"""
def title():
    titleList = [" _______  _______  __    _  _______  ___  __    _  _______  ___     ",
    "|       ||       ||  |  | ||       ||   ||  |  | ||       ||   |    ",
    "|  _____||    ___||   |_| ||_     _||   ||   |_| ||    ___||   |    ",
    "| |_____ |   |___ |       |  |   |  |   ||       ||   |___ |   |    ",
    "|_____  ||    ___||  _    |  |   |  |   ||  _    ||    ___||   |___ ",
    " _____| ||   |___ | | |   |  |   |  |   || | |   ||   |___ |       |",
    "|_______||_______||_|  |__|  |___|  |___||_|  |__||_______||_______|"]

    for l in titleList:
        print(l)
    print("")
main()

