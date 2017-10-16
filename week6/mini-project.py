# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
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
            value += VALUES[self.cards[index].get_rank()]
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
            pos[0] = pos[0] + index*CARD_SIZE[0]*1.5
            pos[1] = pos[1]
            self.cards[index].draw(canvas, pos)
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for ranks in RANKS:
                self.deck.append(Card(suit, ranks))

    def shuffle(self):
        random.shuffle(self.deck) 

    def deal_card(self):
        if len(self.deck):
            return self.deck.pop()
        else:
            return "None"
 
    
    def __str__(self):
        str_deck = ""
        for card in self.deck:
            str_deck = str_deck + str(card) + " "
        return "Deck contains " + str_deck.strip(" ")


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer, outcome, message, player_name, dealer_name, score
    if in_play:
        score -= 1
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = "hit or stand?"
    player_name = "Player"
    dealer_name = "Dealer"
    message = ""
    in_play = True

def hit():
    global player, deck, in_play, outcome, score, message
    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
            if player.get_value() > 21:
                in_play = False
                message = "You are busted and you lose."
                outcome = "New deal?"
                score -= 1
       
def stand():
    global in_play, dealer, deck, outcome, message, score
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            message = "Dealer are busted and you win."
            outcome = "New deal?"
            score += 1
        elif dealer.get_value() >= player.get_value():
                message = "you lose."
                outcome = "New deal?"
                score -= 1
        else:
            message = "you win."
            outcome = "New deal?"
            score += 1
        in_play = False 


# draw handler    
def draw(canvas):
    global player, dealer, outcome, message, score, in_play
    canvas.draw_text("Blackjack", [200, 50], 60, "Red")
    player.draw(canvas, [40,430])
    dealer.draw(canvas, [40,200])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [40 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    canvas.draw_text(dealer_name, [70,170], 40, "Black")
    canvas.draw_text(player_name, [70,400], 40, "Black")
    canvas.draw_text(outcome, [250,400], 40, "Black")
    canvas.draw_text(message, [250,170], 40, "Black")
    canvas.draw_text("Score=" + str(score), [420, 100], 30, "Black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric