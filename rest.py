import json
import requests

class Rest:
  def search(self, name):
    """ 
    if requests.get(...).text => return raw JSON string (use JSON.parse in JS)
    if requests.get(...).json() => return Python dictionary (need more complex parsing in JS)
    """
    return requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' + name).text
