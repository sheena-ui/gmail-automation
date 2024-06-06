def print_info(*args, **kwargs):
    print('Print information from arguments')
    print(args)
    print(kwargs)


if __name__ == '__main__':
    print_info('monday', 'tuesday', 'wednesday')
    print_info(monday=1, tuesday=2)
    print_info('monday', 'tuesday', monday=1, tuesday=2)