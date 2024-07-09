def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    def find(v):
        if parents[v] == v:
            return v
        parents[v] = find(parents[v])
        return parents[v]

    def union(r1, r2):
        r1 = find(r1)
        r2 = find(r2)

        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    for r1, r2, cost in costs:

        if find(r1) != find(r2):
            union(r1, r2)
            answer += cost

    return answer


if __name__ == "__main__":
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
