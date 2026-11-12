graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}
h = {'A': 6, 'B': 4, 'C': 2, 'D': 5,
     'E': 3, 'F': 1, 'G': 0}
def get_heuristic(node):
    return h[node]
def best_first_search(start, goal):
    open_list = [start]
    visited = []
    while open_list:
        open_list.sort(key=get_heuristic)
        node = open_list.pop(0)
        if node in visited:
            continue
        print(node, end=" ")
        if node == goal:
            print("\nGoal Found!")
            return
        visited.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited and neighbour not in open_list:
                open_list.append(neighbour)
    print("Goal Not Found!")
start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()
best_first_search(start, goal)