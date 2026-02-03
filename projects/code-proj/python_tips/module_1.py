def method_1():
    print('method_1')

class ClassA:
    def class_method_1(self):
        print('class_method_1')

#print(__name__) # __main__

if __name__ == '__main__':  # __name__ is built-in variable in every file(module).
    # It means that, only run this code if this file is executed directly, not when it’s imported
    method_1()
    ClassA().class_method_1()
# method_1
# class_method_1
