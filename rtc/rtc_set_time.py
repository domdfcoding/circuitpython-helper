#!/usr/bin/env python
#
#  rtc_set_time.py
"""
Listen for the time from the host computer and set the time on the connected RTC.

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit's DS3231 library:
  https://github.com/adafruit/Adafruit_CircuitPython_DS3231
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import board  # type: ignore
import busio  # type: ignore
import time

# 3rd party
import adafruit_ds3231  # type: ignore

# Set up communication with the RTC
i2c = busio.I2C(board.GP1, board.GP0)
ds3231 = adafruit_ds3231.DS3231(i2c)

# Wait 1 second for the PC to catch up.
time.sleep(1)

# Get the current time from the host PC.
tm_year = int(input("tm_year: "))
tm_mon = int(input("tm_mon: "))
tm_mday = int(input("tm_mday: "))
tm_hour = int(input("tm_hour: "))
tm_min = int(input("tm_min: "))
tm_sec = int(input("tm_sec: "))
tm_wday = int(input("tm_wday: "))
tm_yday = int(input("tm_yday: "))
tm_isdst = int(input("tm_isdst: "))

# Set the time.
new_time = time.struct_time((
		tm_year,
		tm_mon,
		tm_mday,
		tm_hour,
		tm_min,
		tm_sec,
		tm_wday,
		tm_yday,
		tm_isdst,
		))

ds3231.datetime = new_time

# Print the time from the computer, and the time retrieved back from the RTC, for debugging.
print(new_time)
print(ds3231.datetime)
