graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}
h = {'A': 6, 'B': 4, 'C': 5, 'D': 3,
     'E': 2, 'F': 1, 'G': 0}
def hill_climbing(start, goal):
    current = start
    print(current, end=" ")
    while current != goal:
        neighbours = graph[current]
        if not neighbours:
            print("\nGoal Not Found!")
            return
        best = min(neighbours, key=lambda node: h[node])
        if h[best] >= h[current]:
            print("\nGoal Not Found!")
            return
        current = best
        print(current, end=" ")
    print("\nGoal Found!")
hill_climbing('A', 'G')