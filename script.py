import os

# 1. Set up the map size and starting position of the cursor (@)
WIDTH = 20
HEIGHT = 10
player_x = 17
player_y = 5

while True:
    # 2. Clear the terminal screen so it looks like an animation
    # 'nt' is for Windows, 'posix' is for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

    # 3. Draw the ASCII map
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                row += "@"  # Draw the player/cursor
            else:
                row += "."  # Draw the empty map space
        print(row)

    print("\nUse WASD to move (Press Enter after key). Type 'e' to interact.")

    # 4. Get input from the user
    move = input("Move: ").lower()

    # 5. Update coordinates based on input
    if move == 'w' and player_y > 0:
        player_y -= 1  # Move Up
    elif move == 's' and player_y < HEIGHT - 1:
        player_y += 1  # Move Down
    elif move == 'a' and player_x > 0:
        player_x -= 1  # Move Left
    elif move == 'd' and player_x < WIDTH - 1:
        player_x += 1  # Move Right
    elif move == 'e':
        print("entering chat!:  ")
        break  # Exit the loop






import sys
import time


def circular_loading(duration_seconds=5):
    spinner = ["◐", "◓", "◑", "◒"]

    end_time = time.time() + duration_seconds
    i = 0

    print("Loading conversation... ", end="")

    while time.time() < end_time:
        sys.stdout.write(f"\rLoading conversation... {spinner[i % len(spinner)]}")
        sys.stdout.flush()

        i += 1
        time.sleep(0.15)  # Controls the speed of the spin

    sys.stdout.write("\r" + " " * 35 + "\r")
    sys.stdout.flush()


# --- Run the animation ---
circular_loading(5)

# --- Your Conversation Loop Starts Here ---
print(r"""

               .-----.
             /         \          ~~
                                  ~~
            |  (o) (o)  |        [  ]
            \   __     /        / __\
            )=======/          (     )
             (=======/        / \___/
             |       |        //  //
              |_____|      //////
             //////////\___//////
     ( )    ////////////\///////
     (((   /////////////////////
     (((((//|  0  \|/ O |

           |    .---.    |
          /    /     \    \

         |    |   @   |    |
         |     \_____/     |
          \               /
           '-------------+

              |       |
              |   |   |
              |   |   |
              |   |   |
              |___|___|
              (___)(___)
""")
print("NPC: Hello traveler! What brings you to these lands?")

protag = input("type in [wish] to browse through items: ")

while protag != "wish":
    print("type [wish] to browse through items")
    protag = input("type in [wish] to browse through items: ")

else:
    print(" pick between the three")

item_1 = input("x")
item_2 = input("y")
item_3 = input("z")

