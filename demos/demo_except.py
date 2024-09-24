
value = "10a"
try:
    result = int(value)
    print("after bug")
except IndexError:
    print("other deal")
except (ValueError, LookupError):
    print("managed")


print("done")

