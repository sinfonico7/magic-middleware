import json

class MagicCard:

   def __init__(self, card : any , id : str) -> None:
      self.id = id
      self.image = card.get('imageUrl')
      self.languaje = card.get('language')
      pass
   
   def __str__(self):
      card_dict = {"id": self.id,"image": self.image }
      return json.dumps(card_dict)