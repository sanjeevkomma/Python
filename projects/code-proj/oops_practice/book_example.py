class Book:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr(self.name)

book1 = Book("Mastering Spring 5.0");
book2 = Book("Mastering Python");

print(book1)
print(book2)


# ---output--
# 'Mastering Spring 5.0'
# 'Mastering Python'
