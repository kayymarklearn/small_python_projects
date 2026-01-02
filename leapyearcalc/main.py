year = int(input("Enter the year you want to check: \n"))

def check_leap_year(leap_year):
    if leap_year % 4 != 0:
        return f"{leap_year} is not a leap year."
    else:
        if leap_year % 100 != 0:
            return f"{leap_year} is a leap year."
        else:
            if leap_year % 400 != 0:
                return f"{leap_year} is not a leap year."
            else:
                return f"{leap_year} is a leap year."

print(check_leap_year(year))
