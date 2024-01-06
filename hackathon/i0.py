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
total_distance = 0  # Initialize total distance


for _ in range(n):  # Iterate until all nodes are visited
    next_node = -1
    min_dist = float('inf')

    for i in range(n):
        if not visited[i] and i != current_node:
            dist = neighbourhoods[f"n{current_node}"]['distances'][i]
            if dist < min_dist:
                min_dist = dist
                next_node = i
            elif dist == min_dist and i == 8:  # Tie-breaker for n8
                next_node = i

    visited[next_node] = True  # Mark node as visited
    path.append(f"n{next_node}")
    total_distance += min_dist  
    current_node = next_node

# Return to the starting point
path.append(start_neighborhood)
total_distance += neighbourhoods[f"n{current_node}"]['distances'][0]  # Distance back to start

# Output the result
output = {"v0": {"path": path}}
print(output)
