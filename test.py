# Summer/Winter Coding(~2018) - 방문 길이


def solution(dirs):
    answer = 0
    n = 10
    visited = dict()
    pointer = [5, 5]

    for d in dirs:
        temp = tuple(pointer.copy())
        if d == "U":
            pointer[0] -= 1
            if pointer[0] < 0:
                pointer[0] += 1
        elif d == "D":
            pointer[0] += 1
            if pointer[0] > n:
                pointer[0] -= 1
        elif d == "R":
            pointer[1] += 1
            if pointer[1] > n:
                pointer[1] -= 1
        elif d == "L":
            pointer[1] -= 1
            if pointer[1] < 0:
                pointer[1] += 1

        if temp in visited:
            if pointer not in visited[temp]:
                visited[temp].append(pointer.copy())
        else:
            if temp != tuple(pointer):
                visited[temp] = [pointer.copy()]

    for v in visited.values():
        answer += len(v)

    return answer


if __name__ == "__main__":
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
