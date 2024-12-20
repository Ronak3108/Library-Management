import pandas as pd
from datetime import date


def login():
    uname = input("Enter Username : ")
    pwd = input("Enter Password : ")
    df = pd.read_csv("users.csv")
    df = df.loc[df["username"] == uname]
    if df.empty:
        print("Invalid Username given")
        return False
    else:
        df = df.loc[df["password"] == pwd]
        if df.empty:
            print("Invalid Password")
            return False
        else:
            print("Username and Password matched successfully")
            return True


def addNewBook():
    # Get the details of the new book from user input
    bookid = int(input("Enter a book id: "))
    title = input("Enter book title: ")
    author = input("Enter author of the book: ")
    publisher = input("Enter book publisher: ")
    edition = input("Enter edition of book: ")
    cost = float(input("Enter cost of the book: "))
    category = input("Enter category of book: ")

    # Load the current books data from the CSV file
    bdf = pd.read_csv("books.csv")

    # Create a new DataFrame for the new book
    new_book = pd.DataFrame([[bookid, title.lower(), author, publisher, edition, cost, category]],
                            columns=["bookid", "title", "author", "publisher", "edition", "cost", "category"])

    # Concatenate the new book to the existing DataFrame
    bdf = pd.concat([bdf, new_book], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    bdf.to_csv("books.csv", index=False)

    print("Book added successfully\n")
    print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
    prompt()




def searchBook():
    name = input("Enter book title to be searched : ")
    bdf = pd.read_csv("books.csv")
    df = bdf.loc[bdf["title"] == name.lower()]
    if df.empty:
        print("No book found with given title\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()
    else:
        print("Book details are : ")
        print(df)
        print("\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()

def deleteBook():
    name = input("Enter book title to be deleted : ")
    bdf = pd.read_csv("books.csv")
    tempdf = bdf.loc[bdf["title"] == name]

    if tempdf.empty:
        print("There is no book of such name in the library. Please try again\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()
    else:
        bdf = bdf.drop(bdf[bdf["title"] == name.lower()].index)
        bdf.to_csv("books.csv",index = False)
        print("Book DELETED Successfully\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()

def showBooks():
    bdf = pd.read_csv("books.csv")
    print(bdf)
    print("\n")
    print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
    prompt()


def addNewMember():
    # Get the details of the new member from user input
    mid = int(input("Enter Member id: "))
    name = input("Enter name of the member: ").lower()
    phone = input("Enter phone number: ")
    email = input("Enter email id: ")
    address = input("Enter address: ")
    
    # Load the current members data from the CSV file
    mdf = pd.read_csv("members.csv")

    # Create a new DataFrame for the new member
    new_member = pd.DataFrame([[mid, name, phone, email, address]],columns=["mid", "name", "phone", "email", "address"])

    # Concatenate the new member with the existing members DataFrame
    mdf = pd.concat([mdf, new_member], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    mdf.to_csv("members.csv", index=False)

    print("Member added successfully\n")
    print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
    prompt()



def searchMember():
    name = input("Enter member name to be searched : ").lower()
    mdf = pd.read_csv("members.csv")
    df = mdf.loc[mdf["name"] == name]
    if df.empty:
        print("No member found with given name\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()
    else:
        print("Member details are: ")
        print(df)
        print("\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()


def deleteMember():
    name = input("Enter member name to be deleted : ").lower()
    mdf = pd.read_csv("members.csv")
    tempdf = mdf.loc[mdf["name"] == name]

    if tempdf.empty:
        print("There is no member of such name registered. Please try again\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()
    else:
        mdf = mdf.drop(mdf[mdf["name"] == name].index)
        mdf.to_csv("members.csv", index=False)
        print("Member DELETED Successfully\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()

def showMembers():
    mdf = pd.read_csv("members.csv")
    print(mdf)
    print("\n")
    print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
    prompt()


def issueBook():
    bname = input("Enter Book name to be searched : ").lower()
    df = pd.read_csv("books.csv")
    df = df.loc[df["title"] == bname]
    if df.empty:
        print("No Book Found in the Library\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")   
        prompt()

    mname = input("Enter member name to be searched : ").lower()
    df = pd.read_csv("members.csv")
    df = df.loc[df["name"] == mname]  # Changed 'name' to 'Name' to match the column name
    if df.empty:
        print("No such Member Found\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()

    idf = pd.read_csv("issuedbooks.csv")
    book_issue = [bname, mname, date.today()]

    # Use len(idf) to get the index for the next available row
    n = len(idf)  

    # Append the new issue record to the DataFrame using loc[] (instead of at[])
    idf.loc[n] = book_issue

    # Save the updated DataFrame back to the issuedbooks.csv file
    idf.to_csv("issuedbooks.csv", index=False)
    print("Book Issued Successfully\n")
    print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
    prompt()


def showIssuedBooks():
    idf = pd.read_csv("issuedbooks.csv")
    print(idf)
    print("\n")
    print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
    prompt()


def returnBook():
    bname = input("Enter Book to be returned : ").lower()
    mname = input("Enter Member who has the book : ").lower()
    idf = pd.read_csv("issuedbooks.csv")
    idf = idf.loc[idf["book_name"] == bname]
    if idf.empty:
        print("The book is not issued in records\n")
        print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
        prompt()
    else:
        idf = idf.loc[idf["member_name"] == mname]
        if idf.empty:
            print("The book is not issued to the member\n")
            print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")    
            prompt()
        else:
            print("Book can be returned\n")
            ans = input("Are you sure you want to return the book : ")
            if ans.lower() == "yes":
                idf = pd.read_csv("issuedbooks.csv")
                idf = idf.drop(idf[idf["book_name"] == bname].index)
                idf.to_csv("issuedbooks.csv", index=False)
                print("Book Returned Successfully\n")
                print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")
                prompt()
            else:
                print("Return operation cancelled.\n")
                print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")              
                prompt()

def showMenu():
    print("-----------------------------")
    print("         MPS LIBRARY         ")
    print("-----------------------------")
    print("Press 1 - Add New Book")
    print("Press 2 - Search for a Book")
    print("Press 3 - Delete Book")
    print("Press 4 - Show All Books")
    print("Press 5 - Add New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 - Show Issuing Records")
    print("Press 12 - To Quit")
    choice = input("Enter your choice : ")
    return choice

    
        


def prompt():
    if login():
        print('\n')
        ans = input("Do you wish to perform any other tasks?: ").lower()
        if ans == "yes" or ans == "y":
            ch = showMenu()
            if ch == '1':
                addNewBook()
            elif ch == '2':
                searchBook()
            elif ch == '3':
                deleteBook()
            elif ch == '4':
               showBooks()
            elif ch == '5':
                addNewMember()
            elif ch == '6':
                searchMember()
            elif ch == '7':
                deleteMember()
            elif ch == '8':
                showMembers()
            elif ch == '9':
                issueBook()
            elif ch == '10':
                returnBook()
            elif ch == '11':
               showIssuedBooks()
            elif ch == '12':
                return 
            else:
               print("Invalid Option Selected\n")
               print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")              
               prompt()
        elif ans == "no" or ans == "n":
            return
        else:
            print("invalid input recieved. Try running the program if you want to..\n")
            print("ENTER YOUR LOGIN DETAILS AGAIN TO ACCESS THE PROGRAM AGAIN........")              
            prompt()
        
prompt()