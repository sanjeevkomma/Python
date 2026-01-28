def multiply_by_3(data):
    return data * 3

def do_this_and_print(func, data):
    print(func(data))

do_this_and_print(multiply_by_3,125) # 375

do_this_and_print(lambda data:data * 5, 8) # 40

do_this_and_print(lambda data:data * data , 55) # 3025

do_this_and_print(lambda data: data ** 3 , 6) # 216

do_this_and_print(lambda data: len(data), 'Test') # 4
