# 2018 KAKAO BLIND RECRUITMENT - 파일명 정렬


def solution(files):
    answer = []
    for file in files:
        file = file.lower()
        print(file)

    return answer


if __name__ == "__main__":
    print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
    print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
