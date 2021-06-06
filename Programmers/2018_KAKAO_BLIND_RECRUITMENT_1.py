# 2018 KAKAO BLIND RECRUITMENT - [1차]비밀지도

def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        temp = '{0:0>{1}}'.format(bin(i | j)[2:], n)
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')

        answer.append(temp)

    return answer


if __name__ == "__main__":
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))

