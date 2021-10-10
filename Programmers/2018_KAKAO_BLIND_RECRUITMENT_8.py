# 2018 KAKAO BLIND RECRUITMENT - 파일명 정렬


def solution(files):
    answer = []

    for file in files:
        head, number, tail = '', '', ''

        number_check = False

        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                number_check = True
            elif not number_check:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(a) for a in answer]


if __name__ == "__main__":
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
