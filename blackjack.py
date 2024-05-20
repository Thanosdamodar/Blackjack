import random
from art import logo
from replit import clear

def deal_card():
  """Returns a random card from the Deck"""
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def calculate_score(dealt_card):
  if sum(dealt_card)==21 and len(dealt_card)==2:
    return 0
  elif sum(dealt_card)>21 and 11 in dealt_card:
    dealt_card.insert(dealt_card.index(11),1)
    dealt_card.remove(11)
  return sum(dealt_card)

def compare(user,comp):
  if user==0:
    print("Win with a Blackjack")
  elif comp==0:
    print("Lose, Computer has a Blackjack")
  elif comp==user:
    print("Draw")
  elif user>21:
    print("You went over, You Lose")
  elif comp>21:
    print("Computer went over, You Win")
  elif comp>user:
    print("Computer Wins")
  elif user>comp:
    print("User Wins")


def blackjack():
  print(logo)
  user_cards=[]
  computer_cards=[]
  is_game_over=False
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while is_game_over==False:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, Current Score: {user_score}")
    print(f"Computer's First Card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score>21:
      is_game_over=True
    else:
      should_user_continue=input("Type 'Y' to get another card, type 'N' to pass.  ").lower()
      if should_user_continue=="y":
        user_cards.append(deal_card())
      else:
        is_game_over=True
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  print(f"Your final hand: {user_cards}, Final Score: {user_score}")
  print(f"Computer's Final Hand: {computer_cards}, Final Score: {computer_score}")
  compare(user_score,computer_score)

  restart=input("Do you want to restart the game? Press 'Y' for yes, 'N' for no  ").lower()
  if restart=="y":
    clear()
    blackjack()
blackjack()
