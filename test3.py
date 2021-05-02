def solution(tickets):
    edge = dict()
    count = 0
    for a, b in sorted(tickets, key=lambda x: x[1]):
        if a not in edge:
            edge[a] = count
            count += 1
        if b not in edge:
            edge[b] = count
            count += 1

    graph = [[edge[a], edge[b]] for a, b in tickets]

    print(graph)
    answer = []

    return answer


if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))


