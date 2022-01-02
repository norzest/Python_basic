# 1436 영화감독 숌


def solution():
    n = int(input())

    name = 666
    cnt = 0

    while True:
        if "666" in str(name):
            cnt += 1
            if cnt == n:
                print(name)
                break

        name += 1


if __name__ == '__main__':
    solution()
