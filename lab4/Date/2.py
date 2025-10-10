
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(1)
tomorrow = today + timedelta(1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
