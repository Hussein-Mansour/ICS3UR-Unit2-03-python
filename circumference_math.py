#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Tue/Apr27/2021
# This program calculates the circumference of a circle using τ


import constants


def main():
    # input:
    print("We will be calculating the circumference of a circle:")
    radius_of_circle = int(input("Enter the radius of a circle (mm):"))
    # process:
    circumference = constants.TAU * radius_of_circle
    # output:
    print("circumference is {:,.2f} mm.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
