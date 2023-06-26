
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
                    newCard = MagicCard(card['id'], 'sin url')
            else:
                for language_json in card['foreignNames']:
                    newCard = MagicCard(card['id'], language_json['imageUrl'])     
            pass    
            deck.addCardToDeck(newCard)
        return deck
    '''
    def filterCardsByLanguage(self,language:str, cards: list) -> Deck:
        deck = Deck()
        atributos = cards
        for card in atributos:
            try:
                if card['foreignNames'] is None:
                    newCard = MagicCard('sin arrglo id --> ', card['id'])
                    deck.addCardToDeck(newCard)
                    pass     
                for language_json in card['foreignNames']:
                    if language_json['language'] == language:
                        newCard = MagicCard(language_json['imageUrl'])
                        deck.addCardToDeck(newCard)
                    pass
            except KeyError:
                print("Error: La clave 'foreignNames' no está presente en el JSON.")
        return deck
    '''