#!/usr/bin/env python
import sys

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 6:
        date, time, item, category, sales, payment = data
        print(f"{category}\t{sales}")