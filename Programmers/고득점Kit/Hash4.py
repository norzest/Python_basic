# 해시 - 베스트앨범

def solution(genres, plays):
    album = dict()
    len_genres = len(genres)
    for i in genres:
        if i not in album:
            album[i] = sum([plays[j] for j in range(len_genres) if i == genres[j]])

    answer = []
    while album:
        maximum = max(album, key=album.get)
        temp = [plays[i] for i in range(len_genres) if genres[i] == maximum]
        temp.sort(reverse=True)

        for i in range(2):
            try:
                for j in range(len(plays)):
                    if plays.index(temp[i], j) not in answer:
                        answer.append(plays.index(temp[i], j))
                        break
            except IndexError:
                pass

        del album[maximum]

    return answer


if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
    print(solution(["pop", "pop"], [500, 500]))