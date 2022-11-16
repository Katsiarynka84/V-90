import calendar
import locale
loc = (input('Введите локаль(ru, en, us, it, de): '))
locale.setlocale(locale.LC_ALL, loc)
print(calendar.calendar(2022))
