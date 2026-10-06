# Lesson 121 - Databases - SQLite Training On Everything
# Video: https://www.youtube.com/watch?v=4dhxFHgsLyY

# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------

import sqlite3

def get_all_data():

    db = None # قيمة ابتدائية، حتى لا يظهر خطأ في finally لو فشل الاتصال

    try:

        # connect To Database
        db = sqlite3.connect(r"database/app.db")

        # print Success Message
        print("Connected To Database Successfully")

        # Setting Up The Cursor
        cr = db.cursor()

        # Fetch Data From Database
        cr.execute("select * from users")

        # Assign Data To Variable
        results = cr.fetchall()

        # print Number Of Rows
        print(f"Database Has {len(results)} Rows.")

        # Printing Message
        print("\nShowing Data:\n")

        # Loop On Results
        for row in results:
            print(f"UserId => {row[0]},", end=" ")
            print(f"UserName => {row[1]}")

    except sqlite3.Error as er:

        print(f"Error Reading Data {er}")

    finally:

        if (db):

            # Close Database Connection
            db.close()
            print("\nConnection To Database Is Closed.")

get_all_data()

# Output:

# Connected To Database Successfully
# Database Has 3 Rows.

# Showing Data:

# UserId => 101, UserName => Mohammed
# UserId => 102, UserName => Osama
# UserId => 103, UserName => Ahmed

# Connection To Database Is Closed.
