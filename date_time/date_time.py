import datetime


# поточна дата і час
# now = datetime.now()
# print(now)

current_datetime = datetime.datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
# microsecond: Повертає мікросекунди часу.
# Це значення може бути від 0 до 999999.
# У "2023-12-14 12:39:29.992996", now.microsecond буде 992996.
print(current_datetime.microsecond)
# tzinfo: Повертає інформацію про часову зону об'єкта datetime.
# Для now, якщо часова зона не була вказана, tzinfo буде None.
print(current_datetime.tzinfo)
# просто дата без часу
print(current_datetime.date())
# просто час без дати
print(current_datetime.time())


# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(
    year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

# Створення об'єкта datetime
now = datetime.datetime.now()

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}")

# Створення двох об'єктів datetime
datetime1 = datetime.datetime(2023, 3, 14, 12, 0)
datetime2 = datetime.datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# False, тому що datetime1 не наступає за datetime2
print(datetime1 > datetime2)


# Ключові аспекти: методи роботи з датами і часом

# datetime.now(): Метод повертає об'єкт datetime, який містить поточну дату та час.
# datetime.date(): Цей метод повертає об'єкт date, який представляє лише дату (без часу).
# datetime.time(): Метод повертає об'єкт time, який містить лише час (без дати).
# datetime.combine(date, time): Цей метод використовується для об'єднання
# об'єктів date та time і створення нового об'єкта datetime.
# datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0):
# Конструктор класу datetime дозволяє створити об'єкт
# datetime з конкретною датою та часом.
# weekday(): Метод визначає номер дня тижня для вказаної дати,
# де понеділок має номер 0, а неділя - 6.

delta = datetime.timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)


seventh_day_2019 = datetime.datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime.datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

# Додаємо 10 днів до поточної дати
future_date = now + datetime.timedelta(days=10)
print(future_date)


four_weeks_interval = datetime.timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

# Створення об'єкта datetime
date = datetime.datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

# визначити скільки пройшло повних днів, коли Наполеон спалив Москву,
# а це відбулося 14 вересня 1812 року

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime.datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)


# ☝ timestamp є універсальним способом представлення часу,
# оскільки він не залежить від часових зон і календарних систем.
# представляється як кількість секунд (або мілісекунд/мікросекунд у деяких системах)
# з певної початкової дати, найчастіше з 1 січня 1970 року в UTC,
# це часовий пояс Гринвіча.
# У Python ви можете перетворити об'єкт datetime в timestamp і навпаки.
# Конвертація datetime в timestamp

# Конвертація datetime в timestamp
timestamp = datetime.datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу

timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime

# strftime - перетворює об'єкти datetime у рядки за допомогою форматування
# Синтаксис методу strftime виглядає наступним чином:
# datetime_object.strftime(format)
# Де datetime_object - це об'єкт datetime,
# а format - рядок формату, який визначає, як дата та час повинні бути представлені.

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)

# %Y - рік з чотирма цифрами (наприклад, 2023).
# %y - рік з двома цифрами (наприклад, 23).
# %m - місяць як номер (наприклад, 03 для березня).
# %d - день місяця як номер (наприклад, 14).
# %H - година (24-годинний формат) (наприклад, 15).
# %I - година (12-годинний формат) (наприклад, 03).
# %M - хвилини (наприклад, 05).
# %S - секунди (наприклад, 09).
# %A - повна назва дня тижня (наприклад, Tuesday).
# %a - скорочена назва дня тижня (наприклад, Tue).
# %B - повна назва місяця (наприклад, March).
# %b або %h - скорочена назва місяця (наприклад, Mar).
# %p - AM або PM для 12-годинного формату.

# strptime - перетворює рядки у об'єкти datetime за допомогою форматування
# Синтаксис методу strptime виглядає наступним чином:
# datetime_object = datetime.strptime(string, format)
# де:
# string - рядок, який містить дату та/або час.
# format - рядок формату, який вказує, як розібрати string.

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.datetime.strptime(date_string, "%Y.%m.%d")
# Виведе об'єкт datetime, що відповідає вказаній даті та часу
print(datetime_object)


# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)

iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.datetime.fromisoformat(iso_date_string)
print(date_from_iso)

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

# Поверне число від 1 до 7, що відповідає дню тижня
print(f"Сьогодні: {day_of_week}")

# isocalendar() - це кортеж (ISO_рік, ISO_тиждень, ISO_день_тижня), де:

# ISO_рік - це рік у форматі ISO.
# ISO_тиждень - номер тижня в році за ISO 8601 (від 1 до 53).
# ISO_день_тижня - день тижня за ISO 8601, де 1 означає понеділок, а 7 - неділю.

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {
      iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

local_now = datetime.datetime.now()
utc_now = datetime.datetime.now(datetime.timezone.utc)

print(local_now)
print(utc_now)  # Виведе поточний час в UTC


utc_time = datetime.datetime.now(datetime.timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(
    datetime.timezone(datetime.timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)


# Щоб перетворити локальний час у час UTC, спочатку потрібно призначити
# локальному часу відповідну часову зону, а потім використати метод
# astimezone() для конвертації його в UTC:

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = datetime.timezone(datetime.timedelta(hours=2))
local_time = datetime.datetime(
    year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(datetime.timezone.utc)
print(utc_time)  # Виведе час в UTC

# У цьому прикладі, ми створили об'єкт datetime з часовою зоною UTC+2 (Київ)
# та перетворили його в час UTC


# Час у конкретній часовій зоні
timezone_offset = datetime.timezone(
    datetime.timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime.datetime(
    year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)
