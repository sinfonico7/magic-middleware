import json
from domain.model.card import MagicCard
from typing import List
class Deck:
    
    def __init__(self) -> None:
        self.deck : List[MagicCard] = []
        pass
    
    def addCardToDeck(self, card : MagicCard):
       self.deck.append(card)
    pass

    def __str__(self):
        card_list = [{"image": card.image} for card in self.deck]
        deck_dict = {"deck": card_list}
        return json.dumps(deck_dict)
