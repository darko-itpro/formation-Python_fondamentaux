#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Ce module présente les motifs pour identifier les dates.
"""

all_months = "(0[1-9]|1[0-2])/([01][1-9]|10|2[0-8])"
all_months_except_february = "(0[13-9]|1[0-2])/(29|30)"
all_31_days_months = "(0[13578]|1[0-2])/31"
all_together = "((0[1-9]|1[0-2])/([01][1-9]|10|2[0-8]))|((0[13-9]|1[0-2])/(29|30))|((0[13578]|1[0-2])/31)"
add_for_leap_year = "|02/29"

if __name__ == '__main__':
    pass