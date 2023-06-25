# import
import mysql.connector
import datetime


# mainMenu
def main_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Login as Member")
    print("2. Login as Admin")
    print("3. Exit")


def show_all_member():
    data = mysql.connector.connect(user="root", database="library_team")
    cursor = data.cursor()

    query = ("SELECT member_id, member_name FROM member")

    cursor.execute(query)

    print("\n========= Member List =========")
    for (member_id, member_name) in cursor:
        print(f"{member_id}. {member_name}")
    print("\n99. Back to Main Menu")
    cursor.close()
    data.close()


def filter_input_author(user_input):
    str(user_input)
    if user_input == "1" or user_input == "01":
        return "01"
    elif user_input == "2" or user_input == "02":
        return "02"
    elif user_input == "3" or user_input == "03":
        return "03"
    elif user_input == "4" or user_input == "04":
        return "04"
    elif user_input == "5" or user_input == "05":
        return "05"
    else:
        raise ValueError("Invalid input: Please input a number between 1-5")


def filter_input_book(user_input):
    str(user_input)
    if user_input == "1" or user_input == "01":
        return "01"
    elif user_input == "2" or user_input == "02":
        return "02"
    elif user_input == "3" or user_input == "03":
        return "03"
    elif user_input == "4" or user_input == "04":
        return "04"
    elif user_input == "5" or user_input == "05":
        return "05"
    elif user_input == "6" or user_input == "06":
        return "06"
    elif user_input == "7" or user_input == "07":
        return "07"
    elif user_input == "8" or user_input == "08":
        return "08"
    elif user_input == "9" or user_input == "09":
        return "09"
    else:
        return user_input

# member menu
def login_member(user_input):
    print("\n================================= Library UMS ================================\n")
    data = mysql.connector.connect(user="root", database="library_team")
    cursor = data.cursor()

    query = (f"SELECT member_name FROM member WHERE  member_id = {user_input}")

    cursor.execute(query)

    for (member_name) in cursor:
        return (member_name[0])

    cursor.close()
    data.close()


def login_member_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. Display Borrowed Book")
    print("4. Logout")


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
    print("3. Logout")


def return_book_menu():
    print("\n================================= Library UMS ================================\n")
    print("1. Return a Book")
    print("2. Back to Member Menu")
    print("3. Logout")


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
             f"WHERE member_id = '{user_input}' AND return_date IS NULL ORDER BY book_id")

    cursor.execute(query)

    print(f"\n======= Borrowed Book list by {login_member(login_member_id)} =======")
    for (book_id, book_title) in cursor:
        print(f"{book_id}. {book_title}")

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

    query2 = (f"DELETE FROM author_write_book WHERE book_id = '{user_input}'")
    cursor.execute(query2)

    data.commit()
    cursor.close()
    data.close()

    print("\n========== Book removed successfully ==========")


def show_all_book(user_input=0):
    data = mysql.connector.connect(user="root", database="library_team")
    cursor = data.cursor()

    query = ("SELECT author_name, book.book_id, book_title "
             "FROM book "
             "JOIN author_write_book ON book.book_id = author_write_book.book_id "
             "JOIN author ON author_write_book.author_id = author.author_id "
             "LEFT JOIN loan ON book.book_id = loan.book_id "
             "WHERE book.book_id NOT IN ("
             "    SELECT loan.book_id "
             "    FROM loan "
             f"   WHERE loan.member_id = {user_input} AND return_date IS NULL)"
             "GROUP BY book.book_id ORDER BY book.book_id")

    cursor.execute(query)

    print("\n========= Full Book list =========")
    for (author_name, book_id, book_title) in cursor:
        print(f"{book_id}. {book_title} || by {author_name}")

    cursor.close()
    data.close()


def get_due_return(member_id, book_id):
    data = mysql.connector.connect(user="root", database="library_team")
    cursor = data.cursor()

    query = ("SELECT due_return_date "
             "FROM loan "
             f"WHERE member_id = '{member_id}' AND book_id = '{book_id}'")

    cursor.execute(query)

    for (due_return_date) in cursor:
        return (due_return_date[0])

    cursor.close()
    data.close()


# Main Program
run_program = True

run_admin = True
run_add_book = True

run_member = True
run_borrow_book = True
run_return_book = True

while run_program:
    main_menu()

    main_input = input("Enter your choice: ")

    # member login logic
    if main_input == "1":
        show_all_member()
        print()
        login_member_id = filter_input_author(input("Enter your ID: "))
        if login_member_id == "99":
            print("You are now in main menu")
            run_member = False
        else:
            print("Welcome to Library UMS,", login_member(login_member_id))
            run_member = True

        while run_member:
            login_member_menu()
            print()
            member_input = input("Enter your choice: ")

            # borrow a book logic
            if member_input == "1":
                run_borrow_book = True
                while run_borrow_book:
                    borrow_book_menu()
                    borrow_book_input = input("Enter your choice: ")

                    if borrow_book_input == "1":
                        run_borrow_book = True
                        show_all_book(login_member_id)
                        print("\n========== Borrow a Book ==========")

                        borrow_book_id = filter_input_book(input("Enter book ID: "))

                        date_book_borrowed = datetime.datetime.now().strftime("%Y-%m-%d")
                        due_return_date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")

                        data = mysql.connector.connect(user='root', database='library_team')
                        cursor = data.cursor()

                        query = (f"INSERT INTO loan (book_id, member_id, loan_date, due_return_date) "
                                 f"VALUES ('{borrow_book_id}', '{login_member_id}', '{date_book_borrowed}', '{due_return_date}')")
                        cursor.execute(query)

                        data.commit()
                        cursor.close()
                        data.close()

                        print("\n========== Book borrowed successfully ==========")
                        print(f"========== Due return date: {due_return_date} =========")

                    elif borrow_book_input == "2":
                        print("\n=========== Borrow book Canceled ============")
                        run_borrow_book = False

                    elif borrow_book_input == "3":
                        print("Logging out...")
                        run_borrow_book = False
                        run_member = False

            elif member_input == "2":
                run_return_book = True
                while run_return_book:
                    return_book_menu()
                    return_book_input = input("Enter your choice: ")

                    if return_book_input == "1":
                        show_borrowed_book(login_member_id)
                        print("\n========== Return a Book ==========")

                        return_book_id = filter_input_book(input("Enter book ID: "))
                        date_now = datetime.datetime.now().date()
                        due_return_date = get_due_return(login_member_id, return_book_id)

                        days_difference = (date_now - due_return_date).days

                        if days_difference >= 10:
                            lateness_tax = 50000
                        elif days_difference > 0:
                            lateness_tax = days_difference * 5000
                        else:
                            lateness_tax = 0

                        data = mysql.connector.connect(user='root', database='library_team')
                        cursor = data.cursor()

                        query = (
                            f"UPDATE loan "
                            f"SET return_date = '{date_now}', lateness_tax = '{lateness_tax}' "
                            f"WHERE member_id = '{login_member_id}' AND book_id = '{return_book_id}'"
                        )

                        cursor.execute(query)

                        data.commit()
                        cursor.close()
                        data.close()

                        print("\n========== Book returned successfully ==========")
                        print(f"========== Due return date: {due_return_date} =========")
                        print(f"========== Book return date: {date_now} =========")
                        print(f"========== Lateness Tax: Rp{lateness_tax} =========")

                    elif return_book_input == "2":
                        print("\n=========== Return book Canceled ============")
                        run_return_book = False

                    elif return_book_input == "3":
                        print("Logging out...")
                        run_return_book = False
                        run_member = False

            # display borrowed book logic
            elif member_input == "3":
                show_borrowed_book(login_member_id)

            # logout logic
            elif member_input == "4":
                print("Logging out...")
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
                    new_book_id = filter_input_book(input("Enter book id: "))
                    new_book_title = input("Enter book title: ")
                    show_author_db()
                    new_book_author = filter_input_author(input("Enter book's author: "))
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
                    remove_author_book = filter_input_author(input("Which author you wish to remove the book from: "))
                    show_author_book(remove_author_book)

                    remove_book_id = filter_input_book(input("Which book from chosen author you wish to remove: "))
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
