'''Question:- Given a (directed/undirected) graph, design an algorithm and implement it using a program to 
              find if a path exists between two given vertices or not. (Hint: use DFS)'''

def dfs(graph, current, destination, visited):

    if current == destination:
        return True

    visited[current] = True

    for neighbor in range(len(graph)):
        if graph[current][neighbor] == 1 and not visited[neighbor]:
            if dfs(graph, neighbor, destination, visited):
                return True

    return False


# INPUT
V = int(input())

graph = []
for _ in range(V):
    graph.append(list(map(int, input().split())))

source = int(input())
destination = int(input())

visited = [False] * V

if dfs(graph, source, destination, visited):
    print("Yes Path Exists")
else:
    print("No Such Path Exists")

    