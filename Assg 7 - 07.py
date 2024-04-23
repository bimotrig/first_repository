class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value

class RVCar(Car):  # Inherit from Car class
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum

# Example usage
myRV = RVCar()
myRV.seatNum = 8  # Set the number of seats in the RV
print(myRV.getSeatNum())
