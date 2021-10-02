# 해시 - 위장

def solution(clothes):
    kinds = dict()
    answer = 1

    for a, b in clothes:
        if b not in kinds.keys():
            kinds[b] = 2  # 안입는 것과 입는 것 2종류
        else:
            kinds[b] += 1

    for i in kinds:
        answer *= kinds[i] + 1

    return answer - 1


if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print('-------------')
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
    print('-------------')