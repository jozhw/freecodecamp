import re

def arithmetic_arranger(math, solve = False):

    def list_arranger(arrange):
        add = ""
        space = " "
        for item in arrange[:-1]:
          add += item + (space * 4)

        add += arrange[-1]

        return add

    first_line = []
    second_line = []
    line_bar = []
    solution = []
    arrange = ""

    if len(math) > 5:
        return 'Error: Too many problems.'

    for equation in math:

        if re.search('[^0-9\s\+-]+', equation):
            if re.search('[/]', equation) or re.search('[*]', equation):
                return "Error: Operator must be '+' or '-'."
            else:
                return 'Error: Numbers must only contain digits.'

        numbers = equation.split()
        first_integer = numbers[0]
        second_integer = numbers[2]
        operator = numbers[1]

        if (len(first_integer)) > 4 or (len(second_integer)) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if operator == '+':
            add_diff = str(int(first_integer) + int(second_integer))
        elif operator == '-':
            add_diff = str(int(first_integer) - int(second_integer))

#formatting the equations


        #determine the max length
        length = max(len(str(first_integer)), len(str(second_integer)))

    
        space = " "


        first_line.append(str(first_integer).rjust(length + 2))

        second_line.append(operator + space + str(second_integer).rjust(length))

        line_bar.append( '-' * (length + 2))

        solution.append(str(add_diff).rjust(length + 2))


    if solve:
        first = list_arranger(first_line)
        second = list_arranger(second_line)
        third = list_arranger(line_bar)
        final = list_arranger(solution)
        arrange = first + "\n" + second + "\n" + third + "\n" + final
    else:
        first = list_arranger(first_line)
        second = list_arranger(second_line)
        third = list_arranger(line_bar)
        arrange = first + "\n" + second + "\n" + third


    return arrange
