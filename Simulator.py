import os
import time
import sys

from Ship import Ship


class Simulator(object):
    """Simulation platform"""

    def __init__(self):

        # Object ship
        self.ship = Ship()

    # Menu of the Simulator
    def menu(self):

        while (True):
            os.system('cls')
            print("Welcome to the airship simulator! Please enter your choice\n\n")
            print("1. Start the simulation\n")
            print("0. Exit")

            # Input from the user
            input_choice = input()

            # Check the input value
            if input_choice == "1":
                self.startSimulation()
            elif input_choice == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Thank you for using airship simulator!")
                os.system('pause')
                exit()
            else:
                raise Exception("Input error, please try again!")

    # Set the required configuration of the simulator
    def setConfiguration(self):
        pass

    # Start the simulation
    def startSimulation(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Simulation started!")
        os.system('pause')
