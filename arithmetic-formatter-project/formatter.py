def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        # this will check if the number of problems is more than 5
        # if it is, we will return an error message.
        return "Error: Too many problems."

    arranged_problems = [] # this will hold the arranged problems
    

    for index, value in enumerate(problems):
        # ["32", "+", "8"]
        operation = value.split(" ") # this will split the string into a list of 3 elements

        if operation[1] not in "-+":
            # this will check if the operator is not + or -
            # if it is not, we will return an error message.
            return "Error: Operator must be '+' or '-'."

        if len(operation[0]) > 4 or len(operation[2]) > 4:
            # this will check if the numbers are more than 4 digits
            # if they are, we will return an error message.
            return "Error: Numbers cannot be more than four digits."
        
        try:
            # this will check if the numbers are not digits
            # if they are not, we will return an error message.
            # this will also convert the numbers to integers
            # and assign them to value_1 and value_2
            value_1 = int(operation[0])
            value_2 = int(operation[2])
        except ValueError:
            return "Error: Numbers must only contain digits."


        longest_val = max(len(operation[0]), len(operation[2]))
        # this will get the longest value of the two numbers
        # this will also get the length of the longest value
        width = longest_val + 2

        line_1 = f"{operation[0]:>{width}}" # this will format the first number to the right
        # this will also add the width to the number
        line_2 = operation[1] + f"{operation[2]:>{width-1}}"
        # this will format the second number to the right
        # this will also add the width to the number
        d = '-' * width
        

        try:
            # this will check if the arranged_problems list is empty
            # if it is, we will append the first line to it
          arranged_problems[0] += (' ' * 4) + line_1
        except IndexError:
          arranged_problems.append(line_1)

        try:
            # this will check if the arranged_problems list is empty
            # if it is, we will append the second line to it
          arranged_problems[1] += (' ' * 4) + line_2
        except IndexError:
          arranged_problems.append(line_2)

        try:
            # this will check if the arranged_problems list is empty
            # if it is, we will append the third line to it
          arranged_problems[2] += (' ' * 4) + d
        except IndexError:
          arranged_problems.append(d)


        if args:
            # this will check if the args list is not empty
            # if it is not, we will append the answer to the list
          # this will also check if the answer is not None
          ans = int(operation[0]) + int(operation[2]) if operation[1] == '+' else int(operation[0]) - int(operation[2])
          a = f"{str(ans):>{width}}"

          try:
              # this will check if the arranged_problems list is empty
              # if it is, we will append the answer to it
            arranged_problems[3] += (' ' * 4) + a
          except IndexError:
            arranged_problems.append(a)


    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    # this will join the first three lines with a new line character
    # this will also add the fourth line if args is not empty
    output = output + f"\n{arranged_problems[3]}" if args else output

    return output

# This will print the arranged problems with the answers.
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))