class Country:
    def __init__(self):
        print('constructor')

    def __init__(self,name):
        self.name = name
        print(self.name)

    def __init__(self,name="Default"):
        self.name = name
        print(self.name)

    def instance_method1(self):
        print('instance method')

def instance_method2():
    print('instance method2')

default_country = Country()
india = Country('india')
india.instance_method1()
instance_method2()
