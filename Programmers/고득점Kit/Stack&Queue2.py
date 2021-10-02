# 스택/큐 - 기능 개발

def solution(progresses, speeds):
    count = 0
    answer = []
    while len(progresses) > 0:
        if progresses[0] >= 100:
            while len(progresses) > 0 and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            answer.append(count)
            count = 0
        else:
            for j in range(len(progresses)):
                progresses[j] += speeds[j]

    return answer


if __name__ == "__main__":
    aa, bb = input().strip('[]').split('], [')
    aa = list(map(int, aa.split(',')))
    bb = list(map(int, bb.split(',')))
    print(solution(aa, bb))