def hello_decorator(func):

    # inner is a wrapper function in which the argument is called
    # inner function can access the outer local functions like in this case 'func'
    def inner():
        print('Inside decorator function')
        print('print before argument function call')

        # calling the actual function now (actual function is passed by argument)
        # this is inside the wrapper function
        func()
        print('print after argument function call')

    # returns the wrapper function
    return inner


# defining a function to be called inside wrapper
def func_to_be_used():
    print('Inside the gift function')
    print('print the argument function')


# this step will not actually call 'func_to_be_used' function
# it is just retrieving and wrapped 'func_to_be_used' function
func_to_be_used = hello_decorator(func_to_be_used)

# this step calls the wrapped 'func_to_be_used'
func_to_be_used()