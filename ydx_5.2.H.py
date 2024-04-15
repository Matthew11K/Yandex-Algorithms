n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

max_value = max(map(max, matrix))
max_positions = [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == max_value]

scenario_results = []

for max_pos in max_positions:
    row_excluded = max_pos[0]
    remaining_max_after_row_exclusion = 0
    for j in range(m):
        column_max = max(matrix[i][j] for i in range(n) if i != row_excluded)
        if column_max > remaining_max_after_row_exclusion:
            remaining_max_after_row_exclusion = column_max
            column_to_exclude_after_row = j

    # Сценарий 2: Исключаем столбец с максимальным значением
    column_excluded = max_pos[1]
    remaining_max_after_column_exclusion = 0
    for i in range(n):
        row_max = max(matrix[i][j] for j in range(m) if j != column_excluded)
        if row_max > remaining_max_after_column_exclusion:
            remaining_max_after_column_exclusion = row_max
            row_to_exclude_after_column = i
# Выбираем наименьшую оставшуюся максимальную силу из двух сценариев
    if remaining_max_after_row_exclusion <= remaining_max_after_column_exclusion:
        # Исключаем строку
        scenario_results.append((remaining_max_after_row_exclusion, row_excluded, column_excluded))
    else:
        # Исключаем столбец
        scenario_results.append((remaining_max_after_column_exclusion, row_excluded, column_excluded))

print(scenario_results)
# Из всех сценариев выбираем тот, который имеет наименьшую оставшуюся максимальную силу
best_scenario = min(scenario_results, key=lambda x: x[0])
best_race, best_class = best_scenario[1:]

# Выводим результат, индексы увеличены на 1 для соответствия заданию
print(best_race + 1, best_class + 1)
