def say_hello():
    print("Hello World")

print(say_hello())

def give_hello() -> str:
    value = "Hello given"
    return value

print(give_hello())

def say_hello_to(name:str):
    print("Hello", name)
    
say_hello_to("Guido")
