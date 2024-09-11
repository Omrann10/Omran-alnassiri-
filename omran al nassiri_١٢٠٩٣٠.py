def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path)
            if result:
                return result
    
    path.pop()
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
path = dfs(graph, start, goal)
print(" the depth path :", path)