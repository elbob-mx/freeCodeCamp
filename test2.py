math = ["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]
# print(math[0])

longest_val = max(len(math[0]), len(math[2]), len(math[2]))

width = longest_val + 2

output = f"{math[0]:>{width}}\n{math[1]}{math[2]:>{width}}\n{'-'*width}"
print(output)