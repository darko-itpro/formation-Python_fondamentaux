
value = "toto"

def convert(data):
    result = int(data) + 2
    return result

try:
    my_result = convert(value)
    print('le resultat est : ', my_result)
except IndexError:
    print("je fais autre chose")
except (ValueError, LookupError):
    print("in except")
finally:
    print("in finally")

print("done")
