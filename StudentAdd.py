import mysql.connector
def addstudentrecord():

    try:
        # Step-1 & Step-2: Connection
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Enter your db password",
            database="college"
        )

        cur = con.cursor()
        print("*" * 50)

        # Input Validation Loop
        while True:
            try:
                sid = int(input("Enter your Student id: "))
                sname = input("Enter Student name: ")

                if not sname.isalpha():
                    raise ValueError("Name should contain only letters.")

                smarks = float(input("Enter Student marks: "))
                if smarks < 0 or smarks > 100:
                    raise ValueError("Marks should be between 0 and 100.")

                sphoneNumber = input("Enter Student phone number: ")
                if not sphoneNumber.isdigit() or len(sphoneNumber) != 10:
                    raise ValueError("Phone number must be exactly 10 digits.")

                print(" Data accepted successfully!")
                break

            except ValueError as e:
                print(" Error:", e)
                print("Please enter valid details again.\n")

        # Insert Query (Safe)
        query = "INSERT INTO students (sid, sname, marks, phone) VALUES (%s, %s, %s, %s)"
        values = (sid, sname, smarks, sphoneNumber)

        cur.execute(query, values)
        con.commit()

        print("✅ Successfully inserted one record")

    except mysql.connector.Error as err:
        print(" MySQL Error:", err)

    finally:
        if 'con' in locals() and con.is_connected():
            con.close()
            print("✅ MySQL connection closed")
    print("*"*50)


