# tests/test_library.py
import os
import pytest
from library import Library
from book import Book

TEST_FILE = "test_library.json"

@pytest.fixture
def library():
    # Test dosyasını her seferinde sıfırdan oluştur
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    return Library(filename=TEST_FILE)

def test_add_and_list_books(library):
    book = Book("Test Kitap", "Test Yazar", "12345")
    library.add_book(book)
    books = library.list_books()
    assert len(books) == 1
    assert books[0].title == "Test Kitap"

def test_remove_book(library):
    book = Book("Silinecek", "Yazar", "54321")
    library.add_book(book)
    library.remove_book("54321")
    assert library.find_book("54321") is None

def test_find_book(library):
    book = Book("Aranan", "Yazar", "99999")
    library.add_book(book)
    found = library.find_book("99999")
    assert found is not None
    assert found.title == "Aranan"
