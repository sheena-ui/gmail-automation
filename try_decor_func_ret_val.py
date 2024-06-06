def hello_decorator(func):
    def inner(*args, **kwargs):
        print('Inside decorator function')
        print('Before execution')

        # getting the returned value
        # from the call to external func
        returned_val = func(*args, **kwargs)

        print('After execution')

        # returning the value to the original frame
        return returned_val
    return inner


# is the same as hello_decorator(sum_two_numbers)
@hello_decorator
def sum_two_numbers(a, b):
    print('Inside the gift function')
    return a+b


if __name__ == '__main__':
    a, b = 1, 2
    print('Sum = ', sum_two_numbers(a, b))