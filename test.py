def solution(distance, rocks, n):
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    arr = [rocks[i+1] - rocks[i] for i in range(len(rocks) - 1)]

    print(rocks, arr)
    answer = 0
    return answer


if __name__ == "__main__":
    print(solution(25, [2, 14, 11, 21, 17], 2))



