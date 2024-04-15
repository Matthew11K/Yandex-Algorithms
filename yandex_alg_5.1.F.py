def solve(n, numbers):
    is_odd = lambda x: x % 2 != 0

    operations = ""

    if n == 2:
        if is_odd(numbers[0] + numbers[1]) or is_odd(numbers[0] * numbers[1]):
            operations = "+" if is_odd(numbers[0] + numbers[1]) else "x"
        return operations

    first_odd_index = -1
    for i, num in enumerate(numbers):
        if is_odd(num):
            first_odd_index = i
            break

    if first_odd_index == 0 or is_odd(numbers[0] + numbers[1]) or is_odd(numbers[0] * numbers[1]):
        if is_odd(numbers[0] + numbers[1]):
            operations += "+"
        elif is_odd(numbers[0] * numbers[1]):
            operations += "x"
        for i in range(2, n):
            if is_odd(numbers[i]):
                operations += "x"
            else:
                operations += "+"
    else:
        for i in range(first_odd_index):
            operations += "+"
        for i in range(first_odd_index, n - 1):
            if is_odd(numbers[i + 1]):
                operations += "x"
            else:
                operations += "+"

    return operations[:n - 1]

n = int(input())
nums = list(map(int, input().split()))

print(solve(n, nums))
