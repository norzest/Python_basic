# Summer/Winter Coding(~2018) - 스킬트리


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        stack = []

        for s in skill_tree:
            # 선행스킬이 있는 경우 스택에 추가
            if s in skill:
                stack.append(s)

        for i in range(len(stack)):
            # 선행스킬 순서와 다르면 break
            if stack[i] != skill[i]:
                break
        else:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
