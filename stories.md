## greet
* greet
    - utter_greet

## weather_1
* weather{"city": "Toronto"}
    - action_get_weather

## weather_2
* weather
    - utter_get_city
* inform{"city": "Toronto"}
    - action_get_weather