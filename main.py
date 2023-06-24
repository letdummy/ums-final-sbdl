# import
import mysql.connector
import datetime


# mainMenu
def main_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Login as Member")
    print("2. Login as Admin")
    print("3. Exit")


# member menu
def login_member():
    print("\n================================= Library UMS ================================\n")
    if login_member_id == "01":
        print("Welcome, Member 1")
        login_member_menu()
    elif login_member_id == "02":
        print("Welcome, Member 2")
        login_member_menu()
    elif login_member_id == "03":
        print("Welcome, Member 3")
        login_member_menu()
    elif login_member_id == "04":
        print("Welcome, Member 4")
        login_member_menu()
    elif login_member_id == "05":
        print("Welcome, Member 5")
        login_member_menu()
    else:
        print("ID not found")
def login_member_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. Display Borrowed Book")
    print("4. Exit")


# admin menu
def login_admin_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Display Book List")
    print("4. Logout")


# member
def borrow_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Start borrow a Book")
    print("2. Back to Member Menu")
    print("3. Exit")


def return_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Return a Book")
    print("2. Back to Member Menu")
    print("3. Exit")


def display_borrowed_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Display Borrowed Book")
    print("2. Back to Member Menu")
    print("3. Exit")


# admin
def add_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Start to add book")
    print("2. Back to Admin Menu")
    print("3. Logout")


def remove_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Remove a Book")
    print("2. Back to Admin Menu")
    print("3. Logout")


def display_book_list_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Display Book List")
    print("2. Back to Admin Menu")
    print("3. Exit")

# feature member
def show_borrowed_book(user_input):
    data = mysql.connector.connect(user="root", database="library_team")
    cursor = data.cursor()

    query = ("SELECT book.book_id, book.book_title "
             "FROM book "
             "LEFT JOIN loan ON book.book_id = loan.book_id "
             f"WHERE member_id = '{user_input}'")

    cursor.execute(query)

    print("\n======= Borrowed Book list by Member =======")
    for (book_id, book_title) in cursor:
        print(f"{book_id}. {book_title}")
    print()

    cursor.close()
    data.close()


# feature admin
def show_author_db():
    data = mysql.connector.connect(user='root', database='library_team')
    cursor = data.cursor()

    query = ("SELECT * FROM author")

    cursor.execute(query)
    print("\n========== Author List ==========")
    for (id_author, author_name) in cursor:
        print(f"{id_author}. {author_name}")
    print()
    cursor.close()
    data.close()


def show_author_book(user_input):
    data = mysql.connector.connect(user="root", database="library_team")
    cursor = data.cursor()

    query = ("SELECT book.book_id, book.book_title "
             "FROM book "
             "LEFT JOIN author_write_book ON book.book_id = author_write_book.book_id "
             f"WHERE author_id = '{user_input}'")

    cursor.execute(query)

    print("\n======= Book list by Author =======")
    for (book_id, book_title) in cursor:
        print(f"{book_id}. {book_title}")
    print()

    cursor.close()
    data.close()


def remove_book(user_input):
    data = mysql.connector.connect(user="root", database="library_team")
    cursor = data.cursor()

    query = (f"DELETE FROM book WHERE book_id = '{user_input}'")

    cursor.execute(query)

    data.commit()
    cursor.close()
    data.close()

    print("\n========== Book removed successfully ==========")


def show_all_book():
    data = mysql.connector.connect(user="root", database="library_team")
    cursor = data.cursor()

    query = ("SELECT author_name, book.book_id, book_title "
             "FROM book "
             "JOIN author_write_book ON book.book_id = author_write_book.book_id "
             "JOIN author ON author_write_book.author_id = author.author_id ")

    cursor.execute(query)

    print("\n========= Full Book list =========")
    for (author_name, book_id, book_title) in cursor:
        print(f"{book_id}. {book_title} || by {author_name}")

    cursor.close()
    data.close()


# Main Program
run_program = True
run_admin = True
run_add_book = True
run_member = True

while run_program:
    main_menu()

    main_input = input("Enter your choice: ")
    run_admin = True

    # member login logic
    if main_input == "1":
        while run_member:
            login_member_id = input("Enter your ID: ")
            login_member()

            member_input = input("Enter your choice: ")

            if member_input == "1":
                borrow_book_menu()

                borrow_book_input = input("Enter your choice: ")

                if borrow_book_input == "1":
                    show_all_book()
                    print("\n========== Borrow a Book ==========")

                    borrow_book_id = input("Enter book id: ")
                    date_now = datetime.datetime.now()
                    date_book_borrowed = date_now.strftime("%Y-%m-%d")
                    due_date = datetime.datetime.strptime(date_book_borrowed, "%Y-%m-%d") + datetime.timedelta(days=7)
                    due_return_date = due_date.strftime("%Y-%m-%d")

                    data = mysql.connector.connect(user='root', database='library_team')
                    cursor = data.cursor()

                    query = (f"INSERT INTO loan (book_id, member_id, loan_date, due_return_date) "
                             f"VALUES ('{borrow_book_id}', '{login_member_id}', '{date_book_borrowed}', '{due_return_date}')")
                    cursor.execute(query)

                    data.commit()
                    cursor.close()
                    data.close()

                    print("\n========== Book borrowed successfully ==========")
                elif borrow_book_input == "2":
                    login_member_menu()

            elif member_input == "2":
                return_book_menu()
                return_book_input = input("Enter your choice: ")

                # if return_book_input == "1":
                #     show borrowed book : bikin query yang menampilkan buku yang dipinjam oleh member
                #     return_book_id = input("Enter book id: ")

            elif member_input == "3":
                show_borrowed_book(login_member_id)

            elif member_input == "4":
                run_member = False
















    # admin login logic
    elif main_input == "2":
        while run_admin:
            login_admin_menu()

            admin_input = input("Enter your choice: ")

            if admin_input == "1":
                add_book_menu()

                add_book_input = input("Enter your choice: ")

                if add_book_input == "1":
                    new_book_id = input("Enter book id: ")
                    new_book_title = input("Enter book title: ")
                    show_author_db()
                    new_book_author = input("Enter book's author: ")
                    data = mysql.connector.connect(user='root', database='library_team')
                    cursor = data.cursor()

                    query = (f"INSERT INTO book (book_id, book_title) VALUES ('{new_book_id}', '{new_book_title}')")

                    cursor.execute(query)

                    query2 = (
                        f"INSERT INTO author_write_book (book_id, author_id) VALUES ('{new_book_id}', '{new_book_author}')")

                    cursor.execute(query2)

                    data.commit()
                    cursor.close()
                    data.close()

                    print("\n========== Book added successfully ==========")

                elif add_book_input == "2":
                    print("\n============= Add book Canceled =============")

                elif add_book_input == "3":
                    print("Logging out...")
                    run_admin = False

            elif admin_input == "2":
                print("Remove a Book")

                remove_book_menu()

                remove_book_input = input("Enter your choice: ")

                if remove_book_input == "1":
                    show_author_db()
                    remove_author_book = input("Which author you wish to remove the book from: ")
                    show_author_book(remove_author_book)

                    remove_book_id = input("Which book from chosen author you wish to remove: ")
                    remove_book(remove_book_id)

                elif remove_book_input == "2":
                    print("\n=========== Remove book Canceled ============")

                elif remove_book_input == "3":
                    print("Logging out...")
                    run_admin = False

            elif admin_input == "3":
                show_all_book()

            elif admin_input == "4":
                print("Logging out...")
                run_admin = False

    # exit logic
    elif main_input == "3":
        print("Exiting program...")
        run_program = False

    # invalid input logic
    else:
        print("Invalid Input, exiting program...")
        run_program = False
