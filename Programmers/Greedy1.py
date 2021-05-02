# 그리디 - 체육복

def solution(n, lost, reserve):
    _reserve = [_ for _ in reserve if _ not in lost]
    _lost = [_ for _ in lost if _ not in reserve]

    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i - 1)
        elif i+1 in reserve:
            _lost.remove(i + 1)

    answer = n - len(_lost)
    return answer


if __name__ == "__main__":
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))