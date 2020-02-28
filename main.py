from AI import Player
import time

def main():
    bob = Player()
    bob.take_turn()
    done = input("Press enter when done")
    if done == "":
        quit()



if __name__ == "__main__":
    main()