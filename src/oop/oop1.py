# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base/parent class of all vehicles
class Vehicle:
        pass

# child of Vehicle class
class FlightVehicle(Vehicle):
    pass

#child of  FlightVehicle class
class Starship(FlightVehicle):
    pass

# child of FlightVehicle
class Airplane(FlightVehicle):
    pass

#child of Vehicle class
class GroundVehicle(Vehicle):
    pass

#child of Ground Vehicle
class Car(GroundVehicle):
    pass

#child of Ground Vehicle
class Motorcycle(GroundVehicle):
    pass