from book import Book, Author

# Create two authors (Composition — Author objects will be embedded into Books)
author1 = Author("George Orwell", "British")
author2 = Author("Haruki Murakami", "Japanese")

# Create book instances using Author objects
book1 = Book("1984", author1, 1949)
book2 = Book("Kafka on the Shore", author2, 2002)

# Assign publishers to books using nested Publisher class (Composition)
book1.set_publisher("Secker & Warburg", "London")
book2.set_publisher("Shinchosha", "Tokyo")

# Print full details of the books (uses __str__)
print(book1)  # Includes title, author, year, publisher
print(book2)

# Use static method to check if each book is a "classic"
print(f"Is '{book1.title}' a classic? {'Yes' if Book.is_classic(book1.year) else 'No'}")
print(f"Is '{book2.title}' a classic? {'Yes' if Book.is_classic(book2.year) else 'No'}")
