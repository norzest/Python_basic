# Summer/Winter Coding(~2018) - 영어 끝말잇기

from math import ceil


def solution(n, words):
    answer = [0, 0]
    # 차례
    turn = 1
    # 현재 사용한 단어를 담을 리스트
    stacks = []
    # 현재 단어 이전에 사용했던 단어의 마지막 알파벳
    pre_word = words[0][0]

    for word in words:
        # 만약 word 가 이미 사용한 단어이거나 이전 단어와 이어지지 않는다면
        if word in stacks or pre_word != word[0]:
            answer = [turn % n if turn % n != 0 else n, ceil(turn / n)]
            break

        pre_word = word[-1]
        stacks.append(word)
        turn += 1

    return answer


if __name__ == "__main__":
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
