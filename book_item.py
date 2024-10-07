from check_items import *
class Book_item:
    def append_book(book_title,author,new_copies):
        mycursor.execute('''SELECT * FROM books''')
        List = mycursor.fetchall()
        for Tuple in List:
            if Tuple[1]==book_title and Tuple[2]==author:
                print('we have this book and i append it in copies!')
                book_item.append_copies(book_title,new_copies)
                return False
        v=[(book_title,author,new_copies)]
        mycursor.executemany('''INSERT INTO books (title,author,copies) VALUES (%s,%s,%s)''',v)
    def append_copies(book_title,app_copies):
        try:
            sql= "SELECT copies FROM books WHERE title= '" + book_title + "'"
            mycursor.execute(sql)
            List = mycursor.fetchall()
            copies= -1
            for data in List:
                copies=data[0]
                break
            if copies>=0:
                copies += app_copies
                mycursor.execute("UPDATE books SET copies='"+str(copies)+"' WHERE title='"+book_title+"'")
            else:
                print("we don't have this book!!")
        except:
            raise Exception("we don't have this book!?")
    def borrowing_book(book_name,username):
        try:
            mycursor.execute("SELECT copies FROM books WHERE title='"+book_name+"'")
            List=mycursor.fetchall()
            Tuple=List[0]
            copies=int(Tuple[0])
            if copies>0:
                copies -= 1
                mycursor.execute("UPDATE books SET copies='"+str(copies)+"' WHERE title='"+book_name+"'")
                mycursor.execute("SELECT books FROM members WHERE name='"+username+"'")
                List=mycursor.fetchall()
                Tuple=List[0]
                books=Tuple[0]
                if books=='Without book':
                    books=book_name
                else:
                    books +='&'+book_name
                mycursor.execute("UPDATE members SET books='"+books+"' WHERE name='"+username+"'")
            else:
                print("we don't have it!")
        except:
            raise Exception("we don't have it!!!")
        if book_name=='exit':
            return 'exit'
        else:
            return True
    def return_book(book_return,username):
        try:
            mycursor.execute("SELECT copies FROM books WHERE title='"+book_return+"'")
            List=mycursor.fetchall()
            Tuple=List[0]
            copies=int(Tuple[0])
            if copies>=0:
                copies += 1
                mycursor.execute("UPDATE books SET copies='"+str(copies)+"' WHERE title='"+book_return+"'")
                mycursor.execute("SELECT books FROM members WHERE name='"+username+"'")
                List=mycursor.fetchall()
                Tuple=List[0]
                books=Tuple[0].split('&')
                new_books=""
                if len(books)>1:
                    times=0
                    for book in books:
                        times += 1
                        if book!=book_return:
                            if times==len(books):
                                new_books += book
                            else:
                                new_books += (book+'&')
                    if len(new_books.split('&'))<len(books)-1:
                        Delta_x=(len(books)-1-len(new_books.split('&')))
                        for i in range(Delta_x):
                            books += str(book_return)
                else:
                    new_books='Without book'
                mycursor.execute("UPDATE members SET books='"+new_books+"' WHERE name='"+username+"'")
        except:
            raise Exception("we don't have this book in here! maybe you write its name false!")
        if book_return=='exit':
            return 'exit'
        else:
            return True
            # except:
           #     print("we don't have this book in library maybe you write its name False!!!")
book_item=Book_item