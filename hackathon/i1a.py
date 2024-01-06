import json


def calculate_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance


def find_optimal_paths(neighbourhoods, vehicle_capacity, distances):
    
    sorted_neighbourhoods = sorted(neighbourhoods.items(), key=lambda x: x[1]['order_quantity'], reverse=True)

    vehicle_paths = []
    current_capacity = 0
    current_path = ['r0']  

    for neighborhood, data in sorted_neighbourhoods:
        current_capacity += data['order_quantity']
        current_path.append(neighborhood)

        if current_capacity >= vehicle_capacity:
            current_path.append('r0') 
            vehicle_paths.append(current_path)
            current_path = ['r0']
            current_capacity = 0

   
    if len(current_path) > 1:
        current_path.append('r0')
        vehicle_paths.append(current_path)

    paths = {f"v{i}": {"path": vehicle_paths[i]} for i in range(len(vehicle_paths))}
    return paths


with open('level1a.json', 'r') as file:
    input_data = json.load(file)

neighbourhoods = input_data['neighbourhoods']
vehicle_capacity = input_data['vehicles']['v0']['capacity']
distances = {neighborhood: neighbourhoods[neighborhood]['distances'] for neighborhood in neighbourhoods}

optimal_paths = find_optimal_paths(neighbourhoods, vehicle_capacity, distances)
print(json.dumps(optimal_paths, indent=2))
