#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys


total_size = 0
status_count = {}
line_count = 0


def print_stats():
    global total_size, status_count
    print("File size: {}".format(total_size))
    for code in sorted(status_count.keys()):
        print("{}: {}".format(code, status_count[code]))
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) == 9 and tokens[0].count(".") == 3 and tokens[5].startswith('"GET') and tokens[6].startswith("/") and tokens[7].startswith("HTTP/") and tokens[8].isdigit():
            status_code = int(tokens[8])
            file_size = int(tokens[-1])
            total_size += file_size
            if status_code in status_count:
                status_count[status_code] += 1
            else:
                status_count[status_code] = 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise

print_stats()