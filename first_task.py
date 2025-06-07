import datetime

def get_days_from_today(some_date):
    try:
        date_now = datetime.datetime.today()
        python_format_date = datetime.datetime.strptime(some_date, "%Y-%m-%d")
        difference = date_now - python_format_date
        return difference.days
    except:
        return "Incorrect type of data, please use YY-MM-DD format"

some_date = "2026.10.10"


print(get_days_from_today(some_date), "days")
