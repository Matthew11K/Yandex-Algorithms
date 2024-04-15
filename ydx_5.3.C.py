def min_numbers_to_remove(n, a):
    counts = {}
    for number in a:
        counts[number] = counts.get(number, 0) + 1

    max_count = 0
    for number in counts:
        current_count = counts[number] + counts.get(number + 1, 0)
        max_count = max(max_count, current_count)

    return n - max_count

n=int(input())
digits=list(map(int,input().split()))
print(min_numbers_to_remove(n,digits))
