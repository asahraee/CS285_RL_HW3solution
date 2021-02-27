# CS285_RL_HW3solution

The dependencies required for this assignment are also listed in requirements.txt

## Install mujoco:
```
mkdir ~/.mujoco
cd ~/.mujoco
wget https://www.roboti.us/download/mujoco200_linux.zip
unzip mujoco200_linux.zip
mv mujoco200_linux mujoco200
rm mujoco200_linux.zip
cp <location_of_mjkey.txt> .
```
The above instructions download MuJoCo for Linux. If you are on Mac or Windows, you will need to change the `wget` address to either 
`https://www.roboti.us/download/mujoco200_macos.zip` or `https://www.roboti.us/download/mujoco200_win64.zip`.

Finally, add the following to bottom of your bashrc:
```
export LD_LIBRARY_PATH=~/.mujoco/mujoco200/bin/
```

## Install other dependencies


There are two options:

A. (Recommended) Install with conda:

	1. Install conda, if you don't already have it, by following the instructions at [this link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

	```

	This install will modify the `PATH` variable in your bashrc.
	You need to open a new terminal for that path change to take place (to be able to find 'conda' in the next step).

	2. Create a conda environment that will contain python 3:
	```
	conda create -n RL python=3.6
	```

	3. activate the environment (do this every time you open a new terminal and want to run code):
	```
	conda activate RL
	```

	4. Install the requirements into this conda environment
	```
	pip install --user -r requirements.txt
	```

	5. Allow your code to be able to see 'cs285'
	```
	cd <path to the folder that contains cs285>
	$ pip install -e .
	```

This conda environment requires activating it every time you open a new terminal (in order to run code), but the benefit is that the required dependencies for this codebase will not affect existing/other versions of things on your computer. This stand-alone environment will have everything that is necessary.


B. Install on system Python:
	```
	pip install -r requirements.txt
	```



## Setup

You can run this code on your own machine or on Google Colab. 

1. **Local option:** If you choose to run locally, you will need to install MuJoCo and some Python packages; see [installation.md](../hw1/installation.md) from homework 1 for instructions. There are two new package requirements (`opencv-python` and `gym[atari]`) beyond what was used in the previous assignments; make sure to install these with `pip install -r requirements.txt` if you are running the assignment locally.

2. **Colab:** The first few sections of the notebook will install all required dependencies. You can try out the Colab option by clicking the badges below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/berkeleydeeprlcourse/homework_fall2020/blob/master/hw3/cs285/scripts/run_hw3_dqn.ipynb) **Part I (Q-learning)** 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/berkeleydeeprlcourse/homework_fall2020/blob/master/hw3/cs285/scripts/run_hw3_actor_critic.ipynb)     **Part II (Actor-critic)** 

## Complete the code

The following files had blanks to be filled. The relevant sections are marked with `TODO`.

- [infrastructure/rl_trainer.py](cs285/infrastructure/rl_trainer.py)
- [infrastructure/utils.py](cs285/infrastructure/utils.py)
- [policies/MLP_policy.py](cs285/policies/MLP_policy.py)

- [agents/dqn_agent.py](cs285/agents/dqn_agent.py)
- [critics/dqn_critic.py](cs285/critics/dqn_critic.py)
- [policies/argmax_policy.py](cs285/policies/argmax_policy.py)

- [agents/ac_agent.py](cs285/agents/ac_agent.py)
- [critics/bootstrapped_continuous_critic.py](cs285/critics/bootstrapped_continuous_critic.py)
- [policies/MLP_policy.py](cs285/policies/MLP_policy.py)


You may also want to look through [run_hw3_dqn.py](cs285/scripts/run_hw3_dqn.py) and [run_hw3_actor_critic.py](cs285/scripts/run_hw3_actor_critic.py) (if running locally) or [run_hw3_dqn.ipynb](cs285/scripts/run_hw3_dqn.ipynb) and [run_hw3_actor_critic.ipynb](cs285/scripts/run_hw3_actor_critic.ipynb) (if running on Colab).

See the [assignment PDF](cs285_hw3.pdf) for more details on what files to edit.



