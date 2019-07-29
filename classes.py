
class Car:
    def __init__(self):
        print("Creating a car")
        self.__secret()
    # method
    def drive(self):
        print("driving a car...")
    def washCar(self):
        print("washing my car...")
    def __secret(self):
        print("secret method")

toyota = Car()
mitsubishi = Car()
print(type(toyota))
toyota.drive()
toyota.__secret()


# function
def foo():
    pass


# create MobilePhone class
# in init print("creating a phone")
# create methods: ring, powerOn,
#   powerOff
# create secret method: factoryRestart
# create 2 phones
