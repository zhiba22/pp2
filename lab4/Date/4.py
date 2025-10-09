
from datetime import datetime

date1 = datetime(2025, 10, 9, 12, 0, 0)
date2 = datetime(2025, 10, 10, 14, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)
