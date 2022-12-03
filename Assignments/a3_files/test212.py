import calendar
import re

out = "04/02/1998 is today's date"

out1 = re.search(r"(\d?\d)[\/\-\.](\d?\d)[\/\-\.](\d\d\d\d)",out)
out = re.sub(r"(\d?\d)[\/\-\.](\d?\d)[\/\-\.](\d\d\d\d)",calendar.month_abbr[int(out1.group(1))] + ". " + out1.group(2) + ", " +out1.group(3),out)
split = out.split()
print(split)
