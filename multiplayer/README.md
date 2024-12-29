#1.  Multiplayer

Before starting the game, ask "Welcome to Blackjack! How many players? ".

Ask for each players name and then let each player play a hand of blackjack, printing out {"{player_name}'S TURN" as a header before each individual turn.

Keep track of each players hand total.

After each player is done playing, simulate the dealer playing.

Compare each individual player's hand value to the dealer's hand value and for each player print out either "{player_name} wins!", "{player_name} loses!" , or "{player_name} pushes." (Note that each player plays individually against the dealer rather than against each other.) 

#2. Multiple rounds and scorekeeping

When the game starts, each player starts with a score of 3.

When winners/losers are being determined, update each players scores as follows:

If the player wins: increase their score by 1 and print out "{player_name} wins! Score: {new_score}"

If the player loses: decrease their score by 1 and print out "{player_name} loses! Score: {new_score}"

If the player pushes: do not update their score and print out "{player_name} pushes. Score: {new_score}"

At the end of everyone's turn, ask "Do you want to play another hand (y/n)? " 

If the user selects 'y', play another round with the newly updated scores (i.e. if they win the first 2 rounds, their score will be 5)

If the user selects 'n', end the game.

#3. Elimination!

If a user's score hits 0 at the end of a round, print out "{player_name} eliminated!" and remove them from playing in any future rounds.

If at the end of a round all player's are eliminated, print out "All players eliminated!" and end the game.