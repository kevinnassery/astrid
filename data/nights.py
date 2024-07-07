import datetime
f = open("van-stays.md","r")
dates = []
format = '%Y-%m-%d'

def convert_date(sdate):
	return datetime.datetime.strptime(sdate, format)

for x in f.readlines()[2:]:
	fields = x.split('|')
	checkin = convert_date(fields[1].rstrip().lstrip())
	checkout = convert_date(fields[2].rstrip().lstrip())
	dates.append([checkin,checkout])

nights = datetime.timedelta()
for date in dates:
	print(f"{date[1]} {date[0]}")
	nights += date[1] - date[0]
print(nights.days)
