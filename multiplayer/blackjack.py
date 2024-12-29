# Use randint to generate random cards. 
from blackjack_helper import *

'''
# commented because this section is in single player mode.

# USER'S TURN
user_hand = draw_starting_hand("YOUR")
should_hit = 'y'
while user_hand < 21:
  should_hit = input("You have {}. Hit (y/n)? ".format(user_hand))
  if should_hit == 'n':
    break
  elif should_hit != 'y':
    print("Sorry I didn't get that.")
  else:
    user_hand = user_hand + draw_card()
print_end_turn_status(user_hand)
  
# DEALER'S TURN
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
  print("Dealer has {}.".format(dealer_hand))
  dealer_hand = dealer_hand + draw_card()
print_end_turn_status(dealer_hand)

# GAME RESULT
print_end_game_status(user_hand, dealer_hand)
'''

def main():
  #main function to run the game
  players = get_players() #get the list of players
  scores = initialize_scores(players) #initialize their scores

  while True:
    #play a round
    players_hands = {} #dictionary to store player's hands
    for player in players.copy(): #loop through players
      players_hands[player] = player_turn(player)

    dealer_hand = dealer_turn() #play the dealer's turn
    results = compare_results(players_hands, dealer_hand) #compare hands
    scores = update_scores(scores, results) #update scores
    players, scores = eliminate_players(scores, players) #eliminate players with 0 score

    if check_all_eliminated(players): #check if all players are eliminated
      break
    if not ask_continue(): #ask if they want to continue playing
      break

if __name__ == "__main__":
  main()