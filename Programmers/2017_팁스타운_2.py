# 2017 팁스타운 - 예상 대진표

def solution(n, a, b):
    def bs(le, num):
        right = le
        left = 1
        count = 1
        while left <= right:
            mid = (right + left) // 2
            #print(mid, end=' ')
            if mid == num:
                break

            if mid > num:
                right = mid - 1

            if mid < num:
                left = mid + 1

            count += 1
        #print()
        return count

    x, y = bs(n, a), bs(n, b)
    print(x, y)

    return max(x, y)


if __name__ == "__main__":
    print(solution(8, 4, 7))
    print('---')
    print(solution(256, 46, 243))
    print('---')
    print(solution(2, 2, 1))
    print('---')
    print(solution(16, 14, 16))

