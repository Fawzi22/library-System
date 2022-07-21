from Client import Client
from Libararyan import Librarian
from book import Book
from broow import Borrowing_order
from  datetime import timedelta,date
import random


users = []
librarians = []
books = []
borrowed_order = []

books.append(Book('In Search of Lost Time','Swanns Way, the first part of A la recherche de temps perdu','Marcel Proust'  ))
books.append(Book('Ulysses ','Ulysses chronicles the passage of Leopold Bloom through Dublin during an ordinary day','James Joyce'  ))
books.append(Book('Don Quixote','Alonso Quixano, a retired country gentleman in his fifties','Miguel de Cervantes'  ))
books.append(Book('The Great Gatsby','The novel chronicles an era that Fitzgerald himself dubbed the ','F. Scott Fitzgerald'  ))
books.append(Book('Moby Dick','First published in 1851, Melvilles masterpiece is, in Elizabeth Hardwicks words','Herman Melville'  ))
books.append(Book('War and Peace','Epic in scale, War and Peace delineates in graphic detail events leading up to Napoleons invasion of Russia','Leo Tolstoy'  ))

def add_client():
    print('*-*-*-*-*-*')
    users.append(Client(str(input("Your name : ")),int(input('Your age : ')),str(input('Your ID number : ')),int(input('Your phone number : '))))
    print('*-*-*-*-*-*')

def add_librarians():
    print('*-*-*-*-*-*')
    for i in range(int(input("How many Librarian : "))):
        librarians.append(Librarian(str(input("His name : ")),int(input('His age : ')),str(input('His ID number : ')),int(input('His phone number : ')) , int(input('His Salary : '))))
        print('*-*-*-*-*-*')

def borrow_books():
    print('*-*-**-*-**-*-**-*-**-*-**-*-**-*-*')
    for j in books:
        print(j.display())
    bk = int ( input('-------> Select your book : '))
    for i in range (len(books)):
        if bk == ( books[i].get_id() ):
            print('its here : ' , bk)
            borrowed_order.append(Borrowing_order(bk , int(input('Enter your ID : ')) ,'Ordered' ))
            if len(users) == 0 :
                print('------------------\n Please Add client to order !')
            else:
                del books[i]
                print('*-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-*\n' , 'Your order : ')
            for info in borrowed_order:
                print(info.display())

            break
    print('*-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-**-*-*-*')
    for j in books:
        print(j.display())

def return_book():
    rb = int ( input('-------> Select your book : '))
    for i in range (len(borrowed_order)):
        if rb == ( borrowed_order[i].get_book_id() ):
            books.append(borrowed_order[i])


while True:
    print("--------------------------- Welcome In library System ----------------------------------")
    choice = int(input("1.Add Client\n2.Add Librarian\n3.Borrow book\n4.Return Book\n5.Exit\nWhat do you want to do? :"))
    if choice == 1 :
        add_client()
    if  choice == 2 :
        add_librarians()
    if choice == 3 :
        borrow_books()
    if choice == 4 :
        return_book()
    if choice == 5 :
        exit()

