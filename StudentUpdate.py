import mysql.connector

def updaterecord():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Enter your db password",
            database="college"
        )

        cur = con.cursor()

        while True:
            try:
                print("*" * 50)
                print("\tUPDATE STUDENT RECORD")
                print("*" * 50)

                sid = int(input("Enter Student ID to Update: "))

                cur.execute("SELECT * FROM students WHERE sid = %s", (sid,))
                record = cur.fetchone()

                if record is None:
                    print("Student ID not found.")
                    continue

                print("Current Details:")
                print("Name :", record[1])
                print("Marks:", record[2])
                print("Phone:", record[3])

                new_name = input("Enter New Name: ")
                if not new_name.isalpha():
                    raise ValueError("Name must contain only letters")

                new_marks = float(input("Enter New Marks: "))
                if new_marks < 0 or new_marks > 100:
                    raise ValueError("Marks must be between 0 and 100")

                new_phone = input("Enter New Phone Number: ")
                if not new_phone.isdigit() or len(new_phone) != 10:
                    raise ValueError("Phone number must be 10 digits")

                query = "UPDATE students SET sname=%s, marks=%s, phone=%s WHERE sid=%s"
                values = (new_name, new_marks, new_phone, sid)
                cur.execute(query, values)
                con.commit()

                print("✅ Record Updated Successfully.")

                ch = input("Update another record? YES/NO: ").upper()
                if ch not in ("YES", "Y"):
                    print("Thank you for using")
                    break

            except ValueError as e:
                print("Error:", e)

            except mysql.connector.DatabaseError as e:
                print("Database Error:", e)

    finally:
        if 'con' in locals() and con.is_connected():
            con.close()
            print("✅ MySQL connection closed")



