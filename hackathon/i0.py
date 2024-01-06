import json


with open('level0.json', 'r') as file:
    data = json.load(file)


n = data['n_neighbourhoods']
neighbourhoods = data['neighbourhoods']
start_neighborhood = 'r0'


visited = [False] * n
path = [start_neighborhood]
current_node = int(start_neighborhood[1:])
total_distance = 0  


for _ in range(n):  
    next_node = -1
    min_dist = float('inf')

    for i in range(n):
        if not visited[i] and i != current_node:
            dist = neighbourhoods[f"n{current_node}"]['distances'][i]
            if dist < min_dist:
                min_dist = dist
                next_node = i
            elif dist == min_dist and i == 8: 
                next_node = i

    visited[next_node] = True  
    path.append(f"n{next_node}")
    total_distance += min_dist  
    current_node = next_node


path.append(start_neighborhood)
total_distance += neighbourhoods[f"n{current_node}"]['distances'][0]  


output = {"v0": {"path": path}}
print(output)
