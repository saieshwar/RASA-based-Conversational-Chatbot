# Chatbot
RASA based Weather providing ChatBot

This project is a user friendly, web-based application dedicated to answering weather-related queries of the user. This application can be used by anyone to understand the weather of any particular city in the world. When the user asks the bot a question, the bot first identifies the intents and entities from the question and builds a response and sends the same to the user.

For Instance, the chatbot we designed works as follows:
If the user types a question asking the weather of Charlotte Location as below.

User: What’s the weather in Charlotte?

Intent: action_weather (this action is triggered and this makes an API call to "OpenWeatherMap's" and fetches the details)
Entities: Charlotte (Location)

Chatbot builds a response based on the API call and responds to the user as below
Chatbot: “The weather in Charlotte tomorrow is 75F max and 70F min. the weather is clear sky.....................and so on”

The framework used: RASA
<br/>

Languages used: Python
<br/>

Training: NLU model training based on manually created data (data.json) and dialogue management model training based on user generated stories (stories.md)
