import sqlite3
import sys
mycon=sqlite3.Connection("book.db")
mycur=mycon.cursor()

def Create_Table():
    try:
        mycur.execute("""CREATE TABLE BOOKS (id varchar(25) primary key, name varchar(25),author varchar(25),
        price int)""")
        print("Table Created Successfully.")
    except:
        print("Table already exists.")
                                                                      
def Add_Book():
    sql="Insert into BOOKS(id,name,author,price)values(?,?,?,?)"
    print('\nPLEASE PROVIDE THE REQUIRED INFORMATION\n')
    book_id=input('\nEnter the Book ID:  ')
    book_name=input('\nEnter the Books name: ')
    aut_name=input("\nEnter the Author's name: ")
    book_price=int(input("\nEnter the Book's Price: "))
    
    value=(book_id,book_name,aut_name,book_price)
    try:
        mycur.execute(sql,value)
        print('New Book Added Successfully.')
        mycon.commit()
    except:
        print('Error in Insertion. Please try again.')


def Show_All_Books():
    sql1='Select * from BOOKS'

    mycur.execute(sql1)
    rec1=mycur.fetchall()
    print("ID\t\tNAME\t\tAUTHORS NAME\t\tPRICE")
    for x in rec1:
         book_id=x[0]
         book_name=x[1]
         aut_name=x[2]
         book_price=x[3]
         
         print(book_id,'\t\t',book_name,'\t\t',aut_name,'\t\t',book_price)

def Search_Book(id=0):
    sql1="Select * from BOOKS where id=?"
    d=input("Enter Books ID:")
    value=(d,)
    mycur.execute(sql1,value)
    rec1=mycur.fetchall()
    print("ID\t\tNAME\t\tAUTHORS NAME\t\tPRICE")
    for x in rec1:
         book_id=x[0]
         book_name=x[1]
         aut_name=x[2]
         book_price=x[3]
         
         print(book_id,'\t\t',book_name,'\t\t',aut_name,'\t\t',book_price)
         
def Edit_Book():
     print("Current Data in DB")
     Show_All_Books()
     sql="Update BOOKS set price=? where id=?";
     new_id=input('\nEnter the books ID:')
     new_price=int(input('\nEnter the new Price:'))
     value=(new_price,new_id)
     try:
        mycur.execute(sql,value)
        mycon.commit()
        print('Rcord Updated Succesfully.')
        Show_All_Books()
     except:
        print('Error in Updating record. Please try again.')

def Delete_Book():
     print("Current Data in DB")
     Show_All_Books()
     d=int(input('\nEnter the Books ID to Delete:'))
     sql='Delete from BOOKS where id=?'
     value=(d,)
     try:
        mycur.execute(sql,value)
        mycon.commit()
        print('Rcord Deleted Successfully.')
        Show_All_Books()
     except:
          mycon.rollback()
          print('Error In Deleting Record.')
     Show_All_Books()
     
def Close():
    print('\nThank you for using our System. Have a great Day.')
    sys.exit(1)

print('-----------WELCOME TO BOOK MANAGMENT SYSTEM -------------\n')
while(True):
    print('\nPRESS 1 to Add a New Book')
    print('Press 2 to Show All Books')
    print('Press 3 to Edit a Book Detail')
    print('Press 4 to Delete a Books Record')
    print('Press 5 to Search a Book by ID')
    print('Press 6 to close the Application')
    print('Press 0 to Create the Table')
    choice=int(input('ENTER YOUR CHOICE : '))
    if(choice==1):
        Add_Book()
        
    elif(choice==2):
        Show_All_Books()
        
    elif(choice==3):
        Edit_Book()
        
    elif(choice==4):
         Delete_Book()
         
    elif(choice==5):
        Search_Book()
        
    elif(choice==6):
         Close()
         
    elif(choice==0):
        Create_Table()
