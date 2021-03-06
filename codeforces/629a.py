CHOCOLATE = 'C'


def total_pairs(cake):
    total = 0

    for row in cake:
        total += num_pairs(row.count(CHOCOLATE))

    for c in range(len(cake)):
        total += num_pairs(sum(row[c] == CHOCOLATE for row in cake))

    return total


def num_pairs(num):
    return sum(num - i - 1 for i in range(num - 1))


n = int(raw_input())
cake = [raw_input() for _ in range(n)]

print total_pairs(cake)
