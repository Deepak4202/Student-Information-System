import mysql.connector

def deleterecord():
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
                print("\tDELETE STUDENT RECORD")
                print("*" * 50)

                sid = int(input("Enter Student ID to delete: "))

                # Check if record exists
                cur.execute("SELECT * FROM students WHERE sid = %s", (sid,))
                record = cur.fetchone()

                if record is None:
                    print("❌ Student ID not found.")
                    continue

                print("Record found:")
                print("ID    :", record[0])
                print("Name  :", record[1])
                print("Marks :", record[2])
                print("Phone :", record[3])

                confirm = input("Are you sure you want to DELETE this record? (YES/NO): ").upper()

                if confirm == "YES":
                    cur.execute("DELETE FROM students WHERE sid = %s", (sid,))
                    con.commit()
                    print(" Record Deleted Successfully.")
                else:
                    print("Delete cancelled.")

                ch = input("Delete another record? YES/NO: ").upper()
                if ch not in ("YES", "Y"):
                    print("Thank you for using.")
                    break

            except KeyboardInterrupt as e:
                print(e)
                exit()
            except ValueError:
                print(" Invalid ID. Enter numeric value only.")

            except mysql.connector.DatabaseError as e:
                print(" Database Error:", e)

    finally:
        if 'con' in locals() and con.is_connected():
            con.close()
            print("✅ MySQL connection closed")



