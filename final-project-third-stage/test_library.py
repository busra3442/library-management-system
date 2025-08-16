import pytest
from library import Library, Book
import os

def test_add_and_find_book():
    # Test için ayrı bir json dosyası kullan
    test_file = "test_library.json"

    # Önce dosya varsa temizleyelim
    if os.path.exists(test_file):
        os.remove(test_file)

    lib = Library(test_file)

    # Denenecek ISBN (Matilda kitabı)
    isbn = "9780140328721"

    # Kitap ekle
    lib.add_book(isbn)

    # Kitabı bul
    found = lib.find_book(isbn)

    # Kontroller
    assert found is not None
    assert found.isbn == isbn
    assert "Fantastic Mr. Fox" in found.title  # Title "Matilda" geçmeli
    assert "Roald Dahl" in found.authors  # Yazar "Roald Dahl" olmalı

    # Temizlik
    if os.path.exists(test_file):
        os.remove(test_file)

def test_remove_book():
    lib = Library("test_library.json")
    book = Book("Silinecek", "Yazar", "456")
    lib.add_book(book)
    lib.remove_book("456")
    assert lib.find_book("456") is None
