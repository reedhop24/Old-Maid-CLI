from dealer import Dealer
import unittest
import numpy 
import random

game_test_one = Dealer()

class TestInitialDeal(unittest.TestCase):

    def test_init_player(self):
        game_test_one.player_deal()
        self.assertEqual(len(game_test_one.player_hand), 26)

    def test_computer_hand(self):
        game_test_one.computer_deal()
        self.assertEqual(len(game_test_one.computer_hand), 27)

game_test_two = Dealer()

class TestSingleFilter(unittest.TestCase):
    
    game_test_two.player_deal()
    game_test_two.computer_deal()
    
    def test_computer_singles(self):
        game_test_two.computer_match()
        self.assertEqual(len(numpy.unique(game_test_two.computer_hand)), len(game_test_two.computer_hand))

    def test_player_singles(self):
        couple_dict = {

        }
        singles = []
        unmatched_lst = game_test_two.player_hand

        for i in game_test_two.player_hand:
            if i not in couple_dict:
                couple_dict[i] = i
            else:
                singles.append(i+','+i)
                del couple_dict[i]

        game_test_two.player_match(' '.join(singles))
        self.assertEqual(len(game_test_two.player_hand), len(unmatched_lst)-len(singles)*2)

game_test_three = Dealer()

class TestDrawCards(unittest.TestCase):
    
    game_test_three.player_deal()
    game_test_three.computer_deal()
    
    def test_player_draw(self):
        idx = random.randint(0, len(game_test_three.computer_hand)-1)
        game_test_three.player_draw(idx)
        self.assertEqual(game_test_three.player_curr_card, game_test_three.player_hand[len(game_test_three.player_hand)-1])

    def test_computer_draw(self):
        game_test_three.computer_draw()
        self.assertEqual(game_test_three.computer_curr_card, game_test_three.computer_hand[len(game_test_three.computer_hand)-1])
    
if __name__ == '__main__':
    unittest.main()