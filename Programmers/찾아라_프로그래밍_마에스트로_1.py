# 찾아라 프로그래밍 마에스트로 - 폰켓몬

def solution(nums):
    nums_len = int(len(nums)/2)
    nums_set_len = len(set(nums))
    return nums_set_len if nums_set_len <= nums_len else nums_len


if __name__ == "__main__":
    print(solution([3, 1, 2, 3]))
    print(solution([3, 3, 3, 2, 2, 4]))

