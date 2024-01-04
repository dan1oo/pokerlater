import random

#class for individual card
values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10, "J":11, "Q":12, "K":13, "A":14}
suits = {"C", "H", "S", "D"}
class Cards():

    def __init__(self,suit: None, rank: None):
        self.suit = suit
        self.rank = rank

    def returnsuit(self):
        return self.suit
    
    def returnrank(self):

        return self.rank
# class for deck with randomizer
class Deck():

    def __init__(self):

        self._deck = [Cards(suit ,rank) for rank in values for suit in suits]
        self.tempdeck = self._deck


    def shuffle(self):
        random.shuffle(self._deck)
        self.tempdeck = self._deck

    #testing random
    def __str__(self):
        deckstring = [f'{cards.rank},{cards.suit}' for cards in self._deck]
        prinstring = deckstring[:6]
        return str(deckstring)
    
    def deal(self):
        return self.tempdeck.pop()
    
    def burn(self):
        self.tempdeck.pop()

deck = Deck()
for x in range(10):
    print(deck)
    deck.shuffle()







    


    

