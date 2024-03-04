"""Book-class"""


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        raise TypeError("Error")

    def __ne__(self, other):
        if isinstance(other, Book):
            return self.title != other.title or self.author != other.author
        raise TypeError("Error")


book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2")
book3 = Book("Title2", "Author2")


print(book1 == book2)
print(book3 == book2)
print(book1 != book2)