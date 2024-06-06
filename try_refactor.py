class MFALogin:
    def __init__(self, gift_func):
        self.gift_func = gift_func
        self.__inst = None

    def wrapper(self, *args, **kwargs):
        print(f'Decorator function')
        if not self.__inst:
            return self.gift_func(*args, **kwargs)
        else:
            print(f'First try')
            resp = self.gift_func(self.__inst, *args, **kwargs)
            if resp.get('status') == 400:
                mfa = kwargs.get('mfa', 'auth_app')
                ret = getattr(self, mfa)(*args, **kwargs)
                if ret:
                    resp = ret
            return resp
            # return self.gift_func(self.__inst, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.wrapper(*args, **kwargs)

    def __get__(self, inst, owner):
        self.__inst = inst
        return self.wrapper

    def auth_app(self, *args, **kwargs):
        print(f'For second try, decorated gift function')
        return self.gift_func(self.__inst, token=123123, *args, **kwargs)

    def verify_app(self, *args, **kwargs):
        pass


class SsoApi:
    @MFALogin
    def login(self, status=200, *args, **kwargs):
        print('Inside gift function')
        payload = {
            'user': 'sheena',
            'pwd': 'password',
            'status': status
        }
        payload.update(kwargs)
        return payload


@MFALogin
def login(status=200, *args, **kwargs):
    print('Inside standalone gift function')
    payload = {
        'user': 'sheena',
        'pwd': 'password',
        'status': status
    }
    payload.update(kwargs)
    return payload


# sso = SsoApi()
# print(1)
# print(sso.login())
# print(2)
# print(sso.login(status=400))
# print(3)
# print(sso.login(status=400, mfa='verify_app'))
# print(4)
# print(sso.login(status=400, mfa='auth_app'))
# print(5)
# print(login())
# print(6)
# print(login(status=400))

tmp = {
    'otp_secret': 111,
    'ui_otp_secret': 222,
    'other_secret': 2
}
print(f'Before deleting: {tmp}')
secrets = ['otp_secret', 'ui_otp_secret']
for secret in secrets:
    if secret in tmp:
        del tmp[secret]
print(f'After deleting: {tmp}')