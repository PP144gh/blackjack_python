
#Imports:
from class_deck import Deck
from class_chips import Chips
from class_hand import Hand
from class_card import Card
import random



#Functions:
def take_bet(chipsn):
      # Prompt the Player for their bet
      chipsn.set_bet(chipsn.bet)
        

def hit(deck,hand):
      hand.add_card(deck.deal_card())
 


def hit_or_stand(deck,hand):
    print("Hit or stand?")
    print("1 - Hit")
    print("2 - Stand")
    option=int(input())
    if (option==1):
        playvar=True
    elif (option==2):
        playvar=False
    else:
        print ("Invalid Option")
        hit_or_stand(deck,hand)
    return playvar


def play_again(playvar,penniless):
      if( penniless==1):
            option=2
      else:
            print("Play again?")
            print("1 - Yes")
            print("2 - No")
            option=int(input())
      if (option==1):
            playvar=True
      elif (option==2):
            print("Goodbye")
            playvar=False
      else:
            print ("Invalid Option")
            play_again()
      return playvar
   

def show_some(hand_d,hand_p):  
    print ("Dealer:")
    card_to_show=hand_d.cards[1]
    print(str(card_to_show),"(### ## ###)")   # Show only second dealer card
    print()
    print ("Player:") 
    print(str(hand_p))
    hand_p.calc_value()  
    print("Points: ", hand_p.value)
    
def show_all(hand_d,hand_p):
    print ("Dealer:")
    print (str(hand_d))
    hand_d.calc_value()  
    print("Points: ", hand_d.value)
    print()
    print ("Player:")
    print (str(hand_p))
    hand_p.calc_value()  
    print("Points: ", hand_p.value)


def player_busts():
    print ("Busted!")
    print()
    print("=======================")
    print("You Lose")
    print("=======================")
    print()
 

def player_wins():
    print("=======================")
    print("You Won!")
    print("=======================")
    print()


def dealer_busts():
    print("Dealer Busted!")  
    print("=======================")
    print("You Won!")
    print("=======================")
    print()
    
def dealer_wins():
    print()
    print("=======================")
    print("You Lose")
    print("=======================")
    print()
def tie():
    print()
    print("=======================")
    print("Tie")
    print("=======================")
    print()
    
    
#Isto tem de estar fora do while para que ele keep track das chips do player. dentro do while sempre que começa um jogo novo as chips dao restart.   
# Set up the Player's chips
chips1 = Chips()
while True:
    # Print an opening statement
    print("Welcome to the Casino!")
    print()
    print()
    print("--------------------------")
    print("Game")
    print("--------------------------")
    print()
    
    # Prompt the Player for their bet
    take_bet(chips1)
    print()

    # Create & shuffle the deck, deal two cards to each player
    deck1 = Deck()
    deck1.create_deck()
    deck1.shuffle()
    hand_player=Hand()
    hand_dealer=Hand()
    player_busted=0

    #logic behind this: dealer gives one card to the player, gives one to himself and does not show it, gives a another to the player and another to himself, this last card he shows. the players shows both of his cards. 
    for card in range(0,2):
          hand_player.add_card(deck1.deal_card())
          hand_dealer.add_card(deck1.deal_card())

    print()
    # Show cards (but keep one dealer card hidden)
    show_some(hand_dealer,hand_player)
    print()
    playing=hit_or_stand(deck1,hand_player)  # Prompt for Player to Hit or Stand
    while playing:
          hit(deck1,hand_player)
          hand_dealer.calc_value()
          if (hand_dealer.value<=17):
                hit(deck1,hand_dealer)
          hand_player.calc_value()
          #even when the dealer hits he will keep showing only his second card, I think this is how the game works
          show_some(hand_dealer,hand_player)
 
          if (hand_player.value>21): # If player's hand exceeds 21, run player_busts() and break out of loop
                player_busts()
                chips1.lose_bet()
                playing=False
                player_busted=1;

          else:
                player_busted=0;
                playing=hit_or_stand(deck1,hand_player)
            

      #END GAME SCENARIOS

      #show all cards
      # Run different winning scenarios: defini que quando o dealer busts ou o po player ganha, ganha o dobro da bet (odd=2). Nas losses perde a bet, no tie recupera a bet (odd=1)
      
      #apos um stand o dealer faz hit ate ao maximo possivel
    hand_dealer.calc_value()
    while (hand_dealer.value<=17):
          hit(deck1,hand_dealer)
          hand_dealer.calc_value()
    show_all(hand_dealer,hand_player)
    if(player_busted!=1):
          hand_dealer.calc_value()
          hand_player.calc_value()
          if(hand_dealer.value>21):
                dealer_busts()
                chips1.win_bet(2)
          else:
                if (hand_player.value>hand_dealer.value):
                      player_wins()
                      chips1.win_bet(2)
                elif(hand_player.value==hand_dealer.value):
                      tie()
                      chips1.win_bet(1)
                else:
                      dealer_wins()
                      chips1.lose_bet()
    
       
        
    
    # Inform Player of their chips total
    print("Total of chips:", chips1.total)
    if (chips1.total==0):
          print("You lost all of your chips.")
          bankrupcy=1
          play_again(playing,bankrupcy)
          break
    
    # Ask to play again
    playing=play_again(playing,0)
    if (playing==False):
          break
