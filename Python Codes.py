import mysql.connector
from tabulate import tabulate

# code for viewing student details
def viewStudentDetails():

    # Opens database connection with a dictionery            
    conDict = {'host':'localhost',
               'database':'db_student_attendance',
               'user':'root',
               'password':''}
     
    db = mysql.connector.connect(**conDict)

    # Prepare a cursor object using cursor() method
    cursor = db.cursor()
        
    cursor.execute("SELECT * FROM student_info")

    data = cursor.fetchall()
    print(tabulate(data, headers=[
      "\nStudent No", "\nFirst Name", "\nLast Name" ]))

    db.close()

# code to add the attendance to the available students in the first table
def addAttendance():
  
    try:
        # Opens database connection with a dictionery
        conDict = {'host':'localhost',
                   'database':'db_student_attendance',
                   'user':'root',
                   'password':''}

        db = mysql.connector.connect(**conDict)

        # Prepare a cursor object using cursor() method
        cursor = db.cursor()

        mySQLText = "SELECT studentNo,fName FROM student_info"

        cursor.execute(mySQLText)

        data = cursor.fetchall()

        while True:
            
            print("Attendance Of ",cursor.rowcount," Students Needed To Be Added. yes/no?: ", end=' ')
        
            goNext = input()
            print()
            
            viewStudentDetails()
            print()
            
            if (goNext == "yes"):
                
                date = input("Please Enter The Date For The Attendance: ")
                print("\nStudent Attendance(Absent or Present)")
                
                i = 0
                
                while i < cursor.rowcount:
                    print(data[i][1], end=" ")
                    atd = input()
                    
                    cursor1 = db.cursor()
                    
                    mySQLText1 = "INSERT INTO keeping_track (studentNo,date,attendance) VALUES (%s,%s,%s)"

                    cursor1.execute(mySQLText1, (data[i][0], date, atd))

                    db.commit()
                    i += 1
                    
                print("\nAttendance Added\n")
                main()
            
            elif goNext == 'no':
                main()

            else:
                print("\nEnter Either  'yes' or 'no' and try again!\n")
                addAttendance()
                
    except:
        print("ERROR\n")

    db.close()

def ask_again():
    askAgain = input("Do You Want to Add One Last Time(yes or no)? ")
    print()
    if askAgain == "yes":
        
        # Opens database connection with a dictionery
        conDict = {'host':'localhost',
                   'database':'db_student_attendance',
                   'user':'root',
                   'password':''}

        db = mysql.connector.connect(**conDict)

        # Prepare a cursor object using cursor() method
        cursor = db.cursor()


        ustudentNo = int(input("Type Student Number : "))
        while(ustudentNo<0):
            print("The Student Number cannot be Negative. Please Try Again!")
            studentNo = int(input("Type student Number : "))
        

        ufName = input("Type First Name : ")
        while (len(ufName)>18):
            print("Too Many Characters, Maximum 18 Characters! Try Again.")
            ufName = input("Type First Name : ")
                    

        ulName = input("Type Last Name : ")
        while (len(ulName)>18):
            print("Too Many Characters, Maximum 18 Characters! Try Again.")
            ulName = input("Type Last Name : ")


        mySQLText = "INSERT INTO student_info (studentNo, fName, lName) VALUES (%s,%s,%s)"
        myValues = (ustudentNo, ufName, ulName)
        cursor.execute(mySQLText, myValues)

        db.commit()
        print(cursor.rowcount, "Record Added\n")
        db.close()
        main()

    elif askAgain == "no":
        print()
        main()
                                    
    else:
        print("Enter Either 'yes' or 'no'!")
        ask_again()


# code to view necesaary details                     
def view():

    # menu for option 4    
    print(" 1. View all Student Details\n"
          " 2. View all Attendance Details\n"
          " 3. View only Attendance of a Selected Student\n"
          " 4. Return to the Main Menu\n")

    choiceNo3 = int(input("Enter the Preferred Option(1, 2, 3 or 4) : "))
        
    if (choiceNo3 == 1):

        viewStudentDetails()
        print()
        view()

    elif (choiceNo3 == 2):
        
        # Opens database connection with a dictionery    
        conDict = {'host':'localhost',
                   'database':'db_student_attendance',
                   'user':'root',
                   'password':''}
     
        db = mysql.connector.connect(**conDict)

        # Prepare a cursor object using cursor() method
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM keeping_track")

        data = cursor.fetchall()
        print(tabulate(data, headers=[
          "\nStudent No", "\nDate", "\nAttendance" ]))

        print()        
        db.close()
        view()

    elif (choiceNo3 == 3):

        # Opens database connection with a dictionery               
        conDict = {'host':'localhost',
                   'database':'db_student_attendance',
                   'user':'root',
                   'password':''}
     
        db = mysql.connector.connect(**conDict)

        # Prepare a cursor object using cursor() method
        cursor = db.cursor()
        print()
        
        ustudentNo = input("Type the Students Number to get their Attendance : ")
        print()
        
        cursor.execute("SELECT * FROM keeping_track WHERE studentNo = " + ustudentNo)

        data = cursor.fetchall()
        print(tabulate(data, headers=[
          "\nStudent No", "\nDate", "\nAttendance" ]))

        print()        
        db.close()
        view()

    elif (choiceNo3 == 4):
        print()
        main()

    else:
        print("\nEnter Either 1, 2, 3, or 4! Try Again\n")
        view()

# code for updating, inserting and deleting student details
def sub():

    choiceNo2 = input("Which one?; Insert, Update or Delete Students? Else, Type 'Back' to go to the Main Menu: ")
    print()

    if (choiceNo2 == "Insert"):

        # Opens database connection with a dictionery
        conDict = {'host':'localhost',
                   'database':'db_student_attendance',
                   'user':'root',
                   'password':''}
            
        db = mysql.connector.connect(**conDict)

        # Prepare a cursor object ysing cursor() method
        cursor = db.cursor()

        ustudentNo = int(input("Type Student Number : "))
        while(ustudentNo<0):
            print("The Student Number Cannot Be Negative. Please Try Again!")
            ustudentNo = int(input("Type Student Number : "))

        ufName = input("Type First Name : ")
        while (len(ufName)>18):
            print("Too Many Characters, Maximum 18 Characters! Try Again.")
            ufName = input("Type First Name : ")
                
        ulName = input("Type Last Name : ")
        while (len(ulName)>18):
            print("Too Many Characters, Maximum 18 Characters! Try Again.")
            ulName = input("Type Last Name : ")

        mySQLText = "INSERT INTO student_info (studentNo, fName, lName) VALUES (%s, %s, %s)"
        myValues = (ustudentNo, ufName, ulName)
        cursor.execute(mySQLText, myValues)
        
        db.commit()
            
        print(cursor.rowcount, "Record Added\n")

        db.close()
        main()
              
    elif (choiceNo2 == "Update"):

        # Opens database connection with a dictionery
        conDict = {'host':'localhost',
                    'database':'db_student_attendance',
                    'user':'root',
                    'password':''}
     
        db = mysql.connector.connect(**conDict)

        # Prepare a cursor object ysing cursor() method
        cursor = db.cursor()

        ustudentNo = input("Type Student Number : ")

        ufName = input("Type First Name : ")
        while (len(ufName)>18):
            print("Too Many Characters, Maximum 18 Characters! Try Again.")
            ufName = input("Type First Name : ")
                
        ulName = input("Type last name : ")
        while (len(ulName)>18):
            print("Too Many Characters, Maximum 18 Characters! Try Again.")
            ulName = input("Type Last Name : ")
    
        updTxt = "UPDATE student_info SET fName = '" + ufName + "', lName = '" + ulName + "' WHERE studentNo = " + ustudentNo
        cursor.execute(updTxt)

        db.commit()
                
        print(cursor.rowcount, "Record Updated\n")

        db.close()
        main()

    elif (choiceNo2 == "Delete"):

        # Opens database connection with a dictionery        
        conDict = {'host':'localhost',
                    'database':'db_student_attendance',
                    'user':'root',
                    'password':''}

        db = mysql.connector.connect(**conDict)

        # Prepare a cursor object ysing cursor() method
        cursor = db.cursor()

        ustudentNo = input("Type a student number to delete : ")
                
        cursor.execute("DELETE FROM student_info WHERE studentNo = " + ustudentNo + "")

        db.commit()
                
        print(cursor.rowcount, "Record Deleted\n")

        db.close()
        main()

    elif (choiceNo2 == "Back"):
        main()

    else:
        print("Enter either 'Insert', 'Update', 'Delete' Or 'Back'\n")
        sub()

# code for inserting the student details
def newDetails():

    ttlStu = 0

    # Opens database connection with a dictionery
    conDict = {'host':'localhost',
                'database':'db_student_attendance',
                'user':'root',
                'password':''}

    while ttlStu<3:
            
        db = mysql.connector.connect(**conDict)

        # Prepare a cursor object using cursor() method
        cursor = db.cursor()
            
        ustudentNo = int(input("Type student number : "))
        while(ustudentNo<0):
            print("The Student Number Cannot Be Negative. Please Try Again!")
            ustudentNo = int(input("Type student number : "))
            
        ufName = str(input("Type first name : "))
        while (len(ufName)>18):
            print("Too Many Characters, Maximum 18 Characters! Try Again.")
            ufName = str(input("Type first name : "))        
                
        ulName = input("Type last name : ")
        while (len(ulName)>18):
            print("Too Many Characters, Maximum 18 Characters! Try Again.")
            ulName = input("Type last name : ")
                
    
        mySQLText = "INSERT INTO student_info (studentNo, fName, lName) VALUES (%s,%s,%s)"
        myValues = (ustudentNo, ufName, ulName)
        cursor.execute(mySQLText, myValues)

        db.commit()
        print(cursor.rowcount, "Record Added\n")
        db.close()
        ttlStu += 1

    addMore = input("Do You Want Enter More Student Details (yes or no)? ")
    print()
        
    if addMore == "yes":
            
        howMany = int(input("How Many More Student Details Do You Want To Add? 1 or 2?"))
        print()

        if howMany == 1:

            # Opens database connection with a dictionery
            conDict = {'host':'localhost',
                        'database':'db_student_attendance',
                        'user':'root',
                        'password':''}
            
            db = mysql.connector.connect(**conDict)

            # Prepare a cursor object using cursor() method
            cursor = db.cursor()

            ustudentNo = int(input("Type Student Number : "))
            while(ustudentNo<0):
                print("The Student Number Cannot Be Negative. Please Try Again!")
                ustudentNo = int(input("Type Student Number : "))

            ufName = input("Type First Name : ")
            while (len(ufName)>18):
                print("Too Many Characters, Maximum 18 Characters! Try Again.")
                ufName = input("Type First Name : ")
                
            ulName = input("Type Last Name : ")
            while (len(ulName)>18):
                print("Too Many Characters, Maximum 18 Characters! Try Again.")
                ulName = input("Type Last Name : ")
    
            mySQLText = "INSERT INTO student_info (studentNo, fName, lName) VALUES (%s,%s,%s)"
            myValues = (ustudentNo, ufName, ulName)
            cursor.execute(mySQLText, myValues)

            db.commit()
            print(cursor.rowcount, "Record Added\n")
            db.close()

            ask_again()
            print()
            main()
                
        elif (howMany == 2):

            while howMany > 0:

                # Opens database connection with a dictionery
                conDict = {'host':'localhost',
                            'database':'db_student_attendance',
                            'user':'root',
                            'password':''}

                db = mysql.connector.connect(**conDict)
                    
                # Prepare a cursor object using cursor() method
                cursor = db.cursor()
    
                ustudentNo = int(input("Type Student Number : "))
                while(ustudentNo<0):
                    print("The Student Number Cannot Be Negative. Please Try Again!")
                    ustudentNo = int(input("Type Student Number : "))

                ufName = input("Type First Name : ")
                while (len(ufName)>18):
                    print("Too Many Characters, Maximum 18 Characters! Try Again.")
                    ufName = input("Type First Name : ")
                
                ulName = input("Type Last Name : ")
                while (len(ulName)>18):
                    print("Too Many Characters, Maximum 18 Characters! Try Again.")
                    ulName = input("Type Last Name : ")
                        
                mySQLText = "INSERT INTO student_info (studentNo, fName, lName) VALUES (%s,%s,%s)"
                myValues = (ustudentNo, ufName, ulName)
                cursor.execute(mySQLText, myValues)

                db.commit()
                print(cursor.rowcount, "Record Added\n")
                db.close()

                howMany-=1
            main()
        else:
            print("You Can Not Enter Details Of More Than 5 Students In Total!")

    else:
        main()

# code for the main menu
def main():

    print("STUDENT ATTENDANCE\n")

    print("1. Key In New Details.")
    print("2. Entering The Attendance.")
    print("3. Insert, Update, Delete Students Details From The First Table.")
    print("4. View All Student Details, Attendance Details, And Only Attendance of a Selected Student.")
    print("5. Exit\n")


    choice = int(input("Enter Your Preferred Option : "))
    print()

    if (choice == 1):
        newDetails()

    elif (choice == 2):
        addAttendance()
        
    elif (choice == 3):
        sub()
                
    elif (choice == 4):
        view()

    elif (choice == 5):
        exit()

    else:
        print("Invalid Input! Please Enter Either 1, 2, 3, 4 or 5.\n")
        main()
        
main()
