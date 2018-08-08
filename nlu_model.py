from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Metadata, Interpreter

def train():
    training_data = load_data("./data/training_data.json")
    trainer = Trainer(config.load("config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('./models/nlu')
    return model_directory

def run(dir):
    interpreter = Interpreter.load(dir)
    while True:
        res = interpreter.parse(input('>'))
        print(res)

if __name__ == '__main__':
    dir = train()

    #run(dir)

    