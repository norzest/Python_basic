# Summer/Winter Coding(~2018) - 소수 만들기

def solution(nums):
    array = []
    nums_len = len(nums)
    for a in range(nums_len):
        for b in range(a+1, nums_len):
            for c in range(b+1, nums_len):
                array.append(nums[a] + nums[b] + nums[c])

    print(array)

    answer = -1
    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 4]))
    print(solution([1, 2, 7, 6, 4]))


