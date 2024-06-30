def main():
    while True:
        n = input("Number of nodes: ")
        if not n.isdigit():
            print("Enter an integer number")
            continue
        elif int(n) > 26:
            print("Enter a number less than 26")
            continue
        elif int(n) < 3:
            print("You need at least 3 nodes to calculate a shortest path")
            continue
        else:
            break
    
    n = int(n)
    elements = [chr(i) for i in range(65, 65 + n)]
    
    print("Nodes: " + str(elements))
    
    graph = {node: [] for node in elements}
    print("Enter the weight for each pair")
    print("('i' for infinite weight): ")
    
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            node1 = elements[i]
            node2 = elements[j]
            while True:
                weight = input("Weight for edge " + node1 + "-" + node2 + ": ").lower()
                if weight.isdigit():
                    weight = int(weight)
                    graph[node1].append((node2, weight))
                    graph[node2].append((node1, weight))
                    break
                elif weight == 'i':
                    weight = 9999
                    graph[node1].append((node2, weight))
                    graph[node2].append((node1, weight))
                    break
                else:
                    print("Invalid input")
        
    while True:
        source = input("Choose the starting node (" + '/'.join(elements) + "): ").upper()
        if source not in elements:
            print("Please enter a valid node from " + str(elements))
            continue
        break
        
    while True:
        destination = input("Choose the destination node (" + '/'.join(elements) + "): ").upper()
        if destination not in elements:
            print("Please enter a valid node from " + str(elements))
            continue
        if source == destination:
            print("Source and destination nodes cannot be the same. Please enter different nodes.")
            continue
        break
    
    distances, shortest_path = dijkstra(graph, source)
    
    if distances[destination] >= 9999:
        print("\nFrom: " + source + " To: " + destination)
        print("Shortest Path: No path exists")
        print("Distance: infinity")
    else:
        path = " -> ".join(shortest_path[destination])
        distance = distances[destination]
        print("\nFrom: " + source + " To: " + destination)
        print("Shortest Path: " + path)
        print("Distance: " + str(distance))

def dijkstra(graph, start):
    shortest_path = {node: [] for node in graph}
    shortest_path[start] = [start]
    
    unvisited_nodes = set(graph)
    shortest_distances = {node: 9999 for node in graph}
    shortest_distances[start] = 0
    
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: shortest_distances[node])
        
        unvisited_nodes.remove(current_node)
        
        for neighbor, weight in graph[current_node]:
            if weight >= 9999:
                continue
            
            distance = shortest_distances[current_node] + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                shortest_path[neighbor] = shortest_path[current_node] + [neighbor]
    
    return shortest_distances, shortest_path

main()
