def bfs(d, n):
    vi = []  # List to keep track of visited nodes
    q = [n]  # Queue to manage the nodes to visit

    while q:
        node = q.pop(0)  # Dequeue a node
        if node not in vi:
            vi.append(node)  # Mark the node as visited
            print(node)  # Print the node (or process it as needed)

            # Enqueue all adjacent nodes that have not been visited
            for neighbor in d[node]:
                if neighbor not in q and neighbor not in vi:
                    q.append(neighbor)

# Define the graph as a dictionary
d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}

# Perform BFS starting from node 5
bfs(d, 5)