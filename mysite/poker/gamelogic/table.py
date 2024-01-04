import player 
import card



class Table():

    def __init__(self):
        self.seats = [(1,None),(2,None),(3,None),(4,None),(5,None),(6,None),(7,None),(8,None),(9,None),(10,None)]

        self.gamestate = False

    
    
    
    def startgame(self):
        self.gamestate = True




    def pausegame(self):
        self.gamestate = False
    def getgamestate(self):
        return self.gamestate
    
    
    


