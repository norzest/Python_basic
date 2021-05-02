# 완전탐색 - 카펫

def solution(brown, yellow):
    temp = [i for i in range(1, yellow+1) if yellow % i == 0]

    left = 0
    right = len(temp) - 1
    while right >= left:
        if ((temp[left] + 2) * (temp[right] + 2)) - (temp[left] * temp[right]) == brown:
            return [temp[right] + 2, temp[left] + 2]

        left += 1
        right -= 1


if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))