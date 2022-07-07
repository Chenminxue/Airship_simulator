class Battery(object):
    """Interface"""

    def __init__(self, maxCapacity, maxPower):
        # Max capacity
        self.maxCapacity = maxCapacity

        # Current capacity
        self.currentCapacity = 0

        # Max power
        self.maxPower = maxPower

        # Current capacity
        self.currentPower = 0

        # Soc Percent
        self.socPercent = 0.0

        # Real demand power
        self.realDemandPower = 0

    # Remaining energy percentage
    def printSocPercent(self):
        print("Remaining energy: {:.2%}".format(self.socPercent / 100))

    def currentPower(self):
        pass


class LithiumBattery(Battery):
    """Lithium Battery class"""

    # Working statues
    workingStatus = 0
    # Charging power from solar and fuel cell battery
    beingChargedPower = 0

    def __init__(self, maxCapacity, maxPower):
        super().__init__(maxCapacity, maxPower)

    @classmethod
    def checkWorkingStatus(cls, socPercent):
        # 0 % ~ 20 %
        if (socPercent >= 0) and (socPercent < 20):
            LithiumBattery.workingStatus = 1
        # 20 % ~ 40 %
        elif (socPercent >= 20) and (socPercent < 40):
            LithiumBattery.workingStatus = 2
        # 40 % ~ 60 %
        elif (socPercent >= 40) and (socPercent < 60):
            LithiumBattery.workingStatus = 3
        # 60 % ~ 80 %
        elif (socPercent >= 60) and (socPercent < 80):
            LithiumBattery.workingStatus = 4
        # 80 % ~ 100 %
        elif (socPercent >= 80) and (socPercent <= 100):
            LithiumBattery.workingStatus = 5

    def checkCurrentPower(self):

        LithiumBattery.checkWorkingStatus(self.socPercent)

        # Less than 20 %, the lithium battery doesn't work
        if LithiumBattery.workingStatus == 1:
            temp = (self.socPercent - 20) / abs(self.socPercent - 20)
            temp = int(temp)
            self.currentPower = max(0, temp) * self.maxPower

        # Between 20 % and 40 %, the lithium battery doesn't work
        elif LithiumBattery.workingStatus == 2:
            temp = (self.socPercent - 40) / abs(self.socPercent - 40)
            temp = int(temp)
            self.currentPower = max(0, temp) * self.maxPower

        # Between 40 % and 60 %, the lithium battery works on demand
        elif LithiumBattery.workingStatus == 3:
            if self.maxPower < self.realDemandPower:
                self.currentPower = self.maxPower
            else:
                self.currentPower = self.realDemandPower

        # Between 60 % and 80 %, the lithium battery works all the time
        elif LithiumBattery.workingStatus == 4:
            self.currentPower = self.maxPower

        # Between 80 % and 100 %, the lithium battery works all the time
        elif LithiumBattery.workingStatus == 5:
            self.currentPower = self.maxPower


class FuelCell(Battery):
    """Fuel cell class"""

    # Current power of the fuel call
    def checkCurrentPower(self, lb_workingStatus):

        if self.maxPower < self.realDemandPower:
            self.currentPower = self.maxPower
        else:
            self.currentPower = self.realDemandPower

        # Less than 20 %, the lithium battery doesn't work
        if lb_workingStatus == 1:
            if self.maxPower < self.realDemandPower:
                LithiumBattery.beingChargedPower = self.maxPower
            else:
                LithiumBattery.beingChargedPower = self.realDemandPower

        # Between 20 % and 40 %, the lithium battery doesn't work
        if lb_workingStatus == 2:
            if self.maxPower < self.realDemandPower:
                LithiumBattery.beingChargedPower = self.maxPower
            else:
                LithiumBattery.beingChargedPower = self.realDemandPower

        # Between 40% and 60%, the lithium battery works on demand
        if lb_workingStatus == 3:
            if self.maxPower < self.realDemandPower:
                LithiumBattery.beingChargedPower = self.maxPower
            else:
                LithiumBattery.beingChargedPower = self.realDemandPower

        # lithium battery remaining power between 60% and 100%, the fuel cell doesn't work
        if lb_workingStatus == 4 or lb_workingStatus == 5:
            LithiumBattery.beingChargedPower = 0
