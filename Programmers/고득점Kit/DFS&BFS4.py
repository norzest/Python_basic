# DFS/BFS - 여행경로 <-- DFS 역순으로 응용

def solution(tickets):

    def create_graph():
        graph = dict()
        for a, b in tickets:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

        for i in graph:
            graph[i].sort()

        return graph

    def dfs():
        stacks = ["ICN"]
        path = []

        while stacks:
            stack = stacks[-1]

            if stack not in route or len(route[stack]) == 0:
                path.append(stacks.pop())
            else:
                stacks.append(route[stack].pop(0))
        return path[::-1]

    route = create_graph()
    answer = dfs()
    return answer


if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
    print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]))