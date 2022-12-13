import datetime
import os


class LMS:
    #This class is used to keep records of books library

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id): {'books_title': line.replace("\n", ""), 'lender_name': '', 'lend_date': '',
                                              'status': 'Available'}})
            id += 1

    def search_bookname (self):
        fh = open("list_of_books.txt","r")
        word = input("Enter book name (only initial word) (ALL IN CAPS) : ")
        s = "   "
        count = 1

        while (s):
            s = fh.readline()
            li = s.split()
            '''SPLITS A STRING INTO LIST'''
            if word in li :
                print("Line number:", count, ":", s)
            count += 1

    def search_bookauthor (self):
        fh = open("list_of_books.txt","r")
        word = input("Enter book author (Either first or last name) (First Letter Of Word In Caps) : ")
        s = " "
        count = 1

        L = fh.readlines()

        for i in L:
            L2 = i.split()
            if word in L2 :
                print("Line number:", count, ":", i)
            count += 1

    def display_books_with_status(self):
        print("------------------------List of Books---------------------")
        print("Book ID", "\t", "Title")
        print("----------------------------------------------------------")
        for key, value in self.books_dict.items():
            print("\t", key, "\t", value.get("books_title"), "- [", value.get("status"), "]")

    def issue_books(self):
        books_id = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] == 'Available':
                print(
                    f"Issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
                return self.issue_books()
            elif self.books_dict[books_id]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['lend_date'] = current_date
                self.books_dict[books_id]['status'] = 'Already Issued'
                print("Book Issued Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")
            return self.issue_books()

    def add_books(self):
        new_books = input("Enter Books 'TITLE = Author' (follow this format only) : ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 50:
            print("Books title length is too long !!! Title length limit is 50 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict)) + 1): {'books_title': new_books, 'lender_name': '',
                                                                         'lend_date': '', 'status': 'Available'}})
            print(f"The books '{new_books}' has been added successfully !!!")

    def reserve_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif self.books_dict[books_id]['status'] == 'Already Issued':
                your_name = input("Enter Your Name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['status'] = 'Already Issued + Reserved'
                print("Book Reserved Successfully !!!\n")
            elif self.books_dict[books_id]['status'] == 'Already Issued + Reserved':
                print("This book is issued+reserved. Two people cannot reserve the same book.")
                return self.return_books()
            else:
                print("Book ID Not Found !!!")

    def return_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['status'] = 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")


if __name__ == "__main__": #Code that should only be run when file is executed as script
    try:
        mylms = LMS("list_of_books.txt", "Python's")
        press_key_list = {"N": "Search b_name", "B": "Search b_author", "D": "Display Books + Status", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "S": "Reserve Books", "Q": "Quit"}

        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "n":
                print("\nCurrent Selection : SEARCH BOOK BY BOOK NAME\n")
                mylms.search_bookname()

            elif key_press == "b":
                print("\nCurrent Selection : SEARCH BOOK BY BOOK AUTHOR\n")
                mylms.search_bookauthor()

            elif key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.issue_books()

            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display_books_with_status()

            elif key_press == "s":
                print("\nCurrent Selection : RESERVE BOOK\n")
                mylms.reserve_books()

            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_books()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")