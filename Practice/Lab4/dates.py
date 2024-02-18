import datetime

def five_days_ago(day):
    return day - datetime.timedelta(days = 5)

def was_am_willbe():
    today = datetime.datetime.today()
    print(today - datetime.timedelta(days = 1))
    print(today)
    print(today + datetime.timedelta(days = 1))

def who_needs_em(date):
    return date.isoformat(sep = " ", timespec = "seconds")

def diff(date1, date2):
    return abs(date1 - date2).total_seconds()

#######

today = datetime.datetime.now()

print(five_days_ago(today))

was_am_willbe()
print(who_needs_em(today))
''
print(diff(five_days_ago(today), today), "seconds")
