import json
import random
from src.junk.junk import Junk

def junk_list():
    with open("./junk.json", "r+") as a:
        items = json.load(a)

    random_num = random.randint(1, len(items)) # quantidade x random

    # Selecionar aleatoriamente essa quantidade x de itens
    random_items= random.sample(items, random_num)

    junk_items = []
    for item in random_items:
        name = item['Scrap Name']
        value = item['Value Range'] 
        weight = item['Weight']
        junk_items.append(Junk(name, value, weight))

    return junk_items