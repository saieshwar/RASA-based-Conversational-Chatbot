'''
## story 01
* greet
    - utter_greet

## story 02
* goodbye
    - utter_goodbye

## strory 04
* greet
    - utter_ask_location

## story 05
* inform
    - action_weather

## story 06
* inform
    - utter_ask_location
	
	
## Generated Story 1
* greet
	- utter_greet
* inform
	- utter_ask_location

* inform{"location": "charlotte"}
	- slot{"location": "charlotte"}
	- action_weather

* goodbye
	- utter_goodbye
	
## Generated Story 2
* greet
	- utter_greet
* inform
	- utter_ask_location

* inform{"location": "New York"}
	- slot{"location": "new york"}
	- action_weather

* goodbye
	- utter_goodbye
	
## Generated Story 3
* greet
	- utter_greet
* inform
	- utter_ask_location

* inform{"location": "hyderabad"}
	- slot{"location": "hyderabad"}
	- action_weather

* goodbye
	- utter_goodbye
	
## Generated Story 4
* greet
	- utter_greet
* inform
	- utter_ask_location

* inform{"location": "chicago"}
	- slot{"location": "chicago"}
	- action_weather

* goodbye
	- utter_goodbye
	
## Generated Story 5
* greet
	- utter_greet
* inform
	- utter_ask_location

* inform{"location": "Dallas"}
	- slot{"location": "Dallas"}
	- action_weather

* goodbye
	- utter_goodbye
	
## Generated Story 6
* greet
	- utter_greet
* inform
	- utter_ask_location

* inform{"location": "california"}
	- slot{"location": "california"}
	- action_weather

* goodbye
	- utter_goodbye
	
## Generated Story 7
* greet
	- utter_greet
* inform
	- utter_ask_location

* inform{"location": "Austin"}
	- slot{"location": "austin"}
	- action_weather

* goodbye
	- utter_goodbye