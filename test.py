# 2020 KAKAO BLIND RECRUITMENT - 자물쇠와 열쇠


def rotation(key, key_len):  # key 90도 회전
    temp = [[0] * key_len for _ in range(key_len)]
    for i in range(key_len):
        for j in range(key_len):
            temp[j][key_len-1-i] = key[i][j]
    return temp


def match(key, lock, lock_len):  # 자물쇠와 키 매칭
    count = 0

    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2):
            print(lock[i][j], end='')
        print()

    print('-----')
    return False


def solution(key, lock):
    answer = False
    key_len = len(key)
    lock_len = len(lock)

    # 자물쇠 확장
    ex_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]
    for i in range(lock_len):
        for j in range(lock_len):
            ex_lock[i + lock_len][j + lock_len] = lock[i][j]

    cnt = 0
    while cnt < 4:
        key = rotation(key, key_len)
        answer = match(key, ex_lock, lock_len)
        if answer:
            break
        cnt += 1

    return answer


if __name__ == "__main__":
    print(solution(	[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
    print(solution(	[[0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1]], [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 0]]))
