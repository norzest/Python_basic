# 2020 카카오 인턴십 - 키패드 누르기

def solution(numbers, hand):
    key_pad = [  # 리스트 변수들의 위치를 참고하기 위한 변수 (사용 x)
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]

    finger_left = [3, 0]  # * 시작
    finger_right = [3, 2]  # # 시작
    answer = []

    for number in numbers:
        if number in (1, 4, 7):
            answer.append('L')
            finger_left = [number // 3, 0]  # 왼손의 위치 변경
        if number in (3, 6, 9):
            answer.append('R')
            finger_right = [number // 3 - 1, 2]  # 오른손의 위치 변경
        if number in (2, 5, 8, 0):
            num_loc = [3, 1] if number == 0 else [number // 3, 1]  # 입력할 숫자의 키패드상 위치
            #  왼손과 입력할 수 사이의 거리
            left_distance = (max(num_loc[0], finger_left[0]) - min(num_loc[0], finger_left[0])) + \
                            (max(num_loc[1], finger_left[1]) - min(num_loc[1], finger_left[1]))
            #  오른손과 입력할 수 사이의 거리
            right_distance = (max(num_loc[0], finger_right[0]) - min(num_loc[0], finger_right[0])) + \
                             (max(num_loc[1], finger_right[1]) - min(num_loc[1], finger_right[1]))

            if left_distance < right_distance:
                answer.append('L')
                finger_left = num_loc
            elif right_distance < left_distance:
                answer.append('R')
                finger_right = num_loc
            else:
                if hand == "left":
                    answer.append('L')
                    finger_left = num_loc
                else:
                    answer.append('R')
                    finger_right = num_loc

    return ''.join(answer)


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print('-------------')
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print('-------------')
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
    print('-------------')