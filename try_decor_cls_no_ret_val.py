class MyDecor:

    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('Inside decorator function')
        print('Before execution')

        self.func()

        print('After execution')


# Equals instantiate MyDecor class with func_to_be_called as argument
# func_to_be_called = MyDecor(func_to_be_called).__call__()
@MyDecor
def func_to_be_called():
    print('Inside the gift function')
    print('print the argument function')


func_to_be_called()
