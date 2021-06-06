# Summer/Winter Coding(~2018) - 예산

def solution(d, budget):
    d.sort()

    temp = 0
    d_len = len(d)
    for i in range(d_len):
        temp += d[i]
        if temp > budget:
            return i
    else:
        return d_len


if __name__ == "__main__":
    print(solution([1, 3, 2, 5, 4], 9))
    print(solution([2, 2, 3, 3], 10))


