# 2019 KAKAO BLIND RECRUITMENT - 오픈채팅방

def solution(record):
    answer = []
    logs = [_.split() for _ in record]
    user = {log[1]: log[2] for log in logs
            if log[0] == 'Enter' or log[0] == 'Change'}

    for log in logs:
        if log[0] == 'Enter':
            answer.append(user[log[1]] + '님이 들어왔습니다.')
        if log[0] == 'Leave':
            answer.append(user[log[1]] + '님이 나갔습니다.')

    return answer


if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
                    "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
