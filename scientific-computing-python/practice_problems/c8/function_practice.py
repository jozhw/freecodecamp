max = None
min = None

number_list = []

#functions
def max_min(numlist):
    global max
    global min
    # with the global it changes the max and min values outside the function
    # now if you do not put the global that will lead to a tace back error
    # if you do not use global as in you do not want to change the variable
    # you have to put in the argument when defining the variable
    # for example def max_min(numlist, max, min) will call the function that is
    # in the global however, it will not store it in the global
    # this max_min(numlist, max, min)() will not affect the global variable max and min so when this function
    # executes and you do print(max, min) outside of the function
    # it will still print none
    for number in numlist:
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

    #return min, max
    # this return will change the values of min and max
    # so when you print(max_min(number_list, min, max)) the min and max will
    # be the values from the function



# code
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
        max_min(number_list)
        quit()

max_min(number_list) # if defined using max_min(number_list, max, min)
# then you have to put three variables that you want to call
#print(max, min) - under what you have right now "return" is redundant
