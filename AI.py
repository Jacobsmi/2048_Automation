from game import Driver
from array import *
from copy import deepcopy
import random

class Player:
    # Constructor
    def __init__(self):
        super().__init__()
        # AI creates a new game object with the default constructor
        self.game = Driver() 
    

    # This simulates the AI making one keystroke(taking one turn)
    def take_turn(self):
        # First gets the tiles from the game in an raw format
        board_info = self.game.get_tiles()
        # Next parse the board_info so the program can understand how the board looks
        board_array = self.process_board(board_info)
        # Once input has been parsed and board has been created then moves must be simulated and scored
        best_move = self.simulate_moves(board_array)
        # Once best move has been determined make iscoret
        self.game.make_move(best_move)


    # Method takes unprocessed board info and creates a layout of the game that python can understand using a 2D-Array
    def process_board(self, board_info):
        # Creating a 4X4 2D array to represent the state of the game
        board_array = [[0 for i in range(4)] for j in range(4)] 
        # For all the tiles that exist on the board
        for tile in board_info:
            #Split the class name to get information from it
            tile_parts = tile.split("-")
            # Parse the values
            value_parts = tile_parts[1].split(" ")
            tile_value = int(value_parts[0])
            x_tile = int(tile_parts[3])
            y_tile = int(tile_parts[4][0])
            # Add the values to the board array
            board_array[y_tile-1][x_tile-1] = tile_value
        return board_array
    
    # This method will call methods to simulate all 4 moves(Up, Down, Left, and Right) and then once the simulate methods return
    # the simulated boards a method is called to evaluate their score 
    def simulate_moves(self, board_array):
        
        # Create new copies of the boards to be simulated on 
        right_board = deepcopy(board_array)
        left_board = deepcopy(board_array)
        up_board = deepcopy(board_array)
        down_board = deepcopy(board_array)
        print("Original:")
        for row in board_array:
                print(row)
        # Simulate actions on repective boards
        self.simulate_right(right_board)
        self.simulate_left(left_board)
        self.simulate_down(down_board)
        self.simulate_up(up_board)

        # Now calculate score based on making those moves
        left_score = self.score(left_board)
        print("Left score: {} ".format(left_score))
        right_score = self.score(right_board)
        last_right_board = right_board
        print("Right score: {} ".format(right_score))
        down_score = self.score(down_board)
        print("Down score: {} ".format(down_score))
        up_score = self.score(up_board) - 100
        print("Up score: {} ".format(up_score))
        # Chooses which move to make based on score prioritizing moving left and down
        if(up_score + 100 == down_score and down_score == left_score and left_score == right_score):
            x = random.randrange(1,5,1)
            return x
        elif left_score == max([left_score,right_score,down_score,up_score]):
            # If the left repeats
            if board_array == left_board:
                print("REPEATING LEFT")
                return 3
            return 1    
        elif down_score == max([left_score,right_score,down_score,up_score]):
            return 2
        elif right_score == max([left_score,right_score,down_score,up_score]):
            if board_array == right_board:
                return 1
            return 3
        elif up_score == max([left_score,right_score,down_score,up_score]):
            return 4

        
    def score(self, board_array):
        score = 0
        all_tile_values = []
        for row in board_array:
            for x in range(0,4,1):
                all_tile_values.append(row[x])
                if row[x] != 0:
                    score = score + row[x]
                elif row[x] == 0:
                    score = score + 256
        all_tile_values.sort()
        if board_array[3][0] == all_tile_values[-1] and board_array[3][1] == all_tile_values[-2] and board_array[3][2] == all_tile_values[-3] and board_array[3][3] == all_tile_values[-4]:
            score += 1250
        elif board_array[3][0] == all_tile_values[-1] and board_array[3][1] == all_tile_values[-2] and board_array[3][2] == all_tile_values[-3]:
            score += 1000
        elif board_array[3][0] == all_tile_values[-1] and board_array[3][1] == all_tile_values[-2]:
            score += 750
        elif board_array[3][0] == all_tile_values[-1]:
            score += 500
        return score

    # This method will take the board_array that represents the current game state and then with 
    # logic will simulate what will happen if the AI was to move right
    def simulate_right(self, board_array):
            for row in board_array:
                # What to to for the second from right block
                if row[2] != 0:
                    if row[3] == 0:
                        row[3] = row[2]
                        row[2] = 0
                    elif row[3] == row[2]:
                        row[3] = row[2]+row[3]
                        row[2] = 0
            
                # What to do for the second from left block
                if row[1] != 0:
                    # Represents if no other blocks in the row are occupied
                    # Can guarantee that if row[3] is empty row[2] is also empty
                    if row[3] == 0:
                        row[3] = row[1]
                        row[1] = 0
                    # Represents if the right-most block is occupied 
                    elif row[3] != 0 and row[2] == 0:
                        if row[1] == row[3]:
                            row[3] = row[1] + row[3]
                            row[1] = 0 
                        elif row[1] != row[3]:
                            row[2] = row[1]
                            row[1] = 0
                    # Represents if both blocks are occupied
                    elif row[2] != 0:
                        if row[1] == row[2]:
                            row[2] = row[1] + row[2]
                            row[1] = 0

                # What to do for the far left block
                if row[0] != 0:
                    # Represents if no other blocks in the row are occupied
                    if row[3] == 0:
                        row[3] = row[0]
                        row[0] = 0
                    elif row[3] != 0 and row[2] == 0 and row[1] == 0:
                        if row[0] == row[3]:
                            row[3] = row[0] + row[3]
                            row[0] = 0 
                        elif row[0] != row[3]:
                            row[2] = row[0]
                            row[0] = 0
                    elif row[2] != 0 and row[1] == 0:
                        if row[0] == row[2]:
                            row[2] = row[2] + row[0]
                            row[0] = 0
                        else:
                            row[1] = row[0]
                            row[0] = 0
                    elif row[1] !=0:
                        if row[0] == row[1]:
                            row[1] = row[0] + row[1]
                            row[0] = 0
            print("Right Array:")
            for row in board_array:
                print(row)

    def simulate_left(self, board_array):
        for row in board_array:
                # What to to if there is a block in the second to left
                if row[1] != 0:
                    # If the left-most block is empty
                    if row[0] == 0:
                        row[0] = row[1]
                        row[1] = 0
                    # If the left most block is the same as the second
                    elif row[0] == row[1]:
                        row[0] = row[1]+row[0]
                        row[1] = 0
            
                # What to do for the second from right block
                if row[2] != 0:
                    # Represents if no other blocks in the row are occupied
                    # Can guarantee that if row[0] is empty row[1] is also empty
                    if row[0] == 0:
                        row[0] = row[2]
                        row[2] = 0
                    # Represents if the left-most block is occupied but not [1]
                    elif row[0] != 0 and row[1] == 0:
                        if row[2] == row[0]:
                            row[0] = row[2] + row[0]
                            row[2] = 0 
                        elif row[2] != row[0]:
                            row[1] = row[2]
                            row[2] = 0
                    # Represents if both blocks are occupied
                    elif row[1] != 0:
                        if row[1] == row[2]:
                            row[1] = row[1] + row[2]
                            row[2] = 0

                # What to do for the far right block
                if row[3] != 0:
                    # Represents if no other blocks in the row are occupied
                    if row[0] == 0:
                        row[0] = row[3]
                        row[3] = 0
                    elif row[0] != 0 and row[2] == 0 and row[1] == 0:
                        if row[0] == row[3]:
                            row[0] = row[0] + row[3]
                            row[3] = 0 
                        elif row[0] != row[3]:
                            row[1] = row[3]
                            row[3] = 0
                    elif row[1] != 0 and row[2] == 0:
                        if row[3] == row[1]:
                            row[1] = row[1] + row[3]
                            row[3] = 0
                        else:
                            row[2] = row[3]
                            row[3] = 0
                    elif row[2] !=0:
                        if row[3] == row[2]:
                            row[2] = row[3] + row[2]
                            row[3] = 0
        print("Left Array:")
        for row in board_array:
            print(row)
    def simulate_down(self, board_array):
        # Checks by column
        for x in range(0,4,1):
            # What to do if the second from the bottom has a tile
            if board_array[2][x] != 0:
                # If the bottom tile in the column is not occupied
                if board_array[3][x] == 0:
                    board_array[3][x] = board_array[2][x]
                    board_array[2][x] = 0
                # If it is occupied and they are the same value
                elif board_array[3][x] != 0 and board_array[2][x] == board_array[3][x]:
                    board_array[3][x] = board_array[2][x]+board_array[3][x]
                    board_array[2][x] = 0
            # What to do if the second from the top of the column is occupied
            if board_array[1][x] != 0:
                # If no other tiles in the column are occupied go straight to the bottom
                if board_array[3][x] == 0:
                    board_array[3][x] = board_array[1][x]
                    board_array[1][x] = 0
                # If only the bottom on is occupied
                elif board_array[3][x] != 0 and board_array[2][x] == 0:
                    # and the value is the same as the one in the bottom
                    if board_array[3][x] == board_array[1][x]:
                        board_array[3][x] = board_array[3][x] + board_array[1][x]
                        board_array[1][x] = 0
                    # and they are different values
                    elif board_array[3][x] != board_array[1][x]:
                        board_array[2][x] = board_array[1][x]
                        board_array[1][x] = 0
                # If both the second to the bottom and the bottom are occupied
                elif board_array[2][x] != 0:
                    if board_array[2][x] == board_array[1][x]:
                        board_array[2][x] = board_array[1][x] + board_array[2][x]
                        board_array[1][x] = 0
            # If the top tile of the column is occupied
            if board_array[0][x] != 0:
                # If the bottom tile in the column is not occupied
                if board_array[3][x] == 0:
                    board_array[3][x] = board_array[0][x]
                    board_array[0][x] = 0
                # If only the bottom on is occupied
                elif board_array[3][x] != 0 and board_array[2][x] == 0 and board_array[1][x] == 0:
                    # and the value is the same as the one in the bottom
                    if board_array[3][x] == board_array[0][x]:
                        board_array[3][x] = board_array[3][x] + board_array[0][x]
                        board_array[0][x] = 0
                    # and they are different values
                    elif board_array[3][x] != board_array[0][x]:
                        board_array[2][x] = board_array[0][x]
                        board_array[0][x] = 0
                elif board_array[2][x] != 0 and board_array[1][x] == 0:
                    if board_array[2][x] == board_array[0][x]:
                        board_array[2][x] = board_array[2][x] + board_array[0][x]
                        board_array[0][x] = 0
                    else:
                        board_array[1][x] = board_array[0][x]
                        board_array[0][x] = 0
                elif board_array[1][x] != 0:
                    if board_array[1][x] == board_array[0][x]:
                        board_array[1][x] = board_array[1][x] + board_array[0][x]
                        board_array[0][x] = 0
        print("Down Array:")
        for row in board_array:
            print(row)
    def simulate_up(self, board_array):
        # Checks by column
        for x in range(0,4,1):
            # What to do if the second from the bottom has a tile
            if board_array[1][x] != 0:
                # If the bottom tile in the column is not occupied
                if board_array[0][x] == 0:
                    board_array[0][x] = board_array[1][x]
                    board_array[1][x] = 0
                # If it is occupied and they are the same value
                elif board_array[0][x] != 0 and board_array[1][x] == board_array[0][x]:
                    board_array[0][x] = board_array[1][x]+board_array[0][x]
                    board_array[1][x] = 0
            # What to do if the second from the top of the column is occupied
            if board_array[2][x] != 0:
                # If no other tiles in the column are occupied go straight to the bottom
                if board_array[0][x] == 0:
                    board_array[0][x] = board_array[2][x]
                    board_array[2][x] = 0
                # If only the bottom on is occupied
                elif board_array[0][x] != 0 and board_array[1][x] == 0:
                    # and the value is the same as the one in the bottom
                    if board_array[0][x] == board_array[2][x]:
                        board_array[0][x] = board_array[0][x] + board_array[2][x]
                        board_array[2][x] = 0
                    # and they are different values
                    elif board_array[0][x] != board_array[2][x]:
                        board_array[1][x] = board_array[2][x]
                        board_array[2][x] = 0
                # If both the second to the bottom and the bottom are occupied
                elif board_array[1][x] != 0:
                    if board_array[1][x] == board_array[2][x]:
                        board_array[1][x] = board_array[2][x] + board_array[1][x]
                        board_array[2][x] = 0
            # If the top tile of the column is occupied
            if board_array[3][x] != 0:
                # If the bottom tile in the column is not occupied
                if board_array[0][x] == 0:
                    board_array[0][x] = board_array[3][x]
                    board_array[3][x] = 0
                # If only the bottom on is occupied
                elif board_array[0][x] != 0 and board_array[1][x] == 0 and board_array[2][x] == 0:
                    # and the value is the same as the one in the bottom
                    if board_array[0][x] == board_array[3][x]:
                        board_array[0][x] = board_array[0][x] + board_array[3][x]
                        board_array[3][x] = 0
                    # and they are different values
                    elif board_array[0][x] != board_array[3][x]:
                        board_array[1][x] = board_array[3][x]
                        board_array[3][x] = 0
                elif board_array[1][x] != 0 and board_array[2][x] == 0:
                    if board_array[1][x] == board_array[3][x]:
                        board_array[1][x] = board_array[1][x] + board_array[3][x]
                        board_array[3][x] = 0
                    else:
                        board_array[2][x] = board_array[3][x]
                        board_array[3][x] = 0
                elif board_array[2][x] != 0:
                    if board_array[2][x] == board_array[3][x]:
                        board_array[2][x] = board_array[2][x] + board_array[3][x]
                        board_array[3][x] = 0
        print("Up Array:")
        for row in board_array:
            print(row)
                    

                 
            

