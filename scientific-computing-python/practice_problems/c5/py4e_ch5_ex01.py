number = 0.0
total = 0.0
smallernum = None
largernum = None
while True:
    sval = input('Enter number:')
    if sval == "done" :
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Entry")
        continue
    #print(fval)
    number = number + 1
    total = total + fval
    if smallernum is None and largernum is None:
        smallernum = fval
        largernum = fval
        print("smaller", smallernum)
        print("larger", largernum)
    elif fval < smallernum and fval < largernum:
        fval = smallernum
        print("smallerelse", smallernum)
    else:
        if fval > largernum:
            largernum = fval
            print("largerelse", largernum)

print("Total:", total, "Average:", total/number, "Minumum:", smallernum, "Maximum", largernum)
