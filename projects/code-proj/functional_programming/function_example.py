def multiply_by_2(data):
    return data * 2

print(multiply_by_2(3)) # 6
print(multiply_by_2) # <function multiply_by_2 at 0x102558360>


def do_this_and_print(func, data):
    print(func(data))

do_this_and_print(multiply_by_2, 40) # 80

func_example_reference = multiply_by_2
print(func_example_reference(23)) # 46
