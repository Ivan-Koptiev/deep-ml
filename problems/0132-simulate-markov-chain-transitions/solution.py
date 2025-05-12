import numpy as np
def simulate_markov_chain(transition_matrix, initial_state, num_steps):
    # Your code here
    steps=[initial_state]
    current_state=initial_state

    for i in range(num_steps):
        transition_probs=transition_matrix[current_state]
        
        next_state=np.random.choice(len(transition_probs),p=transition_probs)

        steps.append(next_state)

        current_state=next_state

    return steps