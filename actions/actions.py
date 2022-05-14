# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset, FollowupAction

#
from database_connectivity import DataUpdate
from weather_api import Weather
from Healthcare_locator import searchHealthcenter        

class ActionSubmit(Action): 
    def name(self) -> Text: 
                     
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        DataUpdate(tracker.get_slot("FirstName"),tracker.get_slot("LastName"),tracker.get_slot("PhoneNumber"), tracker.get_slot("EMail"), tracker.get_slot("Age"), tracker.get_slot("Location"), tracker.get_slot("Reason"),tracker.get_slot("HealthCenter"), tracker.get_slot("Date") ) 
        return []


class ActionWeather(Action): 
    def name(self) -> Text: 
                     
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        city = tracker.latest_message['text']
        temp=int(Weather(city)['temp'] - 273)
        dispatcher.utter_template("utter_weather",tracker,temp=temp) 
        return []


class ActionHealthcenterLocator(Action):
    
    def name(self) -> Text: 
                     
        return "action_search_healthcenter"


    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        location = tracker.get_slot("Location")
        healthcenterDetails = searchHealthcenter(location)
        dispatcher.utter_message(text = healthcenterDetails) 
        return []