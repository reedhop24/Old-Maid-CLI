from dealer import Dealer

def play():
    print('Hello and welcome to Old Maid!\nThe goal of the game is to pair all of your cards and not be the one left with the Old Maid!\nYou will be dealt half the deck while the computer will be dealt the other half.\nYou will then be prompted to match and discard all available pairs that you can find at which point the computer will do the same.\nYou and the computer will then take turns drawing from each others deck.\nYou will choose an available index at which the card is drawn and the computer will choose a random index within your deck.\nThis goes back and forth until someone is left with the Old Maid(OM) card unable to make a pair!\nPress any Key to begin!')
    input()
    game = Dealer()
    game.player_deal()
    game.computer_deal()
    print('Your hand is: ')
    print(game.player_hand)

    game.computer_match()
    print('Match each/any of the pairs by returning each pair in the EXACT format: "2,2 J,J" ')
    init_pairs = input()
    game.player_match(init_pairs)
    
    def round():
        print('Excellent! Now it is your turn to draw from the computers hand, pick a card(index) between 0 and ' + str(len(game.computer_hand)-1))
        card_drawn = input()
        game.player_draw(card_drawn)
        print('You drew: ' + game.player_curr_card)
        print('Your hand is now:')
        print(game.player_hand)
        print('Match each/any of the pairs by returning each pair in the EXACT format: "2,2 J,J" If you do not have any pairs to match type skip')
        pairs = input()
        game.player_match(pairs)
        game.computer_draw()
        print('The computer drew: ' + game.computer_curr_card)
        game.computer_match()

        if len(game.computer_hand) == 1 and game.computer_hand[0] == 'OM' and len(game.player_hand) == 0:
            print('You Win!')
        elif len(game.player_hand) == 1 and game.player_hand[0] == 'OM' and len(game.computer_hand) == 0:
            print('Aww Shucks! You lost! Play again?')
        else:
            round()
    
    round()

play()