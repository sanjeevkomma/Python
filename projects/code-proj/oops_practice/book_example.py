class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __repr__(self):
        return repr(self.name + ' ' + self.author)

book1 = Book("Mastering Spring 5.0", "Author1");
book2 = Book("Mastering Python", "Author2");

print(book1)
print(book2)


# ---output--
# 'Mastering Spring 5.0 Author1'
# 'Mastering Python Author2'
