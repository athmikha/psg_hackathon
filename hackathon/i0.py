import json

# Read data from the JSON file
with open('level0.json', 'r') as file:
    data = json.load(file)

# Extract data
n = data['n_neighbourhoods']
neighbourhoods = data['neighbourhoods']
start_neighborhood = 'r0'

# Initialize variables
visited = [False] * n
path = [start_neighborhood]
current_node = int(start_neighborhood[1:])

# Greedy heuristic algorithm
for _ in range(n - 1):
    next_node = -1
    min_dist = float('inf')

    for i in range(n):
        if not visited[i] and i != current_node:
            dist = neighbourhoods[f"n{current_node}"]['distances'][i]
            if dist < min_dist:
                min_dist = dist
                next_node = i

    visited[next_node] = True
    path.append(f"n{next_node}")
    current_node = next_node

# Return to the starting point
path.append(start_neighborhood)

# Output the result
output = {"v0": {"path": path}}
print(output)
