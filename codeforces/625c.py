n, k = map(int, raw_input().split())

table = [[0 for _ in range(n)] for _ in range(n)]
cur = 1

for r in range(n):
    for c in range(k - 1):
        table[r][c] = cur
        cur += 1

for r in range(n):
    for c in range(k - 1, n):
        table[r][c] = cur
        cur += 1

column_sum = sum(table[r][k - 1] for r in range(n))
print column_sum

for row in table:
    print ' '.join(str(e) for e in row)
