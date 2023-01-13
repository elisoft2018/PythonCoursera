from datetime import time, timedelta, date, datetime


init_time_for_now = datetime.now()
print('la fecha actual es', init_time_for_now)
print('la fecha futura dos años al futuro es', init_time_for_now + timedelta(days=730))
print(timedelta.min)
print(timedelta.max)
print(timedelta.resolution)



print(date.min)
print(date.max)
print(date.resolution)


print(datetime.min)
print(datetime.max)
print(datetime.resolution)


print(time.min)
print(time.max)
print(time.resolution)

date_time = date.today()
print('Fecha', date_time)
# La función strftime crea un string a partir de un objeto datetime

print('Fecha formateada a un string',  date_time.strftime("%Y-%m-%d"))
print('Fecha formateada a un date time', date_time.strftime("%Y-%m-%d %H:%M:%S"))

print('Fecha formateada a un string',  date_time.strftime("%Y/%m/%d"))
print('Fecha formateada a un date time', date_time.strftime("%Y/%m/%d T%H:%M:%S"))
print('Fecha formateada a un date time', date_time.strftime("%Y/%m/%d %H:%M:%S"))

print(datetime.strptime('2019-01-10', '%Y-%m-%d'))
print(datetime.strptime('2019-01-10 11:23:45', '%Y-%m-%d %H:%M:%S'))
print(datetime.strptime('2019-01-11 T11:23:45.67', '%Y-%m-%d T%H:%M:%S.%f'))
print(datetime.strptime('01-11-2019 T11:23:45.67', '%d-%m-%Y T%H:%M:%S.%f'))

print('TRABAJANDO FECHAS CON EL OBJETO DATE')
my_date = date(2019, 6, 2)
print('Año', my_date.year)
print('Mes', my_date.month)
print('Dia', my_date.day)
print('dia de la semana', my_date.weekday())
print('dia de las semana iso', my_date.isoweekday())
print('Devolver Calendario', my_date.isocalendar())
print('Devolver fecha iso', my_date.isoformat())

date_min = my_date.min
date_max = my_date.max
current_date = date.today()
print('fecha minima', date_min)
print('fecha maxima', date_max)
print('fecha actual', current_date)

yesterday = current_date - timedelta(days=2)
print('Fecha de ayer', yesterday)

delta = current_date - yesterday
print('la diferencia en fechas es', delta)

print('TRABAJANDO FECHAS CON OBJETO DATE TIME')

date_and_time = datetime(2019, 10, 10, 9, 15, 30)
print('fecha date time', date_and_time)
print('año date time', date_and_time.year)
print('mes date time', date_and_time.month)
print('dia date time', date_and_time.day)
print('hora date time', date_and_time.hour)
print('minutos date time', date_and_time.minute)
print('segundos date time', date_and_time.second)
print('microsegundos date time', date_and_time.microsecond)

date_type = date_and_time.date()
print('fecha date a partir de date time', date_type)
now = datetime.now()
print('fecha actual local date time', now)
now_utc = datetime.utcnow()
print('fecha actual UTC date time', now_utc)

print('TRABAJANDO CON OBJETOS DE TIPO TIME')

time_example = time(10, 15, 45)
print('hora', time_example.hour)
print('minutos', time_example.minute)
print('segundos', time_example.second)
print('microsegundos', time_example.microsecond)

time_min = time.min
print('Tiempo minimo', time_min)

time_max = time.max
print('Tiempo maximo', time_max)

date_and_time_1 = datetime(2022, 9, 28, 8, 15, 30)
""" La función strftime crea un string a partir de un objeto datetime"""
print('La función strftime crea un string a partir de un objeto datetime')
print(date_and_time_1.strftime('%Y-%m-%d'))
print(date_and_time_1.strftime('%Y-%m-%d T%H:%M:%S'))
print(date_and_time_1.strftime('%Y/%m/%d'))
print(date_and_time_1.strftime('%Y/%m/%d T%H:%M:%S'))
print(date_and_time_1.strftime('%d/%m/%Y'))
print(date_and_time_1.strftime('%d/%m/%Y T%H:%M:%S'))
print(date_and_time_1.strftime('%d-%m-%Y'))
print(date_and_time_1.strftime('%d-%m-%Y T%H:%M:%S'))

"""La función strptime crea un objeto datetime a partir de un string """

print('La función strptime crea un objeto datetime a partir de un string')

print(date_and_time_1.strptime('2022-09-28', '%Y-%m-%d'))
print(date_and_time_1.strptime('2022-09-28 20:29:56', '%Y-%m-%d %H:%M:%S'))
print(date_and_time_1.strptime('2022-09-7 T20:29:56', '%Y-%m-%d T%H:%M:%S'))
print(date(2019, 12, 31 ).isoformat())











