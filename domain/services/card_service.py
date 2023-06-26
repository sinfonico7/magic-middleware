from domain.model.card import MagicCard
from domain.model.deck import Deck
from domain.ports.card_service_port import CardServiceAbstract

class CardService(CardServiceAbstract):
    def filterCardsByLanguage(self,language: str,cards: list):
        deck = Deck()
        atributos = cards
        print('cantidad de cartas -->', len(atributos))
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