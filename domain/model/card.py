
import json


class MagicCard:

   def __init__(self, imageUrl : str) -> None:
      self.image = imageUrl
      pass
   
   def __str__(self):
      card_dict = {"image": self.image}
      return json.dumps(card_dict)
