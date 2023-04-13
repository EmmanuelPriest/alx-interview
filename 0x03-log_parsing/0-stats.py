#!/usr/bin/python3
'''Log Parsing'''
import sys
import signal


# Define a dictionary to store the number of lines for each status code
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Initialize the total file size and line count to zero
total_size = 0
line_count = 0


def print_stats():
    '''Prints the current stats'''
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    '''Handles signal to print stats when script is interrupted'''
    print_stats()
    sys.exit(0)

# Register the signal handler for the SIGINT signal (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

# Read lines from standard input and parse them
for line in sys.stdin:
    try:
        parts = line.split(" ")
        ip, _, _, _, _, _, _ = parts[:7]
        code = int(parts[8])
        size = int(parts[9])
        total_size += size
        if code in status_codes:
            status_codes[code] += 1
        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0
    except (IndexError, ValueError):
        # If the line is not in the specified format, skip it
        continue

# Print the final statistics when there is no more input
print_stats()
