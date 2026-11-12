graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}
h = {'A': 6, 'B': 4, 'C': 2, 'D': 5,
     'E': 3, 'F': 1, 'G': 0}
def best_first_search(start, goal):
    open_list = [start]
    visited = []
    while open_list:
        open_list.sort(key=lambda x: h[x])
        node = open_list.pop(0)
        print(node, end=" ")
        if node == goal:
            print("\nGoal Found!")
            return
        visited.append(node)
        for n in graph.get(node, []):
            if n not in visited and n not in open_list:
                open_list.append(n)

best_first_search('A', 'G')