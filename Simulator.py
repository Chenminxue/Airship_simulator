import os
import time
from Ship import Ship


class Simulator(object):
    """Simulation platform"""

    def __init__(self):

        # Object ship
        self.ship = Ship()
        self.realDemandPower = 0

    # Showing the input error info
    @staticmethod
    def inputErrorInfo():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Input error! Please try again!")
        os.system('pause')
        os.system('cls' if os.name == 'nt' else 'clear')

    # Menu of the Simulator
    def menu(self):

        while True:
            print("Welcome to the airship simulator! Please enter your choice\n\n")
            print("1. Start the simulation\n")
            print("0. Exit")

            # Input from the user
            input_choice = input()

            # Check the input value
            if input_choice == "1":
                self.setConfiguration()
                self.startSimulation()
            elif input_choice == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Thank you for using airship simulator!")
                os.system('pause')
                exit()
            else:
                Simulator.inputErrorInfo()

    # Set the required configuration of the simulator
    def setConfiguration(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please set the configuration of the system")
        os.system('pause')
        os.system('cls' if os.name == 'nt' else 'clear')

        # Soc percent of the lithium battery
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Initial power of the LITHIUM BATTERY. Please enter the percentage of max capacity(0 - 100)...")

            init_lb_SocPercent = input()

            if init_lb_SocPercent == "":
                Simulator.inputErrorInfo()
                continue

            init_lb_SocPercent = float(init_lb_SocPercent)

            if 100 >= init_lb_SocPercent >= 0:
                self.ship.lithiumBattery.currentCapacity = self.ship.lithiumBattery.maxCapacity * init_lb_SocPercent / 100
                self.ship.lithiumBattery.socPercent = init_lb_SocPercent
                os.system("pause")
                break
            else:
                Simulator.inputErrorInfo()

        # Soc percent of the Fuel battery
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Initial power of the FUEL BATTERY. Please enter the percentage of max capacity(0 - 100)...")

            init_fc_SocPercent = input()

            if init_fc_SocPercent == "":
                Simulator.inputErrorInfo()
                continue

            init_fc_SocPercent = float(init_fc_SocPercent)
            if 100 >= init_fc_SocPercent >= 0:
                self.ship.fuelBattery.currentCapacity = self.ship.fuelBattery.maxCapacity * init_fc_SocPercent / 100
                self.ship.fuelBattery.socPercent = init_fc_SocPercent
                os.system("pause")
                break
            else:
                Simulator.inputErrorInfo()

        # Real demand power
        self.ship.updateRealDemandPower()

    # Start the simulation
    def startSimulation(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Simulation started!")
        os.system('pause')
        os.system('cls' if os.name == 'nt' else 'clear')

        self.ship.lithiumBattery.checkCurrentPower()
        self.ship.fuelBattery.checkCurrentPower(self.ship.lithiumBattery.workingStatus)
        self.update()

    def update(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.ship.updateBattery()
            self.ship.fuelBattery.checkCurrentPower(self.ship.lithiumBattery.workingStatus)
            time.sleep(1)
            if self.ship.lithiumBattery.workingStatus == 5:
                break
