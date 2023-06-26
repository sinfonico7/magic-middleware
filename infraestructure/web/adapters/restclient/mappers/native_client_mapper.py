
from domain.model.card import MagicCard
from domain.model.deck import Deck

class NativeMapperClient():

    def getForeignNamesFromCards(self,cards: any):
        deck = Deck()
        atributos = cards
        for card in atributos:
            newCard = None
            foreign_names = card.get('foreignNames')           
            if foreign_names is None:
                    newCard = MagicCard( { 'language':'', 'imageUrl':'sin url'},card['id'])
                    deck.addCardToDeck(newCard)
            else:
                for language_json in card['foreignNames']:
                    newCard = MagicCard(language_json, card['id'])  
                    deck.addCardToDeck(newCard)   
            pass    
            
        return deck
