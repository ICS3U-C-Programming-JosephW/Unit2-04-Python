#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 6, 2025
"""
This program asks the user for the radius of a circle in cm.
It then calculates and displays the area and circumference (perimeter) using pi.
"""
import math


# Main function to do all of the area and circumference calculations.
def main():
    # Set pi.
    PI = math.pi

    # Get the radius from the user.
    radius = float(input("Enter the radius of the circle in (cm): "))

    # Calculate the area.
    area = PI * (radius**2)

    # Calculate the circumference.
    circumference = 2 * PI * radius

    # Display the area.
    print(f"\nArea = {area:.2f} cm^2")

    # Display the circumference.
    print(f"Circumference = {circumference:.2f} cm")


if __name__ == "__main__":
    main()
