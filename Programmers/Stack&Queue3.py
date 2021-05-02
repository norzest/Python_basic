# 스택/큐 - 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    going = []
    time = []
    answer = 1
    while truck_weights or going:
        if truck_weights and sum(going) + truck_weights[0] <= weight:
            going.append(truck_weights.pop(0))
            time.append(0)

        time = [i+1 for i in time]

        if time[0] == bridge_length:
            time.pop(0)
            going.pop(0)

        answer += 1

    return answer


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
    print('-------------')
    print(solution(100, 100, [10]))
    print('-------------')
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    print('-------------')