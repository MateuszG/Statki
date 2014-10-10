from map import Game_map
from ships import Ships

class Battle(object):
    def __init__(self, x = ' ', y = ' ', turn = 1):
        self.x = x
        self.y = y
        self.turn = turn
        self.Begin()
        self.array_of_ship = []

    def Begin(self):
        my_ships = Ships()
        self.array_of_ships = my_ships.list_of_ships
        
        computer_ships = Ships()
        self.array_of_computer_ships = computer_ships.list_of_ships
        
        my_ships = Game_map("1",0)
        computer_ships = Game_map("2",0)
        
        print("Tura nr:",self.turn)
        
        my_ships.show_ships(self.array_of_ships)
        computer_ships.hide_ships(self.array_of_computer_ships)
        
        for self.turn in range(20):
            computer_ships.Input_data()
            print("Tura nr:",self.turn+1)
            my_ships.computer_AI()
            computer_ships.shot_list()


        