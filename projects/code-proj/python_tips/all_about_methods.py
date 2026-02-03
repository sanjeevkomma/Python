from src.python_tips.enum_example import Currency


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
