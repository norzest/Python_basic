# 그리디 - 단속카메라

def solution(routes):
    routes.sort(key=lambda x: x[1])
    point = routes[0][1]
    answer = 1

    for a, b in routes:
        if a > point:
            answer += 1
            point = b

    return answer


if __name__ == "__main__":
    print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
