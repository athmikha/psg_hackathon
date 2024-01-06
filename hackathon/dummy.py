import json

def nearest_neighbor(data):
    n = data['n_neighbourhoods']
    neighborhoods = data['neighbourhoods']
    start_neighborhood = 'r0'

    visited = [False] * n
    path = [start_neighborhood]
    current_node = int(start_neighborhood[1:])

    for _ in range(n - 1):
        next_node = -1
        min_dist = float('inf')

        for i in range(n):
            if not visited[i] and i != current_node:
                dist = neighborhoods[f"n{current_node}"]['distances'][i]
                if dist < min_dist:
                    min_dist = dist
                    next_node = i

        visited[next_node] = True
        path.append(f"n{next_node}")
        current_node = next_node

    path.append(start_neighborhood)
    return path

if __name__ == "__main__":
    # Read data from the JSON file
    with open('level0.json', 'r') as file:
        data = json.load(file)

    shortest_path = nearest_neighbor(data)

    # Output the result
    output = {"v0": {"path": shortest_path}}
    print(json.dumps(output))
