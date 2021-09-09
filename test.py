# 2018 KAKAO BLIND RECRUITMENT - 캐시

def solution(cacheSize, cities):
    # 캐시 사이즈가 0일 경우
    if cacheSize == 0:
        return len(cities) * 5
    
    # 대소문자 구분 x이니 전부 소문자 화
    cities = [c.lower() for c in cities]
    # 첫 번째는 무조건 cache miss 이니 미리 계산
    answer = 5
    cache = [cities[0]]

    for city in cities[1:]:
        # cache hit
        if city in cache:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
        # cache miss
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.pop(0)
                cache.append(city)

    return answer


if __name__ == "__main__":
    print(solution(	3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
