# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:11:12 2020

@author: lara-
"""

from class_card import Card
import random 

class Deck():
    
    def __init__(self):
        
        self.deck =[]
        
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}  
     
        self.create_deck()
        
    def create_deck(self):
        
        self.deck = []
        
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank, self.values[rank]))
                
    def deal_card(self):
        return self.deck.pop(0)
    
    def shuffle(self):
       # self.create_deck() #para garantir que nao fico sem cartas, cada jogo tem um baralho novo
        random.shuffle(self.deck)
    
    def __str__(self):
        text=" "
        for card in self.deck:
            text+=str(card)+"; "
        return text
    
