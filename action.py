from rasa_core.actions import Action
import requests

class ActionGetWeather(Action):
    def name(self):
        return 'action_get_weather'
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('city')
        if city is not None:
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=cb653d3716f5bed38a5089a5116687fe'.format(city)
            req = requests.get(url)
            res = req.json()
            temp = res['main']['temp']
            dispatcher.utter_message("It is {} C in {}.".format(temp, city))
        else:
            dispatcher.utter_message("Could not get the weather.")
            
        