from datetime import datetime, timedelta


def workdays_and_holidays(N, year, holidays, first_day_of_year):
    month_to_num = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    holidays_datetime = []
    for day, month in holidays:
        holidays_datetime.append(datetime(year, month_to_num[month], day))

    first_day_index = days_of_week.index(first_day_of_year)

    day_counts = [0 for _ in range(7)]
    for i in range(365 + (1 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 0)):
        day_counts[(first_day_index + i) % 7] += 1

    for holiday in holidays_datetime:
        day_counts[holiday.weekday()] -= 1

    max_days_off = max(day_counts)
    min_days_off = min(day_counts)
    best_days = [days_of_week[i] for i, count in enumerate(day_counts) if count == max_days_off]
    worst_days = [days_of_week[i] for i, count in enumerate(day_counts) if count == min_days_off]

    return best_days, worst_days


def calculate_best_and_worst_weekday():
    N = int(input())
    year = int(input())
    holidays = []
    for _ in range(N):
        day, month = input().split()
        holidays.append((int(day), month))

    first_day_of_year = input()

    best_days, worst_days = workdays_and_holidays(N, year, holidays, first_day_of_year)


    print(best_days[0])
    print(worst_days[0])


calculate_best_and_worst_weekday()
