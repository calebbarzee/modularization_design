# 1. Name:
#      Caleb Barzee
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program gets a month and year from the user. It then displays the month requested.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


from operator import truediv


def display_month(day_of_week, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(day_of_week) == type(0))
    assert(0 <= day_of_week <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(day_of_week):
        print("    ", end='')

    # Display the days of the month
    for days_of_month in range(1, num_days + 1):
        print(repr(days_of_month).rjust(4), end='')
        day_of_week += 1
        # Newline after Saturdays
        if day_of_week % 7 == 0:
            print("")  # newline

    # We must end with a newline
    if day_of_week % 7 != 0:
        print("")  # newline


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def get_days_of_month(month, year):
    match month:
        case 1:
            return 31
        case 3:
            return 31
        case 5:
            return 31
        case 7:
            return 31
        case 8:
            return 31
        case 10:
            return 31
        case 12:
            return 31
        case 4:
            return 30
        case 6:
            return 30
        case 9:
            return 30
        case 11:
            return 30
        case 2:
            if is_leap_year(year):
                return 29
            else:
                return 28


def get_day_of_week(month, year):
    # SET year_diff = year - 1753
    # IF year_diff > 0:
    # SET leap_years = 0
    # FOR i IN range(year_diff):
    # IF is_leap_year(1753_i)
    # leap_years ++
    # normal_years = year_diff - leap_years
    # years_to_days = normal_years*365 + leap_years*366
    # IF month > 1:
    # SET months_to_days = 0
    # FOR i IN range(month):
    # months_to_days += get_days_of_month(i)
    # day_of_week = (years_to_days + months_to_days) % 7
    # return day_of_week
    year_diff = year - 1753
    day_of_week = 1
    if year_diff > 0:
        leap_years = 0
        for i in range(year_diff):
            if is_leap_year(1753 - i):
                leap_years += 1
        normal_years = year_diff - leap_years
        years_to_days = normal_years*365 + leap_years*366
        months_to_days = 0
        if month > 1:
            for i in range(month):
                current_month = get_days_of_month(i, year)
                months_to_days += current_month
        day_of_week = (years_to_days + months_to_days) % 7
        match day_of_week:
            case 0:
                day_of_week = 1
            case 1:
                day_of_week = 2
            case 2:
                day_of_week = 3
            case 3:
                day_of_week = 4
            case 4:
                day_of_week = 5
            case 5:
                day_of_week = 6
            case 6:
                day_of_week = 0
    return day_of_week


def main():
    month = 0
    reenter = True
    while reenter:
        month = int(input("Please enter the desired month (1-12): "))
        if 1 <= month <= 12:
            reenter = False
    year = 0
    while year < 1753:
        year = int(input("Please enter the desired year (1753+): "))
    days_of_month = get_days_of_month(month, year)
    day_of_week = get_day_of_week(month, year)
    display_month(day_of_week, days_of_month)


if __name__ == "__main__":
    main()
