import datetime as dt
print(dt.date.today() - dt.timedelta(5))


# first_date = dt.date(2020, 10, 2)
# second_date = dt.date(2020, 10, 7)
# days_5 = dt.timedelta(5, 0, 0, 0, 0, 0, 0)
# delta = second_date - first_date
# print(delta)
# print(dt.date.today() - delta)
# print(print(type(delta)))

from datetime import date, timedelta

today = date.today()
new_date = today - timedelta(days=5)

print("Today:", today)
print("5 days ago:", new_date)
