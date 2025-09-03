import numpy as np

size_map = 4
honey_map = np.ones((size_map,size_map))

honey_map[3,3] = 10   # mục tiêu có honey
honey_map[2,1] = -10  # bẫy
honey_map[1,2] = -10  # bẫy

actions = [0,1,2,3]  # up, down, left, right

q_value = {}
gamma = 0.95
alpha = 0.1

for epoch in range(10000):
    starts = np.random.randint(0,size_map,size=(2,))
    
    print("epoch:", epoch, " start:", starts)
    rewards = []
    states_actions = []
    
    while not (starts[0]==3 and starts[1]==3):
        action = np.random.choice(actions)
        old_pos = tuple(starts)
        
        if action == 0:   # up
            starts[0] = max(0, starts[0]-1)
        elif action == 1: # down
            starts[0] = min(size_map-1, starts[0]+1)
        elif action == 2: # left
            starts[1] = max(0, starts[1]-1)
        elif action == 3: # right
            starts[1] = min(size_map-1, starts[1]+1)
        
        reward = honey_map[starts[0], starts[1]]
        rewards.append(reward)
        states_actions.append(((old_pos), action))
        
        if reward == -10:  # rơi vào bẫy thì dừng
            break
        if reward == 10:  # đến đích thì dừng
            break
    
    # Tính V-value ngược
    current_v = 0
    start_pos_actions = states_actions[0] 
    for (sa, r) in zip(states_actions[::-1], rewards[::-1]):
        current_v = r + gamma*current_v
    if start_pos_actions in q_value.keys() and q_value[start_pos_actions] < current_v:
        q_value[start_pos_actions] = current_v
    elif start_pos_actions not in q_value.keys():
        q_value[start_pos_actions] = current_v
    
    print("current v-value")
    q_value_at_point = [q_value[(starts, 0)], q_value[(starts, 1)], q_value[(starts, 2)], q_value[(starts, 3)]]
    v_value_at = max(q_value_at_point)
    print(f"v_value_at state {starts}")
    
print("Q-value:")
for k in q_value:
    print(k, ":", q_value[k])