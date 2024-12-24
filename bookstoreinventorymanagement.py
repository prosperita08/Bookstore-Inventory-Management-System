books = []

def display_menu():
    print("\nBookstore Inventory Management System")
    print("1. Add Book")
    print("2. View Available Books")
    print("3. Search Book")
    print("4. Update Book Details")
    print("5. Delete Book")
    print("6. Exit")

def add_book():
    book_title = input("Enter book title: ")
    author = input("Enter author name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    book = {"Title": book_title, "Author": author, "Quantity": quantity, "Price": price}
    books.append(book)
    print("Book added to inventory successfully!")

def view_available_books():
    if not books:
        print("No books available in the inventory.")
    else:
        print("\nAvailable Books:")
        for idx, book in enumerate(books, start=1):
            print(f"{idx}. Title: {book['Title']}, Author: {book['Author']}, Quantity: {book['Quantity']}, Price: {book['Price']}")

def search_book():
    search_term = input("Enter book title or author to search: ")
    found_books = [book for book in books if search_term.lower() in book['Title'].lower() or search_term.lower() in book['Author'].lower()]

    if not found_books:
        print("No matching books found.")
    else:
        print("\nMatching Books:")
        for idx, book in enumerate(found_books, start=1):
            print(f"{idx}. Title: {book['Title']}, Author: {book['Author']}, Quantity: {book['Quantity']}, Price: {book['Price']}")

def update_book():
    view_available_books()
    if not books:
        return

    try:
        book_idx = int(input("Enter book number to update: ")) - 1
        updated_quantity = int(input("Enter updated quantity: "))
        updated_price = float(input("Enter updated price: "))

        books[book_idx]['Quantity'] = updated_quantity
        books[book_idx]['Price'] = updated_price

        print("Book details updated successfully!")
    except IndexError:
        print("Invalid book number.")

def delete_book():
    view_available_books()
    if not books:
        return

    try:
        book_idx = int(input("Enter book number to delete: ")) - 1
        deleted_book = books.pop(book_idx)
        print(f"Book '{deleted_book['Title']}' deleted successfully!")
    except IndexError:
        print("Invalid book number.")

def run():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_available_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Exiting Bookstore Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    run()
