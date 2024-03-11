def print_info(**kwargs):
    '''
    **kwargs is a dictionary here
    '''
    for key, value in kwargs.items():
        print(key, value)


print_info(name="abhi", age=27, job="SE")
