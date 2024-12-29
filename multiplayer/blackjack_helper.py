from random import randint

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
  if card_rank == 1:
    card_name = 'Ace'
  elif card_rank == 11:
    card_name = 'Jack'
  elif card_rank == 12:
    card_name = 'Queen'
  elif card_rank == 13:
    card_name = 'King'
  else:
    card_name = card_rank

  if card_rank == 8 or card_rank == 1:
    print('Drew an ' + str(card_name))
  elif card_rank < 1 or card_rank > 13:
    print('BAD CARD')
  else:
    print('Drew a ' + str(card_name))

# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
  card_rank = randint(1, 13)
  print_card_name(card_rank)

  if card_rank == 11 or card_rank == 12 or card_rank == 13:
    card_value = 10
  elif card_rank == 1:
    card_value = 11
  else:
    card_value = card_rank

  return card_value

# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
  print('-----------')
  print(message)
  print('-----------')

# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
  print_header(name + ' TURN')
  return draw_card() + draw_card()

# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
  print('Final hand: ' + str(hand_value) + '.')

  if hand_value == 21:
    print('BLACKJACK!')
  elif hand_value > 21:
    print('BUST.')

# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
  print_header('GAME RESULT')

  if user_hand <= 21 and (user_hand > dealer_hand or dealer_hand > 21):
    print('You win!')
  elif user_hand > 21 or (dealer_hand <= 21 and dealer_hand > user_hand):
    print('Dealer wins!')
  else:
    print('Push.')

#multiplayer
def get_players():
#ask how many players in the game and their names
  players_num = 0
  while players_num < 1: #ensure at least one person is playing
    num = input("Welcome to Blackjack! How many players? ")

    #checking if the user entered a number
    if num.isdigit(): 
      players_num = int(num) #if yes change to integer
      if players_num < 1: #if player enter negative or 0
        print("There must be at least one player.")
    else: #if player entered a string
      print("Please enter a valid number.")

  players = [] #empty list to hold name of all players
  for i in range(1, players_num+1):
    player_name = input(f"What is player {i}'s name? ").strip() #removes whitespace
    #if player enters nothing
    if player_name == "": 
      player_name = f"Player {i}"
    players.append(player_name) #append the name to the empty list
  return players

def player_turn(player_name):
#looping through every player and their turns.
  print_header(f"{player_name.upper()}'s TURN") #print players turn
  hand = draw_starting_hand(player_name) #draw the player's starting hand

  while hand < 21:
    #ask player if they want to hit or stay
    should_hit = input("You have {}. Hit (y/n)? ".format(hand)).lower()
    if should_hit == 'n': #if pressed n, exit the loop.
      break
    elif should_hit != 'y': #user presses something else then continue in the loop
      print("Sorry I didn't get that.")
      continue
    #player chooses to hit, add the card to their hand.
    hand += draw_card()

  #after players turn, show final hand and status.
  print_end_turn_status(hand)
  return hand

def dealer_turn():
  #dealer's turn 
  print("DEALER'S TURN")
  dealer_hand = draw_starting_hand("DEALER") #draw dealer's starting hand
  while dealer_hand < 17: #dealer hits until their hand is 17 or more
    print("Dealer has {}.".format(dealer_hand)) 
    dealer_hand = dealer_hand + draw_card() #add a card to dealer's hand
  print_end_turn_status(dealer_hand) #show end status
  return dealer_hand

def compare_results(players_hands, dealer_hand):
  #after all players simulate dealer's turn and compare each player's hand with dealer.
  print_header("GAME RESULT")
  results = {} #dictionary to store results for each player

  for player, hand in players_hands.items():
    #determine result based on player and dealer hand vlaues
    if hand <= 21 and (hand > dealer_hand or dealer_hand > 21):
      result = "wins"
    elif hand > 21 or (dealer_hand <= 21 and dealer_hand > hand):
      result = "loses"
    else:
      result = "pushes"
    #store the result for the player
    results[player] = result
  return results


def initialize_scores(players):
#initialize each player's to 3 at the start of the game.
  return {player: 3 for player in players}

def update_scores(scores, results):
#after each round, update the player scores.
  for player, result in results.items():
    if result == "wins" :
      scores[player] += 1 #player wins increase their score
      print (f"{player} wins! Score: {scores[player]}")
    elif result == "loses":
      scores[player] -= 1 #player loses decrease their score
      print (f"{player} loses! Score: {scores[player]}")
    else: #no score change if the player ties
      print (f"{player} pushes. Score: {scores[player]}")
  return scores

def ask_continue():
#after updating scores, ask the user if they want to play another round.
  while True:
    choice = input("Do you want to play another hand (y/n)? ")
    if choice == "y":
      return True
    elif choice == "n":
      print ("Thanks for playing!")
      return False
    else:
      print("Sorry I didn't get that.") #invalid input so ask again.

def eliminate_players(scores, players):
#after updating scores, remove any players whose scores has reached 0.
  eliminated = [] #list to store eliminate players
  for player, score in scores.items():
    if score <= 0: #if player's score is 0 or less
      eliminated.append(player)
  for player in eliminated:
    #remove player and announce elimination after player is eliminated
    print(f"{player} eliminated!")
    players.remove(player)
    del scores[player] #remove the player's score
  return players, scores

def check_all_eliminated(players):
  #check if all players have been eliminated
  if not players: #if no players are left
    print("All players eliminated!")
    return True
  return False
