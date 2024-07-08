
value = 1
previous = 1

while value < 500:
    print(value/previous)
    value, previous = value + previous, value
