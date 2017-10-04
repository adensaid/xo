""" An unbeatable noughts and crosses AI"""
import sys
import random
# declare global grid
grid = []


def main():
    """Main entry point"""
    displayWelcome()

    # initialise grid
    for i in range(0, 9):
        grid.insert(i, " ")

    displayGrid()

    for i in range(5):
        choice = int(input("Please enter a number 1-9: ")) - 1
        while 0 > choice or 8 < choice or grid[choice] != ' ':
            if 0 > choice or 8 < choice:
                choice = int(input("Number must be between 1-9: ")) - 1
            else:
                choice = int(input("Position taken, try another: ")) - 1
        grid[choice] = 'X'  # user input

        while grid[choice] != ' ' and i != 4:  # while there are places available, try to input something too
            choice = random.randint(0, 8)
        if grid[choice] != 'X':
            grid[choice] = '0'

        displayGrid()


def displayGrid():
    for i in range(0, 9):
        print("| ", grid[i], end='')
        if i in [2, 5, 8]:
            print("|")
    for i in range(15):
        print("-", end='')
    print()


def displayWelcome():
    print("Welcome to XO AI!")
    print("©2017 AF & SA ltd. ")
    print("All rights reserved")

    print()

    print(" | 1 | 2 | 3 |")
    print(" | 4 | 5 | 6 |")
    print(" | 7 | 8 | 9 |")
    print("---------------")


# convert from player number to their respective signs
convert = {
    0: ' ',
    1: 'X',
    2: '0',
}

if __name__ == '__main__':

    sys.exit(main())
