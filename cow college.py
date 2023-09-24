N = 4
ci = [1, 6, 4, 6]
ci.sort()

mx = len(ci)

lst = [0] * (10)

for i in range(len(ci)):
    if not lst[ci[i]]:
        lst[ci[i]] += (mx - i) * ci[i]

max_cost = max(lst)
cost = 0
for i in range(len(lst)):
    if max_cost == lst[i]:
        cost = i
        break
print(max_cost, cost)
