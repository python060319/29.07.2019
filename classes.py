
class Car:
    def __init__(self):
        print("Creating a car")
        self.__secret()
    # method
    def drive(self, *args):
        print("driving a car...")
        print(args)
    def washCar(self):
        print("washing my car...")
    def __secret(self):
        print("secret method")

toyota = Car()
mitsubishi = Car()
print(type(toyota))
toyota.drive(3, 4)
#toyota.__secret()


# function
def foo():
    pass


# create MobilePhone class
# in init print("creating a phone")
#   also call factoryRestart
# create methods: ring, powerOn,
#   powerOff
# create secret method: factoryRestart
# create 2 phones

# Class Calculator
# __init__ - print creating
# Sum
# def Sum(self, *args):
#   print sum of args
