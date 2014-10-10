from random import randint

class Game_map(object):
    def __init__(self, nr, turn, tablica = [0,0,0,0,0,0,0,0,0,0], line = ""):
        self.array_of_shots = []
        self.array_of_ships = []
        self.array_of_computer_ships = []
        self.tablica = tablica
        self.nr = nr
        self.turn = turn
        self.line = line
        self.no_print = False
        self.sign = "X"

    def computer_AI(self):
        self.x = randint(1,9)
        self.y = randint(1,9)
        for item in self.array_of_ships:
            if (self.x == item[0] and self.y == item[1]):
                self.sign = "X"
                break
            else:
                self.sign = "~"
        self.shot_list()
    
    def Input_data(self):
        self.x = int(input("Podaj wartosc x (poziomo)"))
        self.y = int(input("Podaj wartosc y (pionowo)"))
        #print(self.array_of_computer_ships)
        for item in self.array_of_computer_ships:
            if (self.x == item[0] and self.y == item[1]):
                self.sign = "X"
                break
            else:
                self.sign = "~"
        
    def show_ships(self, array_of_ships):
        i = 0
        self.array_of_ships = array_of_ships
        for item in self.array_of_ships:
            i += 1
            if (i == len(array_of_ships) - 1):
                self.no_print = False
            else:
                self.no_print = True
            self.x = item[0]
            self.y = item[1]
            self.sign = "O"
            self.shot_list()
            self.no_print = False
   
    def hide_ships(self, array_of_computer_ships):
        i = 0
        self.array_of_computer_ships = array_of_computer_ships
        for item in self.array_of_computer_ships:
            i += 1
            if (i == len(array_of_computer_ships) - 1):
                self.no_print = False
            else:
                self.no_print = True
            self.x = item[0]
            self.y = item[1]
            self.sign = " "
            self.shot_list()
            self.no_print = False
                     
    def shot_list(self):
        temp_list = []
        x = self.x
        y = self.y
        #print (x,y)
        if (x>=1 and x<=9) and (y>=1 and y<=9):
            for row_y in range(1,10):
                if row_y != 1:
                    pass
                else:
                    temp_list.append([x,y])
                    if temp_list[0] in self.array_of_shots:
                        pass
                    else:
                        self.array_of_shots.append([x,y,self.sign])
        else:
            if self.no_print == False:
                print('Wprowadzono niepoprawne koordynaty')
        self.tablica = [0,0,0,0,0,0,0,0,0,0]
        self.battlefield()

    def Add_symbol(self,symbol,line, sign):
        self.line = self.line[0:symbol-1]+sign+self.line[symbol:9]
        return(self.line)
       
    def Upper_numbers(self):
        for z in range(0,10):
            if z < 10:
                if self.no_print == False:
                    print (z, end="")
                    z=z+1
        if self.no_print == False:
            print()
        
    def Left_numbers(self, row_y, column_x):
        if row_y*column_x < 10:
            if self.no_print == False:
                print ("",end="")
        if self.no_print == False:
            print (row_y*column_x,end="" )
        
    def Count_space(self,row_y):
        self.line = ""
        lines = str(row_y)
        free_line = 12 - len(lines)
        for _ in range(free_line):
            self.line += " "
        return(self.line)

    def Make_array(self, column_x, row_y):
        for x_y in self.array_of_shots:
            list_with_x = []
            for numbers_x_y in self.array_of_shots:
                list_with_x.append(numbers_x_y[1])
                numbers = list_with_x.count(x_y[1])
            if (column_x >= 1 and row_y >= 1 and column_x <= 9 and row_y <= 10 
                and row_y == x_y[1] and column_x == x_y[0]):
                symbol = x_y[0]
                self.tablica[x_y[1]-1] = 1 + self.tablica[x_y[1]-1]
                self.Add_symbol(symbol,self.line,x_y[2])
                if self.tablica[x_y[1]-1] == numbers:
                    if self.no_print == False:
                        print(self.line, end= "")

    def battlefield(self):
        self.Upper_numbers()
        for row_y in range(1,10):
            self.Count_space(row_y)
            for column_x in range(1,13):
                if column_x != 1:
                    pass
                else:
                    self.Left_numbers(column_x, row_y)
                self.Make_array(column_x, row_y)
            self.line = ""
            if self.no_print == False:
                print()
