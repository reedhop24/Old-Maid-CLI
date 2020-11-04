import random
import re

class Dealer:
    def __init__(self):
        self.deck = ['2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A', 'OM']
        self.player_hand = []
        self.computer_hand = []
        self.player_curr_card = ''
        self.computer_curr_card = ''

    def player_deal(self):
        for i in range(0, 26):
            self.player_hand.append(self.deck.pop(random.randint(0, len(self.deck)-1)))

    def computer_deal(self):
        for i in range(0, 27):
            self.computer_hand.append(self.deck.pop(random.randint(0, len(self.deck)-1)))
    
    def computer_match(self):
        num_dict = {}
        singles = []
        for i in range(0, len(self.computer_hand)):
            if self.computer_hand[i] not in num_dict:
                num_dict[self.computer_hand[i]] = 1
            else:
                occ = num_dict[self.computer_hand[i]]
                occ += 1
                num_dict[self.computer_hand[i]] = occ

        for j in num_dict:
            if num_dict[j] % 2 != 0:
                singles.append(j)

        self.computer_hand = singles

    def player_match(self, idx):
        lst = re.split(',| ', idx)
        singles = []
        idx_dict = {}
            
        for i in lst:
            if i not in idx_dict:
                idx_dict[i] = 1
            else:
                occ = idx_dict[i]
                occ += 1
                idx_dict[i] = occ
        
        for j in range(0, len(self.player_hand)):
            if self.player_hand[j] in idx_dict:
                if idx_dict[self.player_hand[j]] > 0:
                    hand_occ = idx_dict[self.player_hand[j]]
                    hand_occ -= 1
                    idx_dict[self.player_hand[j]] = hand_occ
                else:
                    singles.append(self.player_hand[j])
            else:
                    singles.append(self.player_hand[j])
        
        self.player_hand = singles

    def player_draw(self, idx):
        card = self.computer_hand[int(idx)]
        self.player_curr_card = card
        self.computer_hand.pop(int(idx))
        self.player_hand.append(card)
        return card

    def computer_draw(self):
        idx = random.randint(0, len(self.player_hand)-1)
        card = self.player_hand[idx]
        self.player_hand.pop(idx)
        self.computer_hand.append(card)
        self.computer_curr_card = card       