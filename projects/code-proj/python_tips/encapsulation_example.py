class BookEnhanced:
    def __init__(self, name, copies,author):
        self.name = name
        self._copies = copies
        self.__author = author
    @property   # Property decorator
    def copies(self):
        print('getter called')
        return self._copies  # _copies is protected type(single underscore is used)

    @copies.setter
    def copies(self, copies):
        print('setter called')
        if copies>=0:
            self._copies = copies
    @property
    def author(self):
        print('getter called')
        return self.__author # __author is private type(double underscore is used)

microservices = BookEnhanced('Microservices', 3, 'Author1')
print(microservices.copies) # 3
print('==============')
microservices.copies = 25
print(microservices.copies) # 25
print(microservices.author) # Author1
