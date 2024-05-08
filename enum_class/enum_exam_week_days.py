from enum import Enum


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY


if today == Day.MONDAY:
    print("Сьогодні понеділок.")
else:
    print("Сьогодні не понеділок.")
# Виведе: Сьогодні понеділок.

# має властивості name та value
print(today.name)  # Виведе: MONDAY
print(today.value)  # Виведе: 1

# отримання елемента за значенням
day_from_value = Day(1)
print(day_from_value)  # Виведе: Day.MONDAY
