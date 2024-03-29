# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:33:01 2019

@author: thnxe
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 00:02:56 2019

@author: thnxe
"""
import numpy as np
import random
from importfromlist import next_states, next_actions
from get_rewards_new import final_rewards
from IPython.display import clear_output
alpha = 0.1
gamma = 0.6 
epsilon = 0.5
#actions=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
#states=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
states=np.arange(32)
actions=np.arange(37)
ns=32
na=37
max_epochs=132123
q_table = np.zeros([32, 37])
policy=[]*32
state = np.random.randint(0,ns)
#actions=np.asarray(actions)
#def train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs):
#final_rewards=[[1,-10,0,1],
#               [1,-10,0,1],
#               [1,-10,0,1],
#               [1,-10,0,1]]     
for i in range(0,max_epochs):
        
        done = False
        epochs, penalties, reward, = 0, 0, 0
    
        
        if random.uniform(0, 1) < epsilon:
            if(random.uniform(0,1)<0.5):
                action = random.randint(15,35) # Explore action space
            else:
                for a in next_actions:
                    if(a[0]==i):            #
                        action=a[1]
        else:
            action = np.argmax(q_table[state]) # Exploit learned values

        for a in next_states:
            if(a[0]==i):            #
                next_state=a[1]
        reward=final_rewards[state][action] + penalties
        
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
            
#        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
#        q_table[state, action] = new_value
        q_table[state][action] = reward + gamma * max(q_table[next_state])
        if reward == -10:
            penalties += 1
                
        state = next_state
        epochs += 1
            
        if i % 1000 == 0:
            clear_output(wait=True)
            print(f"Episode: {i}")
            
            
print("Training finished.\n")
#print(q_table)
for i in range(ns):
    policy.append(np.argmax(q_table[i])) #note: policy is taken as a list rather than np array
print(policy)
            
        