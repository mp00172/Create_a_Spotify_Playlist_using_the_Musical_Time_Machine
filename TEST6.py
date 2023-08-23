import datetime

year_today = str(datetime.datetime.now()).split()[0].split("-")[0]
print(year_today)
print(type(year_today))