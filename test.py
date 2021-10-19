# 2020 KAKAO BLIND RECRUITMENT - 자물쇠와 열쇠


def solution(key, lock):
    def check(l):  # 키가 맞는지 확인
        n = len(l) // 3

        for i in range(n, n * 2):
            for j in range(n, n * 2):
                if l[i][j] != 1:
                    return False
        return True

    # 자물쇠 확장
    lock_len = len(lock)
    ex_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]
    for i in range(lock_len):
        for j in range(lock_len):
            ex_lock[i + lock_len][j + lock_len] = lock[i][j]

    for k in key:
        print(k)
    print('---')
    for l in ex_lock:
        print(l)

    answer = check(ex_lock)
    return answer


if __name__ == "__main__":
    print(solution(	[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
