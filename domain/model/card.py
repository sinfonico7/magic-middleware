import json

class MagicCard:

   def __init__(self, id : str,imageUrl : str) -> None:
      self.id = id
      self.image = imageUrl
      pass
   
   def __str__(self):
      card_dict = {"id": self.id,"image": self.image }
      return json.dumps(card_dict)