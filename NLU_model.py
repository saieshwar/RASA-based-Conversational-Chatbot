##importing necessary packages in python
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load("C:/Users/heman/Desktop/myproject/config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'weathernlu')


def run_nlu():

    interpreter = Interpreter.load('C:/Users/heman/Desktop/myproject/models/NLU/default/weathernlu')
    print(interpreter.parse("hi. i am planning to visit London, how's the weather out there. bye"))

if __name__ == '__main__':
    
    #training is already done so lets comment it out to run "run_nlu" function
    
	train_nlu('./data/data.json', "C:/Users/heman/Desktop/myproject/config_spacy.yml", 'C:/Users/heman/Desktop/myproject/models/NLU') 
    
    
	#run_nlu()