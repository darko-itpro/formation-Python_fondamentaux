

def say_hello(name="World"):
    print("Hello", name)

say_hello()
say_hello("Guido")

def create_account(id, value=100, overdraft=False):
    print(id, value, overdraft)

create_account("my id", 1000000000, True)
create_account("my id", 1000000000)
create_account("my id")
create_account("my id", overdraft=True)
