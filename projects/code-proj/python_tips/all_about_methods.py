def example_method(mandatory_parameter, default_parameter="Default",
                   *args, **kwargs):   # args is Tuple, kwargs(keyword arguments) is Dictionary
    print(f"""
         mandatory_parameter: {mandatory_parameter} {type(mandatory_parameter)}
         default_parameter: {default_parameter} {type(default_parameter)}
         args: {args} {type(args)}
         kwargs: {kwargs} {type(kwargs)}
        """)

example_method(15,"String 1","String 2","String 3","String 4","String 5")
# mandatory_parameter: 15 <class 'int'>
#          default_parameter: String 1 <class 'str'>
#          args: ('String 2', 'String 3', 'String 4', 'String 5') <class 'tuple'>
#          kwargs: {} <class 'dict'>

print('=========')
example_method(15,"String 1","String 2","String 3","String 4","String 5", key1='a', key2='b')
# mandatory_parameter: 15 <class 'int'>
#          default_parameter: String 1 <class 'str'>
#          args: ('String 2', 'String 3', 'String 4', 'String 5') <class 'tuple'>
#          kwargs: {'key1': 'a', 'key2': 'b'} <class 'dict'>
print('=========')
example_method(25, "String 1","String 2","String 3","String 4","String 5")
example_method(25,"String 1", key1='a', key2='b')
example_method(key1='a', key2='b',mandatory_parameter=33, default_parameter="String 1")
print('=============================================')
example_list = [10,20,30,40,50,60]
example_method(example_list[0],example_list[1],example_list[2])
# mandatory_parameter: 10 <class 'int'>
#          default_parameter: 20 <class 'int'>
#          args: (30,) <class 'tuple'>
#          kwargs: {} <class 'dict'>
example_method(*example_list) # argument unpacking
# mandatory_parameter: 10 <class 'int'>
#          default_parameter: 20 <class 'int'>
#          args: (30, 40, 50, 60) <class 'tuple'>
#          kwargs: {} <class 'dict'>
example_dict = {'a':'1','b':'2'}
example_method(*example_list, **example_dict)
# mandatory_parameter: 10 <class 'int'>
#          default_parameter: 20 <class 'int'>
#          args: (30, 40, 50, 60) <class 'tuple'>
#          kwargs: {'a': '1', 'b': '2'} <class 'dict'>












