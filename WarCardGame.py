import random


class Card:
    def __init__(self, name, power, quantity, pickedCard=None):
        self.name = name
        self.power = power
        self.quantity = quantity
        self.pickedCard = pickedCard
        self.totalQuantity = (self.quantity * 6)
        print("Initiation for: {:5}, power: {:2}, quantity {:2}".format(
            self.name, self.power, self.quantity,))


"""     @staticmethod
    def shuffle(cardList):
        random.shuffle(cardList) """


class Player:
    def __init__(self, name):
        self.name = name
        self.pickedCard = None
        self.selectedCards = []
        self.selectedCards = []  # List with player's cards
        print("Initiation for: {:5}".format(self.name))

    def drawCard(self):

        self.avilableCards = [k for k in range(
            len(cardList)) if cardList[k].quantity > 0]

        if len(self.avilableCards) == 0:
            print("No cards in the pot")
            return None

        self.pickedCard = random.choice(self.avilableCards)
        cardList[self.pickedCard].quantity -= 1

        self.selectedCards.append(cardList[self.pickedCard])

        return self.pickedCard

    def dealingCards(self):

        self.requiredNumberOfCards = int(
            immutableNumberOfCards / len(playersList))  # Not useful variable

        # self.drawCard


cardList = [
    Card("Ace",     14,     4),  # 0
    Card("King",    13,     4),  # 1
    Card("Quenn",   12,     4),  # 2
    Card("Jack",    11,     4),  # 3
    Card("10",      10,     4),  # 4
    Card("9",       9,      4),  # 5
]

playersList = [
    Player("Pablo"),
    Player("Ela"),
]


immutableNumberOfCards = 0
for card in range(len(cardList)):
    immutableNumberOfCards += cardList[card].quantity
