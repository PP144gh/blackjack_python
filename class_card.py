
class Card():
    def __init__(self, suit, rank, value):
        self.__suit = suit
        self.__rank = rank
        self.__value = value
    def get_suit(self):
        return self.__suit
    def get_rank(self):
        return self.__rank
    def get_value(self):
        return self.__value
    def __str__(self):
        return "({} of {})".format(self.__rank, self.__suit)
        
