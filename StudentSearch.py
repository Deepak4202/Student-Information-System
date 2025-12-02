import mysql.connector

def searchrecord():
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
                print("\tSEARCH STUDENT RECORD")
                print("*" * 50)

                sid = int(input("Enter Student ID to Search: "))

                # Search Query
                cur.execute("SELECT * FROM students WHERE sid = %s", (sid,))
                record = cur.fetchone()

                if record:
                    print("*" * 50)
                    print("✅ Record Found")
                    print("*" * 50)
                    print("Student ID   :", record[0])
                    print("Student Name :", record[1])
                    print("Marks        :", record[2])
                    print("Phone Number :", record[3])
                else:
                    print("❌ Student not found.")

                ch = input("Search another record? YES/NO: ").upper()
                if ch not in ("YES", "Y"):
                    print("Thank you for using.")
                    break

            except ValueError:
                print("❌ Please enter numbers only for Student ID.")

            except mysql.connector.DatabaseError as e:
                print("❌ Database Error:", e)

    finally:
        if 'con' in locals() and con.is_connected():
            con.close()
            print("✅ MySQL connection closed")



