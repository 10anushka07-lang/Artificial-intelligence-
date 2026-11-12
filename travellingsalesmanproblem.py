graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
def travellingsalesman():
    n = len(graph)
    visited = [False] * n
    current = 0
    total = 0
    visited[current] = True
    print("0", end=" ")
    for i in range(n - 1):
        minimum = 999
        next_city = -1
        for city in range(n):
            if not visited[city] and graph[current][city] < minimum:
                minimum = graph[current][city]
                next_city = city
        current = next_city
        visited[current] = True
        total += minimum
        print(current, end=" ")
    total += graph[current][0]
    print("0")
    print("Total Distance:", total)
travellingsalesman()