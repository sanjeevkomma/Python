class book:
    def __init__(self, name, author, copies):
        self.name = name
        self.author = author
        self.copies = copies

    def __repr__(self):
        return repr((self.name, self.author, self.copies))

    def increase_copies(self, how_many):
        self.copies += how_many

    def decrease_copies(self, how_many):
        self.copies -= how_many


book1 = book("Mastering Spring 5.0", "Author1", 14)
book2 = book("Mastering Python", "Author2", 244)

book1.increase_copies(5)
book2.decrease_copies(12)

print(book1)
print(book2)


# ---output--
# ('Mastering Spring 5.0', 'Author1', 19)
# ('Mastering Python', 'Author2', 232)
