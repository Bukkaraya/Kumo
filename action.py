from rasa_core.actions import Action

class ActionGetWeather(Action):
    def name(self):
        return 'action_get_weather'
    
    def run(self):
        print('Here is the weather...')
        pass