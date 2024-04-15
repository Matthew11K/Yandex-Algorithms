n = int(input())  # Количество ягод
berries = [tuple(map(int, input().split())) for _ in range(n)]  # Параметры ягод

# Разделяем ягоды на "хорошие" и "плохие", сохраняя индекс
good_berries = [(a,b, i) for i, (a, b) in enumerate(berries) if a > b]
bad_berries = [(a,b, i) for i, (a, b) in enumerate(berries) if a <= b]

# Сортируем "хорошие" ягоды по a, а "плохие" — также по a
good_berries.sort(key=lambda x: x[1])
bad_berries.sort(key=lambda x: x[0])
#print(bad_berries)
order = []  # Порядок ягод
height = 0  # Текущая высота
max_height = 0  # Максимальная высота
nel=len(good_berries)
# Используем "хорошие" ягоды, кроме одной с наибольшим a
for a, b, index in good_berries:
    height += a
    max_height = max(max_height, height)
    height-=b
    order.append(index+1)
bad_berries.sort(key=lambda x: x[0], reverse=True)
for a, b, index in bad_berries:
    height += a
    max_height = max(max_height, height)
    height -= b
    order.append(index + 1)

print(max_height)
print(' '.join(map(str, order)))
