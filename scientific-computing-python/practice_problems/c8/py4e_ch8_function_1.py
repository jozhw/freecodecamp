def foo():
    print("hello from inside of foo")
    # what the return function does is
    # define the value of return to
    # the function
    return 1

if __name__ == '__main__':
    print("going to call foo")
    x = foo()
    # everytime you call the function
    # it executes in this case wil print
    # out the "hello.."
    # however the return value does
    # not get printed because it is not called to print
    print("called foo")
    print("foo returned " + str(x))
