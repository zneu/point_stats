# Takes coordinates of multiple points from user and calculates the total Euclidean distance between subsequent pairs of points (i.e., line segments). The use story is as follows:
# The user specifies the number of points she wants to input (e.g., 3).
# Sequentially, for each point, the user enters its coordinates, for example, (x1, y1), (x2, y2), (x3, y3) or x1, y1, x2, y2, x3, y3.
# The code calculates the distance from point Pk to the consecutive point Pk+1 (e.g., from point P1 to point P2, from P2 to P3; see figure 1).
# The total distance (Total_d) is derived by summing up the lengths of the individual line segments (e.g., Total_d = dP1P2 + dP2P3).
# The total distance is displayed to the user in a descriptive manner.
# Code works for any number of points (e.g., 0, 1, 10, 100+).
import os
import math

def clear_screen():
    """Clears screen using os functions"""
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    """Shows user help"""
    clear_screen()
    welcome_message = "Welcome to distance tracker, \nGive me coordinates and I will return\nthe distance between all of them."
    print("-"*40)
    print(welcome_message)
    print("-"*40)

def num_coord():
    """Returns a number"""
    while True:
        print("How many coordinates would you like me to analyze, (Q) to quit?")
        user_input = input("> ").lower()
        if user_input == "q":
            clear_screen()
            print("thanks for tyring!")
            quit()
        else:
            try:
                num_coord = int(user_input)
                return num_coord
            except ValueError:
                clear_screen()
                error_input = input("Oops, that was not a number! Who taught you algebra?\nTry again? Y/n\n> ").lower()
                if error_input == "n":
                    clear_screen()
                    print("Thanks for trying!")
                    quit()
                else:
                    clear_screen()
                    print("Trying again...")

def get_coord(num_coord):
    """Returns a list of coordinates, input by the user,
    in form [(X1, Y1), ..., (Xn, Yn)]"""
    count = num_coord
    coord_list = []
    if num_coord == 0:
        print("The distance is 0!")
        quit()
    elif num_coord == 1:
        print("The distance is 0!")
        quit()
    else:
        while count > 0:
            clear_screen()
            print("Please enter x and y\nYou have {} coordinates left to enter".format(count))
            try:
              x = float(input("x > "))
              y = float(input("y > "))
              coord_list.append((x, y))
              count -= 1
              clear_screen()
            except ValueError:
              print("That's not a valid number!")
        return coord_list

def euc_dist(number, coords):
    """Returns the euc_distance of coordinate list"""
    point1 = 0
    point2 = 1
    euc_dict_list = []
    number -= 1
    while number > 0:
        distX = math.pow(coords[point1][0] - coords[point2][0], 2)
        distY = math.pow(coords[point1][1] - coords[point2][1], 2)
        euc_dict_list.append(math.sqrt(distX + distY))
        point1 += 1
        point2 += 1
        number -= 1
    return sum(euc_dict_list)

def display_coordinates(num_coord, coords, euc_dist):
    """Displays information in a neat manner"""
    clear_screen()
    print("You entered {} coordinates".format(num_coord))
    for num, coord in enumerate(coords):
        print("Point {} : {}".format(num, coord))
    print("The distance to travel between those points was: {}".format(euc_dist))

show_help()
number = num_coord()
coords = get_coord(number)
distance = euc_dist(number, coords)
display_coordinates(number, coords, distance)
