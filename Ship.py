from Battery import LithiumBattery
from Battery import FuelCell

# Lithium battery capacity(A.h)
MAX_LITHIUMBATTERY_CAPACITY = 10000
# Lithium battery power(W)
MAX_LITHIUMBATTERY_POWER = 10

# Fuel battery capacity(A.h)
MAX_FUELBATTERY_CAPACITY = 50000
# Fuel battery power(W)
MAX_FUELBATTERY_POWER = 20

TOTAL_DEMAND_POWER = 5

# Air density(kg/m3)
P = 1.293
# Preset flight speed(km/h)
V = 10
# Projected area(m2)
A = 0.52
# Coefficient of wind resistance
cd = 0.5


class Ship(object):

    """Ship class"""

    def __init__(self):
        self.lithiumBattery = LithiumBattery(MAX_LITHIUMBATTERY_CAPACITY, MAX_LITHIUMBATTERY_POWER)
        self.fuelBattery = FuelCell(MAX_FUELBATTERY_CAPACITY, MAX_FUELBATTERY_POWER)
        self.airForce = 0.5 * P * pow(V, 2) * A * cd
        self.indicatorG = True

    def updateRealDemandPower(self):
        realDemandPower = min(TOTAL_DEMAND_POWER, (self.lithiumBattery.maxPower + self.fuelBattery.maxPower))
        self.lithiumBattery.realDemandPower = realDemandPower
        self.fuelBattery.realDemandPower = realDemandPower

    def updateBattery(self):
        if self.lithiumBattery.workingStatus == 1:
            if (20 - self.lithiumBattery.socPercent) / 100 * self.lithiumBattery.currentCapacity < self.fuelBattery.currentCapacity:
                self.fuelBattery.currentCapacity -= (20 - self.lithiumBattery.socPercent) / 100 * self.lithiumBattery.currentCapacity
                self.lithiumBattery.currentCapacity = 0.2 * self.lithiumBattery.maxCapacity
                self.lithiumBattery.workingStatus = 2
            else:
                print("Not enough Fuel cell energy.")

        elif self.lithiumBattery.workingStatus == 2:
            if (40 - self.lithiumBattery.socPercent) / 100 * self.lithiumBattery.currentCapacity < self.fuelBattery.currentCapacity:
                self.fuelBattery.currentCapacity -= (40 - self.lithiumBattery.socPercent) / 100 * self.lithiumBattery.currentCapacity
                self.lithiumBattery.currentCapacity = 0.4 * self.lithiumBattery.maxCapacity
                self.lithiumBattery.workingStatus = 3
            else:
                print("Not enough Fuel cell energy.")

        elif self.lithiumBattery.workingStatus == 3:
            if (60 - self.lithiumBattery.socPercent) / 100 * self.lithiumBattery.currentCapacity < self.fuelBattery.currentCapacity:
                self.fuelBattery.currentCapacity -= (60 - self.lithiumBattery.socPercent) / 100 * self.lithiumBattery.currentCapacity
                self.lithiumBattery.currentCapacity = 0.6 * self.lithiumBattery.maxCapacity
                self.lithiumBattery.workingStatus = 4
            else:
                print("Not enough Fuel cell energy.")

        else:
            print("lithium battery is not charging.")
