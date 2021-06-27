# Summer/Winter Coding(2019) - 멀쩡한 사각형

def solution(w, h):
    if w == 1 or h == 1:
        return (w * h) - max(w, h)
    if w == h:
        return (w * h) - w
    return (w * h) - (min(w, h) * 2)


if __name__ == "__main__":
    print(solution(8, 12))


