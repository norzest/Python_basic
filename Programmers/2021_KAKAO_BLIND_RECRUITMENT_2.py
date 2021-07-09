# 2021 KAKAO BLIND RECRUITMENT - 메뉴 리뉴얼

def solution(orders, course):
    answer = []
    dict = {}

    for i in orders:
        print(i)
        for j in course:
            for k in range(len(i) - j + 1):
                if i[k:k+j] in dict:
                    dict[i[k:k + j]] += 1
                else:
                    dict[i[k:k + j]] = 1
        print('---')

    print(dict)
    return answer


if __name__ == "__main__":
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
    print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))
