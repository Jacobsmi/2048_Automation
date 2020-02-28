from game import Driver
from array import *
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
        # Next process the board_info so the program can understand how the board looks
        board_array = self.process_board(board_info)
        # Once input has been parsed and board has been created then moves must be simulated
        best_move = self.simulate_moves(board_array)


    # Method takes unprocessed board info and creates a layout of the game that python can understand using a 2D-Array
    def process_board(self, board_info):
        # Creating a 4X4 2D array to represent the state of the game
        board_array = [[0 for i in range(4)] for j in range(4)] 
        # For all the tiles that exist on the board
        for tile in board_info:
            #Split the class name to get information from it
            tile_parts = tile.split("-")
            # Parse the values
            tile_value = int(tile_parts[1][0])
            x_tile = int(tile_parts[3])
            y_tile = int(tile_parts[4][0])
            # Add the values to the board array
            board_array[y_tile-1][x_tile-1] = tile_value
            print("Placing tile")
        # Prints the board in its current state
        for row in board_array:
            print(row)
        return board_array
    
    
    def simulate_moves(self, board_array):
        print("Testing array")
        right_score = self.simulate_right(board_array)

    # This method will take the board_array that represents the current game state and then with 
    # logic will simulate what will happen if the AI was to move right
    def simulate_right(self, board_array)    

    