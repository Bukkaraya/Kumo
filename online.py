import logging

from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter


logger = logging.getLogger(__name__)

def run_online_trainer(input_channel,
                        interpreter,
                        domain_def_file='domain.yml',
                        training_data_file='./stories.md'):
    agent = Agent(domain_def_file,
                    policies=[MemoizationPolicy(), KerasPolicy()])
    agent.train_online(training_data_file,
                        input_channel=input_channel)

    return agent

if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    run_online_trainer(ConsoleInputChannel(), RegexInterpreter())