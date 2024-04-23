class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):  # Add 'self' argument
        self.speed += value  # Modify object's speed attribute

# Example usage
myCar = Car()
myCar.upSpeed(10)
print(myCar.speed)