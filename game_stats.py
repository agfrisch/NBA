

class OE:
    def __init__(self, name):
        self.__name = name

    def get_oe_stats(self, fgm, ass, fga, orb, to):
        self.__fgm = fgm
        self.__ass = ass
        self.__fga = fga
        self.__orb = orb
        self.__to = to


    def calculate_oe(self, fgm, ass, fga, orb, to):
        self.__oe = (self.__fgm + self.__ass) / (self.__fga - self.__orb + self.__ass + self.__to)
        self.__oe_adjust = self.__oe * 100

        
    def display_oe(self, fgm, ass, fga, orb, to):
        if self.__oe_adjust in range (0, 49):
            print(f'{self.__name} had an Offensive Efficiency (OE) rating of {self.__oe:,.2f}')
            print(f'{self.__name} had a Below Average OE performance.')
        elif self.__oe_adjust in range (50, 76):
            print(f'{self.__name} had an Offensive Efficiency (OE) rating of {self.__oe:,.2f}')
            print(f'{self.__name} had an Average OE performance.')
        elif self.__oe_adjust in range (76, 99):
            print(f'{self.__name} had an Offensive Efficiency (OE) rating of {self.__oe:,.2f}')
            print(f'{self.__name} had an Above Average OE performance.')
        else:
            print(f'{self.__name} had an Offensive Efficiency (OE) rating of {self.__oe:,.2f}')
            print(f'{self.__name} had an Excellent OE performance.')




    



            
        
