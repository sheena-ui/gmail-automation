"""
class Decorator:
    def __init__(self, gift_func):
        self.gift_func = gift_func

    def __call__(self, *args, **kwargs):
        print('Inside decorator function')
        print('Start wrapping gift with decorator')
        return self.gift_func(*args, **kwargs)


class Gift:

    gift_card = 'Wish you a happy day'

    @Decorator
    def male_gift(self, *args, **kwargs):
        print('Inside gift function')
        print(f'This is a gift for male: {args}, with items: {kwargs}')

    @Decorator
    def female_gift(self, *args, **kwargs):
        print('Inside gift function')
        print(f'This is a gift for female: {args}, with items: {kwargs}')
        print(f'With gift_card_attached: ', self.gift_card)


g = Gift()
g.male_gift('Andy', 'Bob', tie=3, wallet=1)
g.female_gift('Amy', 'Annie', shoes=3, bag=1, shirt=4)

>> AttributeError: 'str' object has no attribute 'gift_card'
"""


class UniversalDecorator:

    def __init__(self, gift_func):
        self.gift_func = gift_func
        self.inst = None

    def __call__(self, *args, **kwargs):
        print('Inside decorator function via __call__')
        return self.decorated_gift_func(*args, **kwargs)
        # print('Start wrapping gift with decorator')
        # return self.gift_func(*args, **kwargs)

    # def __get__(self, wrapped_inst, owner):
    #
    #     def inner(*args, **kwargs):
    #         print('Inside decorator function via __get__')
    #         print('Start wrapping gift with decorator')
    #         # the wrapped_inst position matches with the self parameter position
    #         return self.gift_func(wrapped_inst, *args, **kwargs)
    #
    #     return inner

    def __get__(self, wrapped_inst, owner):
        self.inst = wrapped_inst if wrapped_inst else self.inst
        print('Inside decorator function via __get__')
        return self.decorated_gift_func

    def decorated_gift_func(self, *args, **kwargs):
        print('Start wrapping gift with decorator')
        if self.inst is not None:
            # If self.inst is available, pass it as the first argument
            return self.gift_func(self.inst, *args, **kwargs)
        else:
            # Otherwise, pass all arguments as-is
            return self.gift_func(*args, **kwargs)


class Gift:
    gift_card = 'Wish you a happy day'

    @UniversalDecorator
    def male_gift(self, *args, **kwargs):
        print('Inside gift function')
        print(f'This is a gift for male: {args}, with items: {kwargs}')

    @UniversalDecorator
    def female_gift(self, *args, **kwargs):
        print('Inside gift function')
        print(f'This is a gift for female: {args}, with items: {kwargs}')
        print(f'With gift_card_attached: ', self.gift_card)


@UniversalDecorator
def small_parcel(*args, **kwargs):
    print('Inside parcel function')
    print(f'This is a parcel: {args}, with items: {kwargs}')


g = Gift()
g.male_gift('Andy', 'Bob', tie=3, wallet=1)
g.female_gift('Amy', 'Annie', shoes=3, bag=1, shirt=4)

small_parcel('Sheena', 'Gina', stamp=2, stickers=10)
