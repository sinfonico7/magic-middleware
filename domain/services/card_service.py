
from typing import List
from domain.model.card import MagicCard
from domain.model.deck import Deck


class CardFilter():

    def filterByLanguaje(self,languaje : str, deck : Deck)-> Deck:
        deckFiltered = Deck()
        for card in deck.deck :
           if card.languaje == languaje:
               deckFiltered.addCardToDeck(card) 
        return deckFiltered