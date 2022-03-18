# I creted this programa to calculation delta

# This program takes three square roots and then solves the delta caculation

#import of modules
import math

class Delta:


    def __init__(self):
        self.values()
        self.calc_delta()
        self.checking_delta()
        pass

    # Reciveing  theValues
    def values(self):
        self.a = float (input('Enter the value of a > '))
        self.b = float (input('Enter the value of b > '))
        self.c = float (input('Enter the value of c > '))
    
    # Calculation of delta
    def calc_delta(self):
        self.calc = self.b**2 - 4 * self.a * self.c
        return self.calc

    # Checking the rules for the values of deta
    def checking_delta(self):
        if self.calc > 0:
            self.x1 = (-self.b + math.sqrt(self.calc)) / (2*self.a)
            self.x2 = (-self.b - math.sqrt(self.calc)) / (2*self.a)
            print(f'x1= {self.x1} \n x2 = {self.x2}')
        
        elif self.calc == 0:
            self.x = (-self.b + math.sqrt(self.calc)) / (2*self.a)
            print(f'O o valor da rais real é= {self.x}')

        else:
            print('No real root')

start = Delta()
start.__init__()