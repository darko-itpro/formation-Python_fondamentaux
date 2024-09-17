
def say_hello():
    print("Hello World")

def give_hello() -> str:
    value = "Hello given"
    return value

def say_hello_to(name:str):
    print("Hello", name)

say_hello()
print(give_hello())
