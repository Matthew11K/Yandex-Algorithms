def min_points_for_square(points):
    point_set = set(points)  # Преобразование списка точек в множество для быстрого поиска
    added_points = set()  # Множество для хранения добавленных точек

    for A in points:
        for B in points:
            if A == B:
                continue

            # Вычисление координат потенциальных вершин C и D квадрата
            C = (B[0] + (A[1] - B[1]), B[1] - (A[0] - B[0]))
            D = (A[0] + (A[1] - B[1]), A[1] - (A[0] - B[0]))

            # Проверка, присутствуют ли C и D в исходном множестве точек
            if C in point_set and D in point_set:
                # Квадрат уже существует, добавлять точки не нужно
                return 0, []

            # Если одна из точек отсутствует, добавляем её
            if C not in point_set:
                added_points.add(C)
            if D not in point_set:
                added_points.add(D)

            # Если найдено достаточно точек для формирования хотя бы одного квадрата, прерываем цикл
            if len(added_points) >= 4:
                break

    return len(added_points), list(added_points)

# Пример ввода
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Решение задачи
k, added_points = min_points_for_square(points)
print(k)
for point in added_points:
    print(*point)
