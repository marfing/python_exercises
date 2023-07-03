
from random import randrange

#singleton ?
class deck:
    def __init__(self):
        suit_types = ['clubs','diamonds','hearts','spades']
        self.suits=[]
        for s in suit_types:
            self.suits.append(suit(self, s))

    def getSuitTypes(self):
        return self.suits
    
    #random pick a card from the deck
    def getNewCard(self):
        available_cards_suit = [s for s in self.suits if s.hasNotPickedCards()]
        available_cards_suit_len = len(available_cards_suit)
        if available_cards_suit_len == 0:
            return None
        i = randrange(available_cards_suit_len) if available_cards_suit_len > 1 else 0
        return available_cards_suit[i].getCard()
   
    #all cards in the deck not picked
    def startNewGame(self):
        for su in self.suits:
            su.startNewGame()

    def getNotPickedCardsNumber(self):
        counter = 0
        for s in [su for su in self.suits if su.getNotPickedCardsNumber()]:
            counter += s.getNotPickedCardsNumber()
        return counter

#can have more than 52 cards (multiple decks together)
class blackJackDeck(deck):
    def __init__(self, decks_number) -> None:
        suit_types = ['clubs','diamonds','hearts','spades']
        self.suits = []
        for i in range(decks_number):
            for s in suit_types:
                self.suits.append(suit(self, s))      

class suit:
    def __init__(self, my_deck, type):
        self.type = type
        self.cards = []
        for i in range(13):
            self.cards.append(cards(self,i+1)) #check passing self

    def getType(self):
        return self.type

    #get random not picked card
    def getCard(self):
        not_picked = [c for c in self.cards if not c.isPicked()]
        not_picked_len = len(not_picked)
        if not_picked_len == 0:
            return None
        i = randrange(not_picked_len) if  not_picked_len > 1 else 0
        not_picked[i].setPicked()
        return not_picked[i]

    def hasNotPickedCards(self):
        if len([c for c in self.cards if not c.isPicked()]) == 0:
            return False
        return True
    
    def getNotPickedCardsNumber(self):
        counter = 0
        return len([c for c in self.cards if not c.isPicked()])
    
    def startNewGame(self):
        for c in self.cards:
            c.setPicked(False)

    def __str__(self) -> str:
        return f"{self.type}"

class cards:
    def __init__(self, my_suit, value):
        self.value = value
        self.suit = my_suit
        self.picked = False

    def setPicked(self, pick = True):
        #print(f'Cards::setPicked {self}')
        self.picked = pick
    
    def getValue(self):
        return self.value 
    
    def isPicked(self):
        return self.picked
    
    def __str__(self) -> str:
        return f"Suit: {self.suit} - value: {self.value}"


if __name__ == "__main__":
    count = 0
    #d = deck()
    d = blackJackDeck(3)
    print(f'Total number of cards available after start new game {d.getNotPickedCardsNumber()}')
    print(f'Deck suits: {[s.getType() for s in d.getSuitTypes()]}')
    card = d.getNewCard()
    while card != None:
        print(f'picked card: {card}')
        print(f'Remaining {d.getNotPickedCardsNumber()}')
        card = d.getNewCard()
        count += 1
    print(f'Total number of cards picked {count}')
    d.startNewGame()
    print(f'Total number of cards available after start new game {d.getNotPickedCardsNumber()}')
    
    

    
