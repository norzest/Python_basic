# DFS/BFS - 단어 변환  <------ BFS 사용 나중에 보기

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [0 for _ in words]
    stacks = [begin]
    count = 0

    while stacks:
        stack = stacks.pop()

        if stack == target:
            return count

        for i in range(len(words)):
            temp = [x for x in range(len(words[i])) if words[i][x] != stack[x]]
            if len(temp) == 1:
                if visited[i] == 0:
                    visited[i] = 1
                    stacks.append(words[i])

        count += 1

    return 0


if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
    print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
    print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"]), 3)