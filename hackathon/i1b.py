import json 
def find_routes_recursive(input_data, current_node, current_capacity, path, paths):
    neighborhoods = input_data['neighbourhoods']
    max_capacity = input_data['vehicles']['v0']['capacity']

    if current_node == 'r0' and len(path) > 1:
        paths.append(path)
        return

    if current_capacity < 0 or current_node in path:
        return

    path.append(current_node)

    for neighbor in neighborhoods[current_node]['distances']:
        next_node = 'n' + str(neighbor)
        if neighbor < 50:
            order_quantity = neighborhoods[next_node]['order_quantity']
            print(order_quantity)

        if next_node not in path and current_capacity - order_quantity >= 0:
            find_routes_recursive(input_data, next_node, current_capacity - order_quantity, path[:], paths)
    
    return paths

def find_routes(input_data):
    start_point = input_data['restaurants']['r0']['neighbourhood_distance']
    paths = []

    for i in range(len(start_point)):
        current_capacity = input_data['vehicles']['v0']['capacity']
        paths = find_routes_recursive(input_data, 'n' + str(i), current_capacity, [], paths)

    return {'v0': {'path' + str(idx): path for idx, path in enumerate(paths)}}

# Read input data from file
with open('level1b.json', 'r') as file:
    input_data = json.load(file)

# Get routes for expansion
output = find_routes(input_data)
print(output)
