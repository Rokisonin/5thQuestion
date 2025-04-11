from book import Book, Author

# Create Author
author1 = Author("George Orwell", "British")
author2 = Author("Haruki Murakami", "Japanese")

# Create Books using composition
book1 = Book("1984", author1, 1949)
book2 = Book("Kafka on the Shore", author2, 2002)

# Set publishers using nested class
book1.set_publisher("Secker & Warburg", "London")
book2.set_publisher("Shinchosha", "Tokyo")

# Output
print(book1)
print(book2)
print(f"Is '{book1.title}' a classic? {'Yes' if Book.is_classic(book1.year) else 'No'}")
print(f"Is '{book2.title}' a classic? {'Yes' if Book.is_classic(book2.year) else 'No'}")
