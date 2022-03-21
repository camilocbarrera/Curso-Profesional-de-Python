from datetime import datetime
import pytz

bogota_tz = pytz.timezone('America/Bogota')

bogota_date = datetime.now(bogota_tz)


# print(f'Bogotá: {bogota_date.strftime("%d/%m/%Y, %H:%M:%S")}')


# my_date = pass

def date_time_tz(time_zone: str):
    return f'{time_zone.split("/")[1].replace("_", " ")}: {datetime.now(pytz.timezone(time_zone)).strftime("%d/%m/%Y, %H:%M:%S")}'


print(date_time_tz('America/Bogota'))

print(date_time_tz('America/Caracas'))

print(date_time_tz('America/Buenos_Aires'))

print(date_time_tz('America/Mexico_City'))


def number(numa: int, numbb: float) -> bool:
    pass
