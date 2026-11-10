
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book Title:", self.title)
        print("Book Author:", self.author)
        print("Book Price:", self.price)


b1 = Book("Python Programming", "John", 450)
b2 = Book("Java Programming", "James", 500)

b1.display()
b2.display()
