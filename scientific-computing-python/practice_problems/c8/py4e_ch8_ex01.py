def chop(lst):
    del lst[0]
    del lst[-1]
    # what if I did return lst instead?
    return lst
    # with this return function it brings the value up so regardless if i define a new variable or not it will print out

def middle(lst):
    #del lst[0]
    #del lst[-1]
    #print(lst)
    ## the above verses
    new = lst[1:]
    del new[-1]
    # without the return function it still prints out none
    return new
    # with the return function it returns the actual value

list_1 = [0,1,2,3,4,5]
#print(chop(list_1)) this output is "none" why? probs bc no longer in existence
#print(list_1) will print the middle
#chop_list_1 = chop(list_1)
#print(chop_list_1) same output as the top comment
#print(chop(list_1))
#print(middle(list_1))

#middle_list = middle(list_1)
#print(middle_list)
print(chop(list_1))
