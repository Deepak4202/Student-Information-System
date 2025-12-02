import mysql.connector
def getallrecords():

    try:
        # Step-1 & Step-2: Connection
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Deepak21",
            database="college"
        )


        cur = con.cursor()
        sql_Query = "select * from students"

        cur.execute(sql_Query)
        records = cur.fetchall()
        print("*"*60)
        print("\t\tSID\t\t Sname\t\t Marks \t\t PhoneNumber")
        print("*"*60)
        for record in records:
            for val in record:
                print(f"\t\t{val}",end="")
            print()
        print("------------------------------------------------------------------")



    except mysql.connector.DatabaseError as e:
        print(e)

def getrecord():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Deepak21",
            database="college"
        )

        cur = con.cursor()
        sql_Query = "select * from students"
        cur.execute(sql_Query)

        while True:
            try:
                number = int(input("Enter number of records you want : "))

                if number <= 0:
                    raise ValueError("Dont Enter -ve Numbers")

                records = cur.fetchmany(number)

                # ✅ CLEAR remaining results
                cur.fetchall()

                if len(records) == 0:
                    print("No records present")
                    break

                print("*" * 60)
                print("\tSID\tSname\tMarks\tPhoneNumber")
                print("*" * 60)

                for record in records:
                    for val in record:
                        print(f"\t{val}", end="")
                    print()

                print("-" * 60)
                break

            except ValueError:
                print("Dont Enter String values")

    except mysql.connector.DatabaseError as e:
        print("Database Error:", e)

    finally:
        if 'con' in locals() and con.is_connected():
            con.close()
            print("✅ MySQL connection closed")

    print("*" * 50)
