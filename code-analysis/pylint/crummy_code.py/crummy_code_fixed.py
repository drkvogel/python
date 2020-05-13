""" This module is for learning pylint """

import sys
# from sys import platform

class CarClass:
    """ This class represents a car """

    def __init__(self, color, make, model, year):
        """Constructor"""
        self.color = color
        self.make = make
        self.model = model
        self.year = year
        self.weight = "2000 lbs"

        if "Windows" in sys.platform:
            print("You're using Windows!")

        # self.weight = self.getWeight(1, 2, 3)
        self.weight = self.get_weight()

    def get_weight(self):
        """ Return the car's weight """
        # return "2000 lbs"
        return self.weight

    def get_color(self):
        """ return colour """
        return self.color
