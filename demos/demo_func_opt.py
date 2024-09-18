def say_hello(name:str = "World"):
    print("Hello", name)

say_hello()
say_hello("BPCE")

def create_account(id, value=100, overdraft=False):
    print(id, value, overdraft)

create_account("my id", 1_000_000_000, True)
create_account("my id", 1_000_000_000)
create_account("my id")
create_account(id="my id", overdraft=True)

def func(value):
    print(value)

func(value=10)
