def arithmetic_arranger(problems, show_answers = True):
    # print(len(problems)) = 4
    if int(len(problems)) > 5:
        return "Error: Too many problems."

        arranged_problems = ""

    for index, value in enumerate(problems):
        # ["32", "+", "8"]
        operation = value.split(" ")

    if operation[1] not in "+-":
        return "Error: Operator must be '+' or '-'."

    if len(operation[0]) > 4 or len(operation[2]) > 4:
        return "Error: Numbers cannot be more than four digits."

    try:
        value_1 = int(operation[0])
        value_2 = int(operation[1])
        print(value_1, value_2)
    except ValueError:
        return "Error: Numbers cannot be more than four digits."

    temp_problem = f""
    {value_1}
    {operation[1]}
    {value[2]}
    # ----
    # """


    arranged_problems += temp_problem
    
    return arranged_problems

arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])