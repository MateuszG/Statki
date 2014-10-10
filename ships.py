from random import randint,randrange

class Ships(object):
    def __init__(self):
        self.list = []
        self.x = 0
        self.y = 0
        self.pos = 0
        self.times = 0
        self.list_of_ships = []
        self.make_ship()
        
    def append_ship(self,times):
        self.times = times
        self.x = randint(1,9)
        self.y = randint(1,9)
        self.list.append([self.x,self.y])
        if self.times > 1:
            self.pos = randrange(0,2)
            if self.pos == 1:
                self.get_next_cord_x(self.x,self.y,self.times)
            if self.pos == 0:
                self.get_next_cord_y(self.x,self.y,self.times)
        else:
            pass

    def get_next_cord_x(self,x,y,times):
        if x + self.times < 10 and x - self.times > 0: 
            for _ in range(self.times):
                if len(self.list) == self.times:
                    return 0
                x2 = randrange(self.x-1,self.x+1)
                if x2 >= 1 and x2 <= 9 and self.x != x2:
                        self.x = x2
                        self.list.append([self.x,self.y])
                else:
                        self.get_next_cord_x(self.x,self.y,self.times)
        else:
            self.list = []
            self.x = randint(1,9)
            self.y = randint(1,9)
            self.list.append([self.x,self.y])
            self.get_next_cord_x(self.x,self.y,self.times)

    def get_next_cord_y(self,x,y,times):
        if y + self.times < 10 and y - self.times > 0: 
            for _ in range(self.times):
                if len(self.list) == self.times:
                    return 0
                y2 = randrange(self.y-1,self.y+1)
                if y2 >= 1 and y2 <= 9 and self.y != y2:
                        self.y = y2
                        self.list.append([self.x,self.y])
                else:
                        self.get_next_cord_y(self.x,self.y,self.times)
        else:
            self.list = []
            self.x = randint(1,9)
            self.y = randint(1,9)
            self.list.append([self.x,self.y])
            self.get_next_cord_y(self.x,self.y,self.times)
  
    def add_ship(self,b):
        if self.list_of_ships != []:
            for i in b.list:
                if i not in self.list_of_ships:
                    self.list_of_ships += b.list

        else:
            self.list_of_ships += b.list
                
    def make_ship(self):
        self.add_ship(Mast_4())
        self.add_ship(Mast_3())
        self.add_ship(Mast_3())
        self.add_ship(Mast_2())
        self.add_ship(Mast_2())
        self.add_ship(Mast_2())
        self.add_ship(Mast_1())
        self.add_ship(Mast_1())
        self.add_ship(Mast_1())
        self.add_ship(Mast_1())
        while len(self.list_of_ships) < 20:
            self.add_ship(Mast_1())
            if len(self.list_of_ships) > 19:
                break

class Mast_1(Ships):
    def __init__(self):
        self.list = []
        self.append_ship(1)
        
class Mast_2(Ships):
    def __init__(self):
        self.list = []
        self.append_ship(2)
        
class Mast_3(Ships):
    def __init__(self):
        self.list = []
        self.append_ship(3)
        
class Mast_4(Ships):
    def __init__(self):
        self.list = []
        self.append_ship(4)
