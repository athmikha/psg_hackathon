import json
def calculate_distance(path, distances):
  
  total_distance = 0
  for i in range(len(path) - 1):
    total_distance += distances[path[i]][path[i + 1]]
  return total_distance

def find_optimal_paths(neighbourhoods, vehicle_capacity, distances):

  sorted_neighbourhoods = sorted(neighbourhoods.items(), key=lambda x: x[1]['order_quantity'], reverse=True)

  current_capacity = 0
  current_path = ['r0'] 
  paths = {"v0": {}}

  for neighborhood, data in sorted_neighbourhoods:
    
    if current_capacity + data['order_quantity'] > vehicle_capacity:
      
      current_path.append('r0')
      paths["v0"]["path" + str(len(paths["v0"]) + 1)] = current_path
      current_path = ['r0']
      print(current_capacity,"curr")
      current_capacity = 0
    current_capacity += data['order_quantity']
    current_path.append(neighborhood)
    
  if len(current_path) > 1:
    current_path.append('r0')
    paths["v0"]["path" + str(len(paths["v0"]) + 1)] = current_path

  return paths

input_data = json.load(open('level1a.json'))
neighbourhoods = input_data['neighbourhoods']
vehicle_capacity = input_data['vehicles']['v0']['capacity']
distances = {neighborhood: neighbourhoods[neighborhood]['distances'] for neighborhood in neighbourhoods}

optimal_paths = find_optimal_paths(neighbourhoods, vehicle_capacity, distances)


print(json.dumps(optimal_paths, indent=3))
