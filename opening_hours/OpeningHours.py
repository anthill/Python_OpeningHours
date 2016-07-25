#!/usr/bin/python

from ctypes import cdll, c_char_p, c_voidp

opening_hours = cdll.LoadLibrary("libopening-hours.so")

build = opening_hours.build_opening_hours
build.restype = c_voidp

print_oh = opening_hours.print_oh
print_oh.restype = c_char_p

class OpeningHours:
    def __init__(self, expression):
        self.oh = build(c_char_p(expression))

    def __str__(self):
        return str(print_oh(c_voidp(self.oh)))
