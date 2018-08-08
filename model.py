import logging

from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

def train():
    logging.basicConfig(level='INFO')
    dialog_training_data_file = './stories.md'
    path_to_model = './models/dialogue'

    agent = Agent('domain.yml',
                policies = [MemoizationPolicy(), KerasPolicy()])
    
    agent.train(dialog_training_data_file,
                augmentation_factor=50,
                epochs=100,
                batch_size=10,)

    agent.persist(path_to_model)

if __name__ == '__main__':
    
    train()
    agent = Agent.load('./models/dialogue',
                     interpreter="./models/nlu/default/model_20180808-121641")
    agent.handle_channel(ConsoleInputChannel())
