import json
from typing import Dict
import sys
from argparse import Namespace
from agent import agent_fn
if __name__ == "__main__":
    
    def read_input():
        """
        Reads input from stdin
        """
        try:
            return input()
        except EOFError as eof:
            raise SystemExit(eof)
    step = 0
    player_id = 0
    configurations = None
    i = 0
    while True:
        inputs = read_input()
        obs = json.loads(inputs)
        
        observation = Namespace(**dict(step=obs["step"], obs=json.dumps(obs["obs"]), remainingOverageTime=obs["remainingOverageTime"], player=obs["player"], info=obs["info"]))
        if i == 0:
            configurations = obs["info"]["env_cfg"]
        i += 1
        # data = json.dumps(dict(obs=json.loads(observation.obs), step=observation.step, remainingOverageTime=observation.remainingOverageTime, player=observation.player, reward=observation.reward))
        # observation["updates"].append(inputs)
        actions = agent_fn(observation, configurations)
        print(json.dumps(actions))