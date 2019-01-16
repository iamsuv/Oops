

#Motorbike Class

class MotorBike:
    def __init__(self,speed):
        self.speed=speed
    def increase_speed(self,change):
        self.speed +=change
    def decrease_speed(self,change):
        self.speed -=change


Honda=MotorBike(120)
Pulser=MotorBike(180)


print(Honda)
print(Pulser)
print()
print(Honda.speed)
print(Pulser.speed)
print()
Honda.increase_speed(20)
Pulser.increase_speed(30)
print(Honda.speed)
print(Pulser.speed)
print()
Honda.decrease_speed(50)
Pulser.decrease_speed(50)
print(Honda.speed)
print(Pulser.speed)

