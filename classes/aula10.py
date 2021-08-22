from datetime import date, time, datetime, timedelta

current_date = date.today()


def show_current_date():
    month = current_date.today().strftime("%B")
    day = current_date.today().strftime("%d")
    year = current_date.today().strftime("%Y")

    print("Today is {month} {day} of {year}".format(month=month, day=day, year=year))


def show_time(hour, minute, second):
    given_time = time(hour, minute, second)
    print("The given time is: {}".format(given_time))


def show_date_time():
    current_datetime = datetime.now()
    print(current_datetime.strftime("Today is %B %d of %Y, at %H:%M:%S."))
    print(current_datetime.strftime("In other words, today is %c."))


def say_weekday_in_portuguese(weekday):
    weekdays_ptbr = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")
    print("Welcome to {weekday} ! 🇧🇷".format(weekday=weekdays_ptbr[weekday]))


def print_datetime_as_locale_representation(given_datetime):
    print(given_datetime.strftime("The converted given date would look something like: %c."))


def convert_string_to_datetime(given_date, current_pattern):
    converted_date = datetime.strptime(given_date, current_pattern)
    return converted_date


def increase_date_in_days(given_date, days):
    increased = given_date + timedelta(days=days)
    return increased


def decrease_date_in_days(given_date, days):
    decreased = given_date - timedelta(days=days)
    return decreased


def increase_or_decrease_date(option, given_date, days, hours, minutes):
    if option == "increase":
        return given_date + timedelta(days=days, hours=hours, minutes=minutes)
    elif option == "decrease":
        return given_date - timedelta(days=days, hours=hours, minutes=minutes)
    else:
        return "invalid option, try again!"


if __name__ == "__main__":
    show_current_date()
    show_time(22, 51, 30)
    show_date_time()
    say_weekday_in_portuguese(datetime.now().weekday())
    print_datetime_as_locale_representation(datetime(21, 8, 19, 23, 26, 0))
    converted_datetime = convert_string_to_datetime("19/08/21 23:34:00", "%d/%m/%y %H:%M:%S")
    print("The time of the converted_datetime object is: {}".format(converted_datetime))

    increased_date = increase_date_in_days(converted_datetime, 365)
    print("\nThe increased date is: {}".format(increased_date))

    decreased_date = decrease_date_in_days(converted_datetime, 365 * 2)
    print("The decreased date is {}".format(decreased_date))

    new_date = increase_or_decrease_date("increase", converted_datetime, 31, 0, 26)
    print("The new date is: {}".format(new_date))
