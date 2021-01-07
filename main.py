# main.py
# Midnight Rider
# A text-based adventure game
# Gamespot gives it 9 out of 10

import random
import sys
import textwrap
import time


INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER

WE"VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL

THAT'S WHY THE GOVERNMENT WANTS IT.

WE CAN'T LET THEM HAVE IT.

ONE GOAL: SURVIVE... AND THE CAR

REACH THE END BEFORE THE MAN GON GETCHU.

----
"""

CHOICES = """
    ---
    A.
    B.
    C. Speed ahead at full throttle
    D. Stop at gas station
    E. Status Check
    Q. QUIT
    ___
    """


def intro():
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

def main():
    #intro()
    MAX_FUEL_LEVEL = 50

    # Variables
    done = False

    kms_travelled =  0    # 100 km is the end
    agents_distance = -20 # 0 is the end
    turns = 0             #
    tofu = 3              # 3 is max
    fuel = MAX_FUEL_LEVEL # Max is 50 L
    hunger = 0            #


    # MAIN LOOP
    while not done:
        pass
        # TODO: Check if reached END GAME

        # TODO: Present the user their choices
        print(CHOICES)


        user_choice = input("What do you want to do? ").lower().strip(",./<>?!")


        if user_choice == "c":
            pass
            # FAST
            players_distance_now = random.randrange(10,16)
            agents_distance_now = random.randrange(7,15)

            # Burn fuel
            fuel -= random.randrange(5,11)

            # Player distance traveled
            kms_travelled += players_distance_now

            # Agents_distance_now
            agents_distance -= players_distance_now - agents_distance_now

            # Player: kms_travelled + players_distance_now
            # Agents: players_distance_now - agents_distance_now


            # Agents distance traveled
            # Feedback to player
            print()
            print("ZOZOOOOOM")
            print(f"-------- You traveled {players_distance_now} kms--------")

        elif user_choice == "d":
            # Refueling
            # Fill up the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give player feedback
            print()
            print("-------- You filled the fuel tank --------")
            print("-------- The agents got closer --------")
            print()


        elif user_choice == "e":
            print(f"\t-----Status Check-----")
            print(f"\tkm travelled: {kms_travelled}")
            print(f"\tFuel remaining: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind")
            print(f"\tYou have {tofu} tofu left ")
            print("\t-----------------------")


        elif user_choice == "q":
            done = True

        time.sleep(1.5)


        # TODO: Change the environment based on user choice and RNG

        # TODO: Random event generator

    # Outro
    print("Thanks for playing! ")


if __name__ == "__main__":
    main()