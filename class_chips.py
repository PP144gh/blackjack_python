
class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def set_bet(self, bet):
        print("--------------------------")
        print("Total of chips: ", self.total)
        self.bet=int(input("Bet: "))
        if self.bet <= self.total:
            remaining=self.total-self.bet
            self.total = remaining
            print("Remaining: ", remaining)
            print("--------------------------")
        else:
            print()
            print("Insuficient funds!")
            self.set_bet(self.bet)
    
    def win_bet(self,odd):
        self.total = self.total + self.bet*odd
        print("Your net profit was:", self.bet*(odd-1))
        self.bet = 0
        
    
    def lose_bet(self):
        self.total = self.total 
        self.bet = 0 




