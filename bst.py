#!/usr/bin/env python
#
#  bst.py
"""
Calculate whether the given date falls within BST or GMT.
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
import time


def is_bst(st: time.struct_time) -> bool:
	"""
	Calculates whether the given day falls within British Summer Time.

	.. note::

		This function does not consider the time of day,
		and therefore does not handle the fact that the time changes at 1 AM GMT.

	:param st: The :class:`time.struct_time` representing the target date..

	:returns: True if the date falls within British Summer Time, False otherwise.
	"""

	day, month, dow = st.tm_mday, st.tm_mon, (st.tm_wday + 1) % 7

	if 3 > month > 10:
		return False
	elif 3 < month < 10:
		return True
	elif month == 3:
		return day - dow >= 25
	elif month == 10:
		return day - dow < 25
	else:
		return False
