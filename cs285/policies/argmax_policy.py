import numpy as np


class ArgMaxPolicy(object):

    def __init__(self, critic):
        self.critic = critic

    def get_action(self, obs):
        if len(obs.shape) > 3:
            observation = obs
        else:
            observation = obs[None]
        
        ## TODO return the action that maxinmizes the Q-value 
        # at the current observation as the output
        # ............................................................
        q_actions = self.critic.qa_values(observation)
        # index = np.where(q_actions == np.max(q_actions))
        index = np.argmax(q_actions)
        # print("index = ", index)
        action = index
        # ............................................................

        return action.squeeze()