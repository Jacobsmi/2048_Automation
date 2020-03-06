from AI import Player
import time

def main():
    bob = Player()
    while(True):
        time.sleep(0.5)
        bob.take_turn()



if __name__ == "__main__":
    main()