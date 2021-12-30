import os,sys
import pickle
import datetime

current_time = datetime.datetime.now()
print ("DATE AND TIME : ", end = "")
print (current_time)
print("                     WELCOME TO KCG COLLEGE OF TECHNOLOGY                                   ")
print("                     LIBRARY MANGEMENT SYSTEM                                 ")
print("                          ")

#Inserting data
def insertRecord():
    current_time = datetime.datetime.now()
    pid=int(input('Student ID :'))
    pname=(input('Enter Student Name :'))
    pdate=input("Student's date of birth(DD/MM/YYYY):")
    pbg=(input("Name of the book issued :"))
    bno=int(input("Book number :"))
    pbranch=input("Student' branch :")
    doi= current_time

    #Creating the dictionary
    rec={'Pid':pid,'Pname':pname,'Pdate':pdate,'Pbg':pbg,'Bn':bno,'Pbranch':pbranch,'Doi':doi}

    #Writing the Dictionary
    f=open('students.data','ab')
    pickle.dump(rec,f)
    f.close()

#Display all the record
def showRecord():
    f=open('students.data','rb')
    while True:
        try:
            rec=pickle.load(f)
            print('Student ID :',rec['Pid'])
            print('Student Name :',rec['Pname'])
            print("Student's date of birth :",rec['Pdate'])
            print("Name of the book issued :",rec['Pbg'])
            print('Book number :',rec['Bn'])
            print('Student branch :',rec['Pbranch'])
            print('Date and time of issue :',rec['Doi'])
            print("********************************************************************************************************************")
        except EOFError:
            break
    f.close()

#Check by Student infomation
def checkPatient(pid):
    f=open('students.data','rb')
    while True:
        try:
             rec = pickle.load(f)
             if rec['Pid'] == pid:
                print('Student ID :',rec['Pid'])
                print('Student Name :',rec['Pname'])
                print('Student date of birth :',rec['Pdate'])
                print('Name of the book issued :',rec['Pbg'])
                print('Book number :',rec['Bn'])
                print('Student branch :',rec['Pbranch'])
                print('Date and time of issue :',rec['Doi'])
        except EOFError:
            break
    f.close()
    
#Check by Student's name
def checkPat(pname):
    f=open('students.data','rb')
    while True:
        try:
            rec=pickle.load(f)
            if rec['Pname']==pname:
                print('Student ID:',rec['Pid'])
                print('Student Name:',rec['Pname'])
                print('Student date of birth :',rec['Pdate'])
                print('Name of the book issued :',rec['Pbg'])
                print('Book number :',rec['Bn'])
                print('Student branch:',rec['Pbranch'])
        except EOFError:
            break
    f.close()
                          

#Check by Student's date of birth
def checkPati(pdate):
    f=open('students.data','rb')
    while True:
        try:
            rec=pickle.load(f)
            if rec['Pdate']==pdate:
                print('Student ID :',rec['Pid'])
                print('Student Name:',rec['Pname'])
                print('Student date of birth :',rec['Pdate'])
                print('Name of the book issued :',rec['Pbg'])
                print('Book number :',rec['Bn'])
                print('Student branch:',rec['Pbranch'])
                print('Date and time of issue :',rec['Doi'])
        except EOFError:
            break
    f.close()
       
#Check by Student book issued
def checkpatien(pbname):
    f=open('students.data','rb')
    while True:
        try:
            rec=pickle.load(f)
            if rec['Pbg']==pbloodgroup:
                print('Student ID:',rec['Pid'])
                print('Student Name:',rec['Pname'])
                print('Student date of birth :',rec['Pdate'])
                print('Name of the book issued :',rec['Pbg'])
                print('Book number :',rec['Bn'])
                print('Student branch:',rec['Pbranch'])
                print('Date and time of issue :',rec['Doi'])
        except EOFError:
            break
    f.close()
    
#Check by Student's branch
def checkPatie(pbranch):
    f=open('students.data','rb')
    while True:
        try:
            rec=pickle.load(f)
            if rec['Pbranch']==pbranch:
                print('Student ID:',rec['Pid'])
                print('Student Name:',rec['Pname'])
                print('Student date of birth :',rec['Pdate'])
                print('Name of the book issued:',rec['Pbg'])
                print('Book number :',rec['Bn'])
                print('Student branch:',rec['Pbranch'])
                print('Date and time of issue :',rec['Doi'])
        except EOFError:
            break
    f.close()

def checkProduct(pid):
    f = open('students.data','rb')
    while True:
        try:
            rec = pickle.load(f)
            if rec['Pid'] == pid:
                return True
        except EOFError:
            break
    f.close()
    return False
       

#Deleting a record based on Student id
def delete(pid):
    f=open('students.data','rb')
    reclst=[]
    while True:
        try:
            rec=pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f=open('students.data',"wb")
    for x in reclst:
           if x['Pid']==pid:
               continue
           pickle.dump(x,f)
    f.close()


while True:
    print('Type 1 to insert Student information.')
    print("")
    print('Type 2 to display Student information.')
    print("")
    print('Type 3 to search by Student id.')
    print("")
    print('Type 4 to search by Student name.')
    print("")
    print('Type 5 to search by Student on date admission.')
    print("")
    print("Type 6 to search by Student book issued.")
    print("")
    print('type 7 to search by Student on Student based.')
    print("")
    print('Type 8 to delete a Student information.')
    print("")
    print('Type 9 to quit the program.')
    print("")
    choice=int(input('Enter your chioce:'))
    if choice == 1:
        insertRecord()
    if choice == 2:
        showRecord()
    if choice == 3:
        pid=int(input('Enter a Student ID to search:'))
        checkPatient(pid)
    if choice == 4:
        pname=input('Enter the Student name to search:')
        checkPat(pname)
    if choice == 5:
        pdate=input(" Student's date of birth(DD/MM/YYYY):")
        checkPati(pdate)
    if choice ==6:
        pbloodgroup=input(" Name of the book :")
        checkpatien(pbname)
    if choice == 7:
        pbranch=input('Student branch:')
        checkPatie(pbranch)
    if choice == 8:
       pid=int(input('Enter a Student ID:'))
       if checkProduct(pid)==True:
            delete(pid)
       else:
           print('Invalid Student ID:')
    if choice==9:
        print("                       HAVE A NICE DAY                       " )
        sys.exit(0)
    os.system('pause')
    os.system('cls')
