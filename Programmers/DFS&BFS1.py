# DFS/BFS - 타겟 넘버

def solution(numbers, target):
    graph = [[numbers[0], -numbers[0]]]

    for x, i in enumerate(numbers[1:]):
        temp = []
        for j in graph[x]:
            temp.append(j + i)
            temp.append(j - i)

        graph.append(temp)

    answer = graph[-1].count(target)
    return answer


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print('-------------')