# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.events import SlotSet
import requests
import json


class Prodotto(Action):

    def name(self) -> Text:
        return "action_Prodotto"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name= str(tracker.get_slot('prodotto'))
        name1=name.replace(" ","").replace("'","").lower()
        r=requests.get(url='http://localhost:3000/prodotto')
         

        if r.status_code==200: 
            data=r.json()
            if name1 in data:
                description=data[name1]['descrizione']
                nome=data[name1]['name']
                category=data[name1]['category']
                prezzo=data[name1]['prezzo']
                link=data[name1]['link']

                output='{}\n\n {} è un gioco appartenente alla categoria "{}", disponibile al prezzo di € {}.\n\n Per maggiori informazioni puoi cliccare nel seguente link {}'.format(description, nome, category, prezzo, link)
            else: 
                output='Mi dispiace, purtroppo il prodotto non è più disponibile!\n Posso fare altro per te?'
        else:
            output='error'
        
        dispatcher.utter_message(text=output)
        return []

class Personaggio(Action):

    def name(self) -> Text:
        return "action_Personaggio"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name= str(tracker.get_slot('personaggio'))
        name1=name.replace(" ","").lower()
        r=requests.get(url='http://localhost:3000/personaggio')
         

        if r.status_code==200:
            data=r.json()
            description=data[name1]['descrizione']
            nome=data[name1]['name']
            product=data[name1]['prodotti']
            
            output='{}\nTi mostro i prodotto più popolari relativi al personaggio "{}" 👇. \n{}\nVuoi ulteriori informazioni su uno di questi? Dimmi quale!'.format(description, nome, product)
            
        else:
            output='error'
        
        dispatcher.utter_message(text=output)
        return []

class Eta(Action):

    def name(self) -> Text:
        return "action_Eta"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name= str(tracker.get_slot('età'))
        r=requests.get(url='http://localhost:3000/eta')
         

        if r.status_code==200:
            data=r.json()
            nome=data[name]['name']
            product=data[name]['prodotti']
            
            output='Bene, ti mostro subito i nostri migliori prodotti per bambini da {}.👇\n{}\nDigita uno di questi per ottenere più informazioni'.format(nome, product)
        else:
            output='error'
        
        dispatcher.utter_message(text=output)
        return []

class MyFallback(Action):
    
    def name(self) -> Text:
        return "action_my_fallback"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_fallback")
        return []

class fanculo(Action):
    
    def name(self) -> Text:
        return "action_my_eta"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response = "utter_scelta_eta")
        return []
    
    
