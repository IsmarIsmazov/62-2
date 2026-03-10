




# def example(number: int) -> int: ...


# def example2(*args) -> str:
#     args[0] 

# def example3(**kwargs) -> str:
#     kwargs.get("a") 

# example2([1, "hasd", True])
# example3(a=1, b="hasd", c=True)

auth = {
    "login": "ismar",
    "password": "1234567890"
}

login = auth.get("name")
# login = auth["name"]
print(login)