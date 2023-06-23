# import
import mysql.connector


# mainMenu
def main_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Login as Member")
    print("2. Login as Admin")
    print("3. Exit")


# member menu
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
    print("1. Borrow a Book")
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
    print("3. Exit")


def remove_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Remove a Book")
    print("2. Back to Admin Menu")
    print("3. Exit")


def display_book_list_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Display Book List")
    print("2. Back to Admin Menu")
    print("3. Exit")


def show_author_db():
    data = mysql.connector.connect(user='root', database='library_team')
    cursor = data.cursor()

    query = ("SELECT * FROM author")

    cursor.execute(query)
    for (id_author, author_name) in cursor:
        print(f"{id_author}. {author_name}")
    cursor.close()
    data.close()


def author_filter(user_input):
    if user_input == "01":
        return "01"
    elif user_input == "02":
        return "02"
    elif user_input == "03":
        return "03"
    elif user_input == "04":
        return "04"
    elif user_input == "05":
        return "05"
    else:
        return None


# Main Program
run_program = True
run_admin = True
run_add_book = True

while run_program:
    main_menu()

    main_input = input("Enter your choice: ")

    # member login logic
    if main_input == "1":
        print("Login as Member")

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
                    print("\n========== Author List ==========")
                    show_author_db()
                    print()
                    new_book_author = author_filter(input("Enter book author: "))
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

                    print("Book added successfully")



            elif admin_input == "2":
                print("Remove a Book")
            elif admin_input == "3":
                print("Display Book List")
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
