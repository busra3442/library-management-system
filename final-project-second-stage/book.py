class Book:
    def __init__(self, title, authors, isbn):
        self.title = title
        self.authors = authors
        self.isbn = isbn

    def __repr__(self):
        return f"{self.title} - {self.authors} (ISBN: {self.isbn})"
