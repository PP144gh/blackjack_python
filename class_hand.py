
from class_deck import Deck

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0   # start with zero value
        self.aces = 0   # you may need to add an attribute to keep track of aces 
    
    def add_card(self,card):
        self.cards.append(card)
        self.calc_value()
    
    def calc_value(self):
        points=0
       
        for card in self.cards:
            if card.get_rank() == "Ace":
                self.aces += 1
            points += card.get_value()

        if (self.aces >= 1) :
            it=0;
            while(points >21):
                points -= 10
                it+=1    
            self.aces +=self.aces-it
               
        self.value = points
        
    def __str__(self):
        text=""
        for card in self.cards:
            text+=str(card)+" "
        return text

