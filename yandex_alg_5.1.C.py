def calculate_presses(spaces):
    if spaces == 0:
        return 0
    elif spaces == 1:
        return 1
    elif spaces == 2:
        return 2
    elif spaces == 3:
        return 2
    else:
        tabs = spaces // 4
        remaining_spaces = spaces % 4

        if remaining_spaces == 3:
            return tabs + 2
        else:
            return tabs + remaining_spaces



n = int(input())

total_presses = 0
for _ in range(n):
    spaces = int(input())
    total_presses += calculate_presses(spaces)

print(total_presses)
