list = ["30", "40", "500", "A"]


for number in list:
    width = len(max(list, key=len)) + 2
    print(f"{number:>{width}}")
    print(type(number))

print(f"this is: {type(list)} type")