# 위클리 챌린지 7주차 - 입실 퇴실


def solution(enter, leave):
    n = len(enter)
    # ex) 3명일 경우 각 1번 2번 3번이 마주친 사람을 저장
    answer = [0] * n
    # 현재 입실하거나 퇴실할 사람을 나타내는 변수
    enter_idx, leave_idx = 0, 0
    # 현재 방에 있는 사람
    room = set()

    # 최대한 입실하자마자 퇴실하는 경우를 가정
    # 전부 퇴실할 때까지 반복
    while leave_idx < n:
        # 퇴실할 경우
        if leave[leave_idx] in room:
            # 퇴실한 인원 제거
            room.remove(leave[leave_idx])
            leave_idx += 1
            continue
        # 입실할 경우
        if enter[enter_idx] not in room:
            # 방에 있던 사람이 입실한 사람과 마주침
            for i in room:
                answer[i - 1] += 1
            # 입실한 사람이 방에 있던 사람들과 마주침
            answer[enter[enter_idx] - 1] = len(room)
            # 입실한 인원 제거
            room.add(enter[enter_idx])
            enter_idx += 1

    return answer


if __name__ == "__main__":
    print(solution([1, 3, 2], [1, 2, 3]))
    print(solution([1, 4, 2, 3], [2, 1, 3, 4]))
    print(solution([3, 2, 1], [2, 1, 3]))
    print(solution([3, 2, 1], [1, 3, 2]))
    print(solution([1, 4, 2, 3], [2, 1, 4, 3]))
