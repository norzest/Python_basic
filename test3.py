INF = int(1e9)
distance = [INF] * (4+1)


def dijkstra(start):
    distance[start] = 0


    return distance

print(distance)
print(dijkstra(3))
print(distance)
print(dijkstra(2))
print(distance)
