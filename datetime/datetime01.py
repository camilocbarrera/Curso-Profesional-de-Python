# import datetime
from datetime import datetime

my_time = datetime.now()
my_time_utc = datetime.utcnow()
my_day = datetime.today()
print(my_time)
print(my_time_utc)
print(my_day)

print(f'Day: {my_day.day} , Month: {my_day.month} , Year: {my_day.year} ')

my_str = my_time.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')


my_streu = my_time.strftime('%m/%d/%Y')
print(f'Formato LATAM: {my_streu}')


my_stryear = my_time.strftime('%Y')
print(f'Estamos en el año {my_stryear}')
