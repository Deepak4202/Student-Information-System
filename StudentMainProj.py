import sys

from StudentMenu import menu
from StudentAdd import addstudentrecord
from StudentViews import getallrecords, getrecord
from StudentDelete import deleterecord
from StudentUpdate import updaterecord
from StudentSearch import searchrecord

while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                addstudentrecord()
            case 2:
                getallrecords()
            case 3:
                getrecord()
            case 4:
                deleterecord()
            case 5:
                updaterecord()
            case 6:
                searchrecord()
            case 7:
                print("✅ Thanks for using Student Information System")
                sys.exit()
            case _:
                print(" Invalid choice! Try again.")

        cont = input("Do you want to continue? YES/NO: ").upper()
        if cont not in ("YES", "Y"):
            print("✅ Thanks for using Student Information System")
            break

    except ValueError:
        print(" Please enter numeric value only.")
