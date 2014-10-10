from game_start import Game_start
import sys

class Main_menu(object):
    def __init__(self, number = 0):
        print("################")
        print("# Gra w statki #")
        print("################")
        print("1. Nowa gra")
        print("2. Ranking")
        print("3. Pomoc")
        print("4. Wyjscie")
        print("----------------")
        number = input("Wybierz jedna z ponizszych opcji w menu: ")
        self.number = int(number)
        self.Main(number)
        sign = input("Koniec?")
        if sign != 0:
            quit

    def Main(self,number):
        if (self.number == 1):
            self.Start_game()
        elif self.number == 2:
            self.Ranking()
        elif self.number == 3:
            self.Help()
        elif self.number == 4:
            self.Exit()
        else:
            print("Brak prawidlowego wyboru")

    def Start_game(self):
        game = Game_start()

    def Ranking(self):
        text_from_file = open("ranking.bin",'r')
        for line, single_line in enumerate(text_from_file):
            print(single_line)
        text_from_file.close()
        Menu = Main_menu()

    def Help(self):
        try:
            text_from_file = open("pomoc.txt",'r')
            for line, single_line in enumerate(text_from_file):
                print(single_line)
            text_from_file.close()
            Menu = Main_menu()
            
        except IOError as err:
            print("I/O error: {0}".format(err))

    def Exit(self):
        print("Wychodze")
        quit
