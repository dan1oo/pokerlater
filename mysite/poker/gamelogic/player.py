

class Player():

    def __init__(self, name = "Player", stack = 0):

        self.name = name
        self.stack = stack

        self.hand = (None, None)

    def besthand(self, boardcards):
        cards = [self.hand[0], self.hand[1]]
        for x in boardcards:
            if x != None:
                cards.append(x)

        

    

