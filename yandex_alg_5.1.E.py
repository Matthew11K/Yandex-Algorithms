def find_profit(n, k, d):
    stack = [(n, 1)]

    while stack:
        num, day = stack.pop()

        if day == d + 1:
            if num % k == 0:
                return num
            continue

        remainder = num % k
        for digit in range(10):
            next_remainder = (remainder * 10 + digit) % k
            if next_remainder == 0:
                stack.append((num * 10 + digit, day + 1))

    return -1

n, k, d = map(int, input().split())
result = find_profit(n, k, d)
print(result)
