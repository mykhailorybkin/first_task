import datetime



def get_days_from_today(some_date):
    date_now = datetime.datetime.today()
    python_format_date = datetime.datetime.strptime(some_date, "%Y.%m.%d")
    difference = date_now - python_format_date
    return difference.days

some_date = "2026.10.10"


print(get_days_from_today(some_date), "days")
