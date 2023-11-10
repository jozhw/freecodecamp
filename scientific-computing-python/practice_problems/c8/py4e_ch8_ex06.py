number_list = []
max = None
min = None


while True:
    enter_number = input('Enter number: ')
    if enter_number == 'done':
        break
    try:
        float(enter_number)
        #print(enter_number)
        number_list.append(enter_number)
    except:
        print(enter_number, 'is not a number.')
        print(number_list)
        for number in number_list:
            numbers = float(number)
            if max is None and min is None:
                max = numbers
                #print('max', max)
                min = numbers
                #print('min', min)
            elif max < numbers:
                max = numbers
            else:
                if numbers < min:
                    min = numbers
        print('The maximum is: ', max, '.', 'The minimum is: ', min, '.')

        quit()

for number in number_list:
    numbers = float(number)
    if max is None and min is None:
        max = numbers
        #print('max', max)
        min = numbers
        #print('min', min)
    elif max < numbers:
        max = numbers
    else:
        if numbers < min:
            min = numbers

print(number_list)
print('The maximum is: ', max, '.', 'The minimum is: ', min, '.')
