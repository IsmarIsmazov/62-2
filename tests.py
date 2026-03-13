




# def example(number: int) -> int: ...


# def example2(*args) -> str:
#     args[0] 

# def example3(**kwargs) -> str:
#     kwargs.get("a") 

# example2([1, "hasd", True])
# example3(a=1, b="hasd", c=True)

# auth = {
#     "login": "ismar",
#     "password": "1234567890"
# }

# login = auth.get("name")
# # login = auth["name"]
# print(login)


list_obj = ["12", 12, True, 123.012, None]
limit = 2
page = 3
max_page = len(list_obj) // limit 
print(f"максимальная страницы: {max_page}")
list_pages = range(1, max_page + 1)
for i in list_pages:
    print(f"страницы номер: {i}")
start = (page - 1) * limit
print(f"start: {start}")
end = page * limit
print(f"end: {end}")
result = list_obj[start:end]
print(f"результат: {result}")
