#!/usr/bin/python3
'''Log Parsing'''
import sys
import signal


# Create dictionary to store number of lines for each status code
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Initializing the total file size and the number of lines
file_size = 0
num_lines = 0


def status_to_print():
    '''Returns/prints the current status'''
    print("File size: {}".format(file_size))
    for stat in sorted(status_codes.keys()):
        if status_codes[stat] > 0:
            print("{}: {}".format(stat, status_codes[stat]))


def handle_signal(sig, frame):
    '''Create handler for signals that will print stats
        when script is interrupted
    '''
    status_to_print()
    sys.exit(0)


# Register the handler for signals for the SIGINT signal (CTRL+C)
signal.signal(signal.SIGINT, handle_signal)

# Read and parse lines from stdin
for line in sys.stdin:
    try:
        element = line.split(" ")
        i_p = element[0]
        stats = int(element[8])
        size = int(element[9])
        file_size += size
        status_codes[stats] += 1
        num_lines += 1
        if num_lines == 10:
            status_to_print()
            num_lines = 0
    except (IndexError, ValueError):
        # If line not in actual format, skip it
        continue

# When there is no more input print stats
status_to_print()
