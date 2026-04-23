import datetime 
library_rows = {} 
books = {} 
users = {} 
borrow_records = {} 
 
# -------------------------------- 
# 1. Register User 
# -------------------------------- 
def register_user(): 
    print("\n----- USER REGISTRATION -----") 
 
    user_id = input("Enter User ID: ") 
    name = input("Enter User Name: ") 
    phone = input("Enter Phone Number: ") 
 
    users[user_id] = { 
        "name": name, 
        "phone": phone 
    } 
 
    print("User registered successfully!\n") 
 
 
# -------------------------------- 
# 2. Setup Library Rows 
# -------------------------------- 
def setup_library_rows(): 
    print("\n----- LIBRARY ROW SETUP -----") 
 
    rows = int(input("Enter number of rows in library: ")) 
 
    for i in range(1, rows + 1): 
        count = int(input(f"How many books in Row {i}: ")) 
        library_rows[i] = count 
 
    print("Library rows created successfully!\n") 
 
 
# -------------------------------- 
# 3. Add Books 
# -------------------------------- 
def add_books(): 
    print("\n----- ADD BOOKS -----") 
 
    book_id = input("Enter Book ID: ") 
    title = input("Enter Book Title: ") 
    author = input("Enter Author Name: ") 
    category = input("Enter Category (Comic/Thriller/Mystery/Fantasy/etc): ") 
    row = int(input("Enter Row Number: ")) 
 
    books[book_id] = { 
        "title": title, 
        "author": author, 
        "category": category, 
        "row": row, 
        "available": True 
    } 
 
    print("Book added successfully!\n") 
 
 
# -------------------------------- 
# 4. Display Library Books 
# -------------------------------- 
def display_books(): 
    print("\n----- LIBRARY BOOK LIST -----") 
 
    if not books: 
        print("No books in library\n") 
        return 
 
    for book_id, info in books.items(): 
        print(f""" 
Book ID     : {book_id} 
Title       : {info['title']} 
Author      : {info['author']} 
Category    : {info['category']} 
Row         : {info['row']} 
Available   : {info['available']} -----------------------------""") 
 
 
# -------------------------------- 
# 5. Search Books by Category 
# -------------------------------- 
def search_by_category(): 
    print("\n----- SEARCH BY CATEGORY -----") 
 
    category = input("Enter category: ") 
 
    found = False 
 
    for book_id, info in books.items(): 
        if info["category"].lower() == category.lower(): 
            print(info["title"], "-", info["author"]) 
            found = True 
 
    if not found: 
        print("No books found in this category") 
 
 
# -------------------------------- 
# 6. Borrow Book 
# -------------------------------- 
def borrow_book(): 
    print("\n----- BORROW BOOK -----") 
 
    user_id = input("Enter User ID: ") 
    book_id = input("Enter Book ID: ") 
 
    if book_id not in books: 
        print("Book not found") 
        return 
 
    if not books[book_id]["available"]: 
        print("Book already borrowed") 
        return 
 
    date = datetime.date.today() 
 
    borrow_records[book_id] = { 
        "user_id": user_id, 
        "borrow_date": date, 
        "return_date": None 
    } 
 
    books[book_id]["available"] = False 
 
    print("Book borrowed successfully on", date) 
 
 
# -------------------------------- 
# 7. Return Book 
# -------------------------------- 
def return_book(): 
    print("\n----- RETURN BOOK -----") 
 
    book_id = input("Enter Book ID: ") 
 
    if book_id not in borrow_records: 
        print("No record found") 
        return 
 
    date = datetime.date.today() 
 
    borrow_records[book_id]["return_date"] = date 
    books[book_id]["available"] = True 
 
    print("Book returned on", date) 
 
 
# -------------------------------- 
# 8. View Borrow Records 
# -------------------------------- 
def view_records(): 
    print("\n----- BORROW RECORDS -----") 
 
    if not borrow_records: 
        print("No borrow records") 
        return 
 
    for book_id, record in borrow_records.items(): 
        print(f""" 
Book ID      : {book_id} 
User ID      : {record['user_id']} 
Borrow Date  : {record['borrow_date']} 
Return Date  : {record['return_date']} 
---------------------------""") 
 
 
# ================================= 
#            MAIN MENU 
# ================================= 
while True: 
 
    print(""" 
==================================== 
        MAJESTIC LIBRARY SYSTEM 
==================================== 
 
1. Register User 
2. Setup Library Rows 
3. Add Books 
4. Display Books 
5. Search Books by Category 
6. Borrow Book 
7. Return Book 
8. View Borrow Records 
9. Exit 
""") 
 
    choice = input("Enter your choice: ") 
 
    if choice == "1": 
        register_user() 
 
    elif choice == "2": 
        setup_library_rows() 
 
    elif choice == "3": 
        add_books() 
 
    elif choice == "4": 
        display_books() 
 
    elif choice == "5": 
        search_by_category() 
 
    elif choice == "6": 
        borrow_book() 
 
    elif choice == "7": 
        return_book() 
 
    elif choice == "8": 
        view_records() 
 
    elif choice == "9": 
        print("Thank you for using Majestic Library System") 
        break 
 
    else: 
        print("Invalid choice")
