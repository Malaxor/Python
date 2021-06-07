from random import shuffle

class Card:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    
    def __init__(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def __repr__(self):
        return f"Deck of {self.count()} cards."
    
    def count(self):
        return len(self.cards)
    
    def _deal(self, amount):
        if not self.cards:
            raise ValueError("All cards have been delt.")
        # when user asks for more cards than available
        amount = min(self.count(), amount)
        if amount == 1:
            return self.cards.pop()
        return [self.cards.pop() for i in range(amount)]
        
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        shuffle(self.cards)
        return self
    
    def deal_card(self):
        return self._deal(1)
    
    def deal_hand(self, amount):
        return self._deal(amount)
    