import os
import pytest
from library import Library

TEST_FILE = "test_library.json"

@pytest.fixture
def library():
    # Test dosyasını her seferinde sıfırdan oluştur
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    return Library(filename=TEST_FILE)

def test_add_and_list_books(library):
    test_isbn = "9780140328721"  # Fantastic Mr. Fox
    library.add_book(test_isbn)
    books = library.list_books()
    assert len(books) == 1
    assert "Fantastic Mr. Fox" in books[0].title
    assert "Roald Dahl" in books[0].authors

def test_remove_book(library):
    test_isbn = "9780140328721"
    library.add_book(test_isbn)
    library.remove_book(test_isbn)
    # Kitap silindi mi kontrol et
    found = library.find_book(test_isbn)
    assert found is None

def test_find_book(library):
    test_isbn = "9780140328721"
    library.add_book(test_isbn)
    found = library.find_book(test_isbn)
    assert found is not None
    assert "Fantastic Mr. Fox" in found.title
