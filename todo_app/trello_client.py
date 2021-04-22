from todo_app.item import Item
import requests

import os
TRELLO_API_KEY=os.getenv('TRELLO_API_KEY')
TRELLO_API_TOKEN=os.getenv('TRELLO_API_TOKEN')

def get_cards():
    url = "https://api.trello.com/1/boards/607d74ceadb03648ed69404d/cards"

    query = {
    'key': TRELLO_API_KEY,
    'token': TRELLO_API_TOKEN
    }

    response = requests.get(
    url,    
    params=query
    ).json()
    
    cards=[]
    for item in response:
        cards.append(Item(item['idBoard'], item['id'], get_list_name(item['idList']), item['name']))
    return cards

def get_list_name(listid):
    url = f"https://api.trello.com/1/lists/{listid}"

    query = {
    'key': TRELLO_API_KEY,
    'token': TRELLO_API_TOKEN
    }

    response = requests.get(
    url,
    params=query
    ).json()

    return response['name']

def add_card(card):
    url = "https://api.trello.com/1/cards"

    query = {
    'key': TRELLO_API_KEY,
    'token': TRELLO_API_TOKEN,
    'idList': '607ee7413159d52044dd1436',
    'name': card
    }

    response = requests.post(
    url,
    params=query
    ).json()
    
    return response

def move_card(cardId):
    url = f'https://api.trello.com/1/cards/{cardId}'

    query = {
    'key': TRELLO_API_KEY,
    'token': TRELLO_API_TOKEN,
    'idList': '607ee7521f09a53fc86c5d43',
    }

    response = requests.put(
    url,
    params=query 
    ).json()

    return response