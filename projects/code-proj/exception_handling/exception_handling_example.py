import builtins

# print(1/0) # ZeroDivisionError: division by zero
#print(2+'2') # TypeError: unsupported operand type(s) for +: 'int' and 'str'

values = [1,'2']
# print(sum(values)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(value); # NameError: name 'value' is not defined. Did you mean: 'values'?
# print(values.non_existing) # AttributeError: 'list' object has no attribute 'non_existing'
# print(values.non_existing()) # AttributeError: 'list' object has no attribute 'non_existing'

# ZeroDivisionError
# TypeError
# NameError
# AttributeError

help(builtins)


# CLASSES
#     object
#         BaseException
#             BaseExceptionGroup
#                 ExceptionGroup(BaseExceptionGroup, Exception)
#             Exception
#                 ArithmeticError
#                     FloatingPointError
#                     OverflowError
#                     ZeroDivisionError
#                 AssertionError
#                 AttributeError
#                 BufferError
#                 EOFError
#                 ImportError
#                     ModuleNotFoundError
#                 LookupError
#                     IndexError
#                     KeyError
#                 MemoryError
#                 NameError
#                     UnboundLocalError
#                 OSError
#                     BlockingIOError
#                     ChildProcessError
#                     ConnectionError
#                         BrokenPipeError
#                         ConnectionAbortedError
#                         ConnectionRefusedError
#                         ConnectionResetError
#                     FileExistsError
#                     FileNotFoundError
#                     InterruptedError
#                     IsADirectoryError
#                     NotADirectoryError
#                     PermissionError
#                     ProcessLookupError
#                     TimeoutError
#                 ReferenceError
#                 RuntimeError
#                     NotImplementedError
#                     PythonFinalizationError
#                     RecursionError
#                 StopAsyncIteration
#                 StopIteration
#                 SyntaxError
#                     IndentationError
#                         TabError
#                 SystemError
#                 TypeError
#                 ValueError
#                     UnicodeError
#                         UnicodeDecodeError
#                         UnicodeEncodeError
#                         UnicodeTranslateError
