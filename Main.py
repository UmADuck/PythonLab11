import re

f = open('access_log_Jul95', 'r')
lines = f.readlines()

data_regex = r'^.*\[01\/Jul\/1995\:00\:([0-1][0]|[0][1-9])\:([0-6][0-9]).*NASA.*$'


pattern = re.compile(data_regex)

number_of_matches = 0

for line in lines:
    m = pattern.match(line)
    if m:
         number_of_matches += 1
print(f"number_of_matches: {number_of_matches}" )

