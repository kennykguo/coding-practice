# Problem statement: README.md   |   Run tests: python3 test.py


def find_endpoint(edges: list[list[int]], start: int) -> int:
    
    visited = set()

    current_node = start

    adj = {}

    for i,j in edges:
        if i not in adj:
            adj[i] = []
        adj[i].append(j)

    # print(adj)

    while current_node not in visited:
        # print(current_node)
        visited.add(current_node)

        if current_node not in adj:
            return current_node # found the end
        
        next_node = adj[current_node][0]

        if next_node in visited:
            return current_node
        
        current_node = next_node

    return current_node

    
