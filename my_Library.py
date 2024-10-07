import csv
file=open('times.csv','r')
data=csv.reader(file)
header=next(data)
header=next(data)
times=int(header[0])
condition=str(times)
class Member:
    def __init__(self,member_name,member_ID,member_books):
        self.member_name=member_name
        self.member_ID=member_ID
        self.member_books=member_books
        file=open('members/members'+condition+'_info.csv','a',newline="")
        w=csv.writer(file)
        w.writerow([self.member_name,self.member_ID,self.member_books])
        file.close()
class Book:
    def __init__(self,book_name,book_author,book_copies):
        self.book_name=book_name
        self.book_author=book_author
        self.book_copies=book_copies
        file=open('books/books'+condition+'_info.csv','a',newline="")
        w=csv.writer(file)
        w.writerow([self.book_name,self.book_author,self.book_copies])
        file.close()
class Register:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        file=open('register.csv','a',newline="")
        w=csv.writer(file)
        w.writerow([self.username,self.password])
        file.close()
class Check:
    def check_for_register(check_item):
        if check_item=='usernames':
            find1=''
            while find1!=False:
                find1=''
                username=input('username: ')
                if len(username)>3:
                    file=open('members/members'+condition+'_info.csv','r')
                    data=csv.reader(file)
                    check_username=False
                    while check_username!=True:
                        try:
                            header=next(data)
                            if header[0]==username:
                                find1=True
                                print('another person used it!')
                        except:
                            check_username=True
                            if find1!=True:
                                find1=False
                else:
                    print('username should be greater from 3 letters!')
            return username
        if check_item=='IDies':
            line=1
            file=open('members/members'+condition+'_info.csv','r')
            data=csv.reader(file)
            check_ID=False
            while check_ID==False:
                try:
                    header=next(data)
                    line+=1
                except:
                    check_ID=True
                    ID=line
            return ID
        if check_item=='book_name':
            find3=''
            while find3!=False:
                find3=''
                book_name=input('book_name: ')
                file=open('books/books'+condition+'_info.csv','r')
                data=csv.reader(file)
                check_book_name=False
                while check_book_name!=True:
                    try:
                        header=next(data)
                        if header[0]==book_name:
                            find3=True
                            print('this book is in the library!')
                    except:
                        check_book_name=True
                        if find3!=True:
                            find3=False
            return book_name
        if check_item=='password':
            check_password=False
            while check_password!=True:
                password=input('password: ')
                if len(password)>5:
                    check_password=True
                else:
                    print('Password should be greater from 5 letters')
            return password
    def check_member():
        username=input('username: ')
        password=input('password: ')
        file=open('register.csv','r')
        data=csv.reader(file)
        find=False
        check_user=False
        while check_user==False:
            try:
                header=next(data)
                l_username=header[0]
                l_Password=header[1]
                if username==l_username:
                    if password==l_Password:
                        find=True
                    else:
                        password += '\n'
                        if password==l_Password:
                            find=True
            except:
                check_user=True
        if find==True:
            print('welcome')
        if find==False:
            print('information is false!')
        file.close()
        Touple=(username,password,find)
        return Touple
    ##############################################
    def check_books():
        file=open('books/books'+condition+'_info.csv','r')
        data=csv.reader(file)
        header=next(data)
        run2=True
        while run2==True:
            try:
                header=next(data)
                print(f'name is {header[0]} :::::: author is {header[1]} :::::: copies is {header[2]}')
            except:
                run2=False
        file.close()
    def check_one_book():
        book_name=input('book_name: ')
        file=open('books/books'+condition+'_info.csv','r')
        data=csv.reader(file)
        check_book=False
        find_book=False
        while check_book==False:
            try:
                header=next(data)
                if header[0]==book_name:
                    print(f'name is {header[0]} author is {header[1]} copies is {header[2]}')
                    copies=header[2] 
                    find_book=True
            except:
                check_book=True
        if find_book==True:
            return (book_name,copies)
        else:
            return False
    def check_one_ID():
        ID=input('ID: ')
        file=open('members/members'+condition+'_info.csv','r')
        data=csv.reader(file)
        find_ID=False
        check_ID=False
        while check_ID==False:
            try:
                header=next(data)
                if header[1]==ID:
                    print(f'name is {header[0]} ID is {header[1]} books is {header[2]}')
                    find_ID=True
            except:
                check_ID=True
        return find_ID
check=Check
def register():
        username=check.check_for_register('usernames')
        password=check.check_for_register('password')
        ID=check.check_for_register('IDies')
        member_book='~~~~'
        member=Member(username,ID,member_book)
        member_register=Register(username,password)
        return username
def run():
    if username=='Librarian' and password=='12345678':
        run1=True
        while run1==True:
            answer2=input('What do you want?(check_books,check_members,check_one_ID,check_one_book,append_book,exit)')
            if answer2=='check_books':
                check.check_books()
            if answer2=='check_members':
                file=open('members/members'+condition+'_info.csv','r')
                data=csv.reader(file)
                header=next(data)
                run3=True
                while run3==True:
                    try:
                        header=next(data)
                        print(f'name is {header[0]} :::::: ID is {header[1]} :::::: books is {header[2]}')
                    except:
                        run3=False
            if answer2=='append_book':
                file=open('books/books'+condition+'_info.csv','a',newline="")
                w=csv.writer(file)
                book_name=check.check_for_register('book_name')
                book_author=input('book_author: ')
                book_copies=input('book_copies: ')
                book=Book(book_name,book_author,book_copies)
                file.close()
            if answer2=='check_one_book':
                check.check_one_book()
            if answer2=='check_one_ID':
                check.check_one_ID()
            if answer2=='exit':
                run1=False
        return condition
    else:
        run4=True
        while run4==True:
            answer3=input('What do you want?(check_books,check_one_book,borrowing_book,return_book,check_my_information,exit)')
            if answer3=='check_books':
                check.check_books()
            if answer3=='check_one_book':
                check.check_one_book()
            if answer3=='check_my_information':
                file=open('members/members'+condition+'_info.csv','r')
                data=csv.reader(file)
                check_info=False
                while check_info==False:
                    try:
                        header=next(data)
                        if username==header[0]:
                            print(f'your username is {header[0]} ID is {header[1]} books is {header[2]}')
                    except:
                        check_info=True
            if answer3=='borrowing_book':
                Touple=check.check_one_book()
                try:
                    copies=Touple[1]
                    book_name=Touple[0]
                    answer4=input('Do you give it to member or not?')
                    if answer4=='yes':
                        file=open('times.csv','r')
                        data=csv.reader(file)
                        header=next(data)
                        header=next(data)
                        times=int(header[0])+1
                        new_condition=str(times)
                        file=open('members/members'+condition+'_info.csv','r')
                        data=csv.reader(file)
                        file2=open('members/members'+new_condition+'_info.csv','x')
                        file2.close()
                        check_members=False
                        while check_members==False:
                            try:
                                header=next(data)
                                if header[0]==username:
                                    if header[2]=='~~~~':
                                        header[2]=book_name
                                    else:
                                        header[2]+='&'+book_name
                                file2=open('members/members'+new_condition+'_info.csv','a',newline="")
                                w=csv.writer(file2)
                                w.writerow([header[0],header[1],header[2]])
                                file2.close()
                            except:
                                check_members=True
                        ########################
                        file=open('books/books'+condition+'_info.csv','r')
                        file2=open('books/books'+new_condition+'_info.csv','x')
                        file2.close()
                        file=open('books/books'+condition+'_info.csv','r')
                        data=csv.reader(file)
                        var_check_books=False
                        while var_check_books==False:
                            try:
                                header=next(data)
                                if header[0]==book_name:
                                    header[2]=int(header[2])-1
                                if header[2]!=0:
                                    file2=open('books/books'+new_condition+'_info.csv','a',newline="")
                                    w=csv.writer(file2)
                                    w.writerow([header[0],header[1],header[2]])
                                    file2.close()
                            except:
                                var_check_books=True
                        file=open('times.csv','w',newline="")
                        w=csv.writer(file)
                        w.writerows([['numbers','times'],[times,'times']])
                        file.close()
                        run4=False
                except:
                    print("we don't have this book!")
            #############################################################################
            if answer3=='return_book':
                book_return=input('book_return: ')
                answer4=input('Can i append it in library?')
                if answer4=='yes':
                    file=open('times.csv','r')
                    data=csv.reader(file)
                    header=next(data)
                    header=next(data)
                    times=int(header[0])+1
                    new_condition=str(times)
                    file=open('members/members'+condition+'_info.csv','r')
                    data=csv.reader(file)
                    file2=open('members/members'+new_condition+'_info.csv','x')
                    file2.close()
                    check_members=False
                    while check_members==False:
                        try:
                            header=next(data)
                            if header[0]==username:
                                List=header[2].split('&')
                                x=len(List)
                                header[2]=''
                                for i in range(x):
                                    if List[i]!=book_return:
                                        header[2]+=List[i]+'&'
                            file2=open('members/members'+new_condition+'_info.csv','a',newline="")
                            w=csv.writer(file2)
                            if header[2]!='':
                                w.writerow([header[0],header[1],header[2]])
                            elif header[2]=='&':
                                header[2]='~~~~'
                                w.writerow([header[0],header[1],header[2]])
                            else:
                                header[2]='~~~~'
                                w.writerow([header[0],header[1],header[2]])
                            file2.close()
                        except:
                            check_members=True
                    ########################
                    file=open('books/books'+condition+'_info.csv','r')
                    file2=open('books/books'+new_condition+'_info.csv','x')
                    file2.close()
                    file=open('books/books'+condition+'_info.csv','r')
                    data=csv.reader(file)
                    find_book=False
                    var_check_books=False
                    while var_check_books==False:
                        try:
                            header=next(data)
                            if header[0]==book_return:
                                header[2]=int(header[2])+1
                                find_book=True
                            file2=open('books/books'+new_condition+'_info.csv','a',newline="")
                            w=csv.writer(file2)
                            w.writerow([header[0],header[1],header[2]])
                            file2.close()
                        except:
                            var_check_books=True
                    file=open('times.csv','w',newline="")
                    w=csv.writer(file)
                    w.writerows([['numbers','times'],[times,'times']])
                    file.close()
                    if find_book==False:
                        author=input('i should apend it in library!Ebter its author: ')
                        file2=open('books/books'+new_condition+'_info.csv','a',newline="")
                        w=csv.writer(file2)
                        w.writerow([book_return,author,'1'])
                        file2.close()
                    run4=False
            if answer3=='exit':
                run4=False
        return new_condition
##################################################
while True:
    answer=input('Are you registerid?')
    if answer=='yes':
        Touple=check.check_member()
        username=Touple[0]
        password=Touple[1]
        find=Touple[2]
        if find==True:
            try:
                condition=run()
            except:
                pass
    if answer=='no':
        username=register()
        try:
            condition=run()
        except:
            pass