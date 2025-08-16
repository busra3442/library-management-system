from library import Library

def test_add_book_from_api():
    lib = Library("test.json")
    lib.add_book("9780140328721")  # Matilda, Roald Dahl
    assert any(book.isbn == "9780140328721" for book in lib.books)


