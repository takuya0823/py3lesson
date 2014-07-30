__author__ = 'ts'
import datetime
today = datetime.datetime.now()
print(today)
print(today.weekday())
if today.weekday() < 3:
    print('weekday today.work to hard.')
elif today.weekday() == 4:
    print('金曜日だ')
else:
    print('today is hooooooliday!')




