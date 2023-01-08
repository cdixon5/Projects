#!/usr/bin/env python3

from time import sleep
import math
import string
import numpy as np


def blackjack():
	import random

		# Create deck of cards
	cardtype = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	deck = dict.fromkeys(cardtype, 4)
	cards = []
	knownCards =[]
	for ct in deck:
		cards.extend([ct for x in range(0,4)])

		# Function to draw a random card from deck: choose random card and remove from deck
	def draw_card():
		card = random.choice(cards)
		cards.remove(card)
		return card

		# Sum user's hand: find sum of list
	def cardsum(cardlist):
		count = cardlist.count('A')
		cardlist = [x for x in cardlist if x != 'A']
		cardlist.extend(['A' for x in range(count)])
		sumofcards = 0
		for c in cardlist:
			if c.isdigit():
				sumofcards+=int(c)
			elif c in ['K','Q','J']:
				sumofcards+=10
			else:
				sumofcards+=11
				if sumofcards > 21:
					sumofcards-=11
					sumofcards+=1
		return sumofcards
             
		# Clear screen and print message on top of screen  
	print('\033c\t\t\tBlackJack Simulator by Cadabra')

		# Draw player's first two cards
	card1 = draw_card()
	card2 = draw_card()
	your_cards = [card1,card2]

		# Draw dealer's first two cards
	card1 = draw_card()
	card2 = draw_card()
	opp_cards = [card1,card2]

		# Check for user blackjack (21 off first 2 cards)
	if cardsum(your_cards) == 21:
		print('Your cards:')
		print('', *your_cards, sep = '  ') ; sleep(1.2)
		print('\nPlayer BlackJack!') ; sleep(1.8)
		userBJ = 1
	else:
		print('Your cards:')
		print('', *your_cards, sep = '  ')
		your_sum = cardsum(your_cards)
		print(f'\nYour Sum:\n  {your_sum}\n')
		userBJ = 0


		# Check for dealer blackjack (21 off first 2 cards)
	if cardsum(opp_cards) == 21:
		print('Dealer cards:')
		print('', *opp_cards, sep = '  ') ; sleep(1.2)
		print('\n Dealer BlackJack!') ; sleep(1.8)
		dealBJ = 1
	else:
		print(f'\nDealer cards:\n  {card2}  ?\n')
		dealBJ = 0

	# RULE: If only the player or dealer gets a blackjack, they win
#	if(userBJ and !dealBJ):
#		('Player Blackjack, player wins!')
#	elif(!userBJ and dealBJ):
#		('Dealer Blackjack, dealer wins!')
#	elif(userBJ and dealBJ):
#		('Player AND Dealer Blackjack, Push! (tie)')
	
	# RULE: Player can only make moves while their score is under 21 (autostand on 21)
	while cardsum(your_cards) < 21:
		print('\n  -~-~-~-~-~-~-~-~-')
		print('  | For Help:\tH |\n  | For Stand\t0 |\n  | For Hit\t1 |')
		print('  -~-~-~-~-~-~-~-~-\n')
		stand_hit = input('  >> ')

		# If user inputs h, call help func
		if (stand_hit.lower() == 'h'):
			#help_usr()
			print('\033c\t\t\tBlackJack Simulator by Cadabra')
			print('Calculating . . .')

		# If user inputs 1, call hit func
		elif int(stand_hit) == 1:
			print('\nDrawing card . . .') ; sleep(0.7)
			drawn_card = draw_card()
			print(f'You drew a {drawn_card}!') ; sleep(1.2)
			useless = input('Press a key to continue.\n\n  >>')

			print('\033c\t\t\tBlackJack Simulator by Cadabra')
			your_cards.append(drawn_card)
			print('\033c\t\t\tBlackJack Simulator by Cadabra')
			print(f'Last drawn card:\n  {drawn_card}\n')

		# If user inputs 0, break loop
		elif int(stand_hit) == 0:
			break

		# Any other input is invalid, request new user input
		else:
			print('Invalid input!')
			continue

       
		your_sum = cardsum(your_cards)
		print(f'Your cards:')
		print('', *your_cards, sep = '  ')
		print(f'\nYour Sum:\n  {your_sum}\n')

		if(your_sum<22):
			print(f'\nDealer cards:\n  {card2}  ?\n')

	
    
	while cardsum(opp_cards) <= 21:
		print('\033c\t\t\tBlackJack Simulator by Cadabra')
			
			# Print player's cards and sum
		print(f'Your cards:')
		print('|', *your_cards, sep = '  ')
		#display_cards(your_cards)
		print(f'\nYour Sum:\n  {cardsum(your_cards)}\n')

			# Print dealer's cards and sum
		print(f'\nDealer cards:')
		print('', *opp_cards, sep = '  ')
		opp_sum = cardsum(opp_cards)
		print(f'\nOpponent Sum:\n  {cardsum(opp_cards)}\n')

			# RULE: Dealer must hit if their score is under 12
		if cardsum(opp_cards) <= 12:
			drawn_card = draw_card()
			opp_cards.append(drawn_card)
			print(f'Opponent Hits and Draws a {drawn_card}')

			# RULE: Dealer cannot hit if their score is over 15, can hit if they decide
		elif cardsum(opp_cards) > 12 and cardsum(opp_cards) < 17:
			opp_choice = random.choice([0,1])
			if opp_choice == 0:
				break
			else:
				drawn_card = draw_card()
				opp_cards.append(drawn_card)
				print(f'Opponent Hits and Draws a {drawn_card}')
		else:
			break

	your_sum = cardsum(your_cards)

	if your_sum > 21 and opp_sum <= 21:
		print('\nYou are Busted, Opponent Wins')
	elif opp_sum > 21 and your_sum <= 21:
		print('\nOpponent is Busted, You Win')
	elif opp_sum > your_sum:
		print('\nOpponent has higher value, Opponent Wins')
	elif opp_sum < your_sum:
		print('\nYou have higher value, You Win')
	else:
		print('\nSame Value, Tied')


blackjack()
