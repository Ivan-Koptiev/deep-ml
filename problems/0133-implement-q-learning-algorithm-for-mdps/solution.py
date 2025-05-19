import numpy as np

def q_learning(num_states, num_actions, P, R, terminal_states, alpha, gamma, epsilon, num_episodes):
    #Q(s,a) = r(s,a) + gamma * sum s'-> end (P(s'|s,a))*max_a' (Q(s',a'))
    #Q(s,a) += alpha * [r + gamma * max_a' (Q(s',a')) - Q(s,a)]
    #with p = epsillon select random action
    #with p = 1 - epsillon select highest Q-value function
    #Start with matrix of 0's and iterate num_episode times updating it
    #starting from random non-terminal state
    #P = probabilities
    #R = rewards

    #Initialize table to update
    Q_table=np.zeros((num_states,num_actions))

    #iterate by number of episodes
    for _ in range(num_episodes):

        #initialize random state on each iteration
        state = np.random.choice([i for i in range(num_states) if i not in terminal_states])

        #repeat until the end of the episode aka when terminal state is reached
        while state not in terminal_states:

            #with p=episllon select 