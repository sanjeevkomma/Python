class Book:
    def __init__(self, name, author, copies):
        self.name = name
        self.author = author
        self.copies = copies

    def __repr__(self):
        return repr((self.name, self.author, self.copies))

book1 = Book("Mastering Spring 5.0", "Author1", "14")
book2 = Book("Mastering Python", "Author2", "244")

print(book1)
print(book2)


# ---output--
# ('Mastering Spring 5.0', 'Author1', '14')
# ('Mastering Python', 'Author2', '244')
