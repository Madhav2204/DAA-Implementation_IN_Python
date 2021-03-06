def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex)
    for node in graph[vertex] :
        if node not in visited:
            dfs(graph, node, visited)

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0', '4']),
         '3': set(['1', '4']),
         '4': set(['1', '2', '3'])}

dfs(graph, '0')