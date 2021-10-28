# RTC

Utilities for DS3231 real-time clock modules.

## `rtc_set_time.host.py`

This file runs on the HOST computer, and communicates with a microcontroller to set the RTC's internal time.

## `rtc_set_time.py`

This file runs on the MICROCONTROLLER. It receives the time from the host computer and sets the RTC's internal time.

## Usage

1. Copy `rtc_set_time.py` to the microcontroller as `code.py`.
2. Copy the [`adafruit_ds3231`](https://github.com/adafruit/Adafruit_CircuitPython_DS3231) module to the microcontroller's `lib` directory.
3. Run `python3 rtc_set_time.host.py /dev/ttyACMX` on the host computer, where `X` is the number of the serial port for communication with the microcontroller.
