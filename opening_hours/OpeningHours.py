#!/usr/bin/python

from ctypes import cdll, c_char_p, c_voidp, c_int

opening_hours = cdll.LoadLibrary("libopening-hours.so")

build = opening_hours.build_opening_hours
build.restype = c_voidp

print_oh = opening_hours.print_oh
print_oh.restype = c_char_p

isopen = opening_hours.is_open_expended
isopen.restype = c_int

class OpeningHours:
    def __init__(self, expression):
        self.oh = build(c_char_p(expression))

    def __str__(self):
        return str(print_oh(c_voidp(self.oh)))

    def is_open_expended(self, min, hour, day, month, year, day_of_week, day_of_year):
        return isopen(c_voidp(self.oh), c_int(min), c_int(hour), c_int(day), c_int(month), c_int(year), c_int(day_of_week), c_int(day_of_year))
