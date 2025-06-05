import datetime
date_now = datetime.datetime.today()
print(date_now)

def get_days_from_today(today, some_date):
    difference = today - some_date
    return difference.days

some_date = "2026.10.10"
python_format_date = datetime.datetime.strptime(some_date, "%Y.%m.%d")

print(get_days_from_today(date_now, python_format_date), "days")
