class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y


def count_leap_years(d):
    """ Counts number of leap years.

    Args:
        d Date(obj): Date object.

    Returns:
        int: No of years till date.
    """

    years = d.y
    if (d.m <= 2):
        years -= 1

    return int(years / 4) - int(years / 100) + int(years / 400)



def get_difference(dt1, dt2):
    """ Find the difference between the days of 2 date.

    Args:
        dt1 Date(obj): Date 1 Date object.
        dt2 Date(obj): Date 2 Date object.

    Returns:
        int: No of difference between 2 dates
    """

    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year1_days = dt1.y * 365 + dt1.d
    for i in range(0, dt1.m - 1):
        year1_days += monthDays[i]
    year1_days += count_leap_years(dt1)


    year2_days = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        year2_days += monthDays[i]
    year2_days += count_leap_years(dt2)

    return (year2_days - year1_days)



if __name__ == "__main__":
    print("Enter Date 1 : ")
    date_1 = input()
    dt1_obj = Date(int(date_1[6:]), int(date_1[4:6]), int(date_1[:4]))

    print("Enter Date 2 : ")
    date_2 = input()
    dt2_obj = Date(int(date_2[6:]), int(date_2[4:6]), int(date_2[:4]))

    print(get_difference(dt1_obj, dt2_obj), "days")
