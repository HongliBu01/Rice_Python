# Testing template for the Hand class


import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)

class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        str_card = ""
        for card in self.cards:
            str_card = str_card + str(card) + " "
        return "Hand contains " + str_card.strip(" ")

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        count = 0
        for index in range(len(self.cards)):
            values += VALUES[self.cards[index].get_rank()]
            if self.cards[index].get_rank() == "A":
                count += 1
        if count == 0:
            return value
        else :
            if value + 10 <= 21:
                return value + 10
            else:
                return value

    def draw(self, canvas, pos):
        for index in range(len(self.cards)):
            pos[0] = pos[0] + index*CARD_SIZE[0]*1.2
            pos[1] = pos[1]
            self.cards[index].draw(canvas, pos)

# Test code

c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
print c1, c2, c3
print type(c1), type(c2), type(c3)

test_hand = Hand()
print test_hand

test_hand.add_card(c1)
print test_hand

test_hand.add_card(c2)
print test_hand

test_hand.add_card(c3)
print test_hand

print type(test_hand)


###################################################
# Output to console
# note that the string representation of a hand will 
# vary based on how you implemented the __str__ method

#SA C2 DT
#<class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
#Hand contains 
#Hand contains SA 
#Hand contains SA C2 
#Hand contains SA C2 DT 
#<class '__main__.Hand'>