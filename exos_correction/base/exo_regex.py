from demos.myhome import confort
import re

def match_to_str(match_object):
    status = confort(int(match_object.group('temperature')))
    return status

def temp_to_natural(sentence:str) -> str:
    pattern = "(?P<temperature>[0-9]+)°[cC]"
    result = re.sub(pattern, match_to_str, sentence)
    return result

if __name__ == '__main__':
    sentence = "Lorsqu'il fait 12°c, je me couvre. Mais pendant les vacances, il a fait 26°c certains jours. Mais aujourd'hui, il a fait 22°c, nous en avons profité pour sortir un peu"
    print(temp_to_natural(sentence))
