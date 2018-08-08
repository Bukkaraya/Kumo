import logging

from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    dialog_training_data_file = './stories.md'
    path_to_model = './models/dialogue'

    agent = Agent('domain.yml', 
                policies = [MemoizationPolicy(), KerasPolicy()])
    
    agent.train(dialog_training_data_file)

    agent.persist(path_to_model)