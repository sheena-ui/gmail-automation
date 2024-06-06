
def test_header(*args, header={}):
    for arg in args:
        header.update(arg)
    return header


if __name__ == '__main__':
    # test_header({'Content-Type': 'application/json'}, {'Content-Type': 'multipart/form-data'})
    # print(test_header())
    headers = {'Content-Type': 'application/json'}
    headers.update({'Content-Type': 'multipart/form-data'})
    print(headers)