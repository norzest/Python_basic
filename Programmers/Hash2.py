# 해시 - 전화번호 목록

def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if phone_book[j].startswith(phone_book[i]) and i != j:
                return False
    return True


if __name__ == "__main__":
    a = input().strip('[]')
    a = a.replace('"', '').replace(' ', '').split(',')

    print(solution(a))