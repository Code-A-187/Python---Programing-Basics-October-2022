from math import floor

processors_needed = int(input())
workers = int(input())
working_days = int(input())

manufactured_processors = floor(workers * working_days * 8) / 3

if manufactured_processors >= processors_needed:
    print(f'()')