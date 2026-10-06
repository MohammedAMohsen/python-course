# Lesson 125 - Databases - SQLite Create Skills App Part 3
# Video: https://www.youtube.com/watch?v=Bi5BMs9fc80

# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 3 --
# -----------------------------------------------------

# Import SQLite Module:
import sqlite3

try:

    # Create Database And Connect:
    db = sqlite3.connect(r"database/big_app.db")

    # print Success Message:
    print("Connected To Database Successfully")

    # Setting Up The Cursor:
    cr = db.cursor()

    # ملاحظة: وضع مدخلات المستخدم داخل نص الأمر بطريقة f-string غير آمن
    # الطريقة الآمنة باستخدام علامة ? موجودة في الدرس 127

    # Create The Tables and Fields:
    cr.execute("create table if not exists users (user_id integer, name text)")
    cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

    def commit_and_close():
        """Commit Changes And Close Connection To Database"""
        db.commit()
        db.close()
        print("Connection To Database Is Closed")

    # My User ID
    uid = 2

    # Define The Methods:

    def show_skills():

        cr.execute(f"select * from skills where user_id = '{uid}'")

        results = cr.fetchall()

        print(f"You Have {len(results)} Skills.")

        if len(results) > 0:

            print("Showing Skills With Progress:")

        for row in results:

            print(f"Skill => {row[0]},", end=" ")
            print(f"Progress => {row[1]}%")

        commit_and_close()

    def add_skill():
        
        sk = input("Write Skill Name: ").strip().capitalize()

        prog = input("Write Skill Progress: ").strip()

        cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', {prog}, {uid})")

        commit_and_close()

    def delete_skill():

        sk = input("Write Skill Name: ").strip().capitalize()

        cr.execute(f"delete from skills where name = '{sk}' and user_id = {uid}")
        # (and user_id = {uid}) user_idالخاصة بالمستخدم صاحب ال skillاحذف ال 
        # لكل المستخدمين skillلازم احدد اي مستخدم والا حذف جميع ال 

        commit_and_close()

    def update_skill():

        pass

        commit_and_close()
    
except sqlite3.Error as er:

    print(f"Error Reading Data {er}")

# Input Big Message:
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option: 
"""
# Input Option Choose:
user_input = input(input_message).strip().lower()

# Command List:
commands_list = ["s", "a", "d", "u", "q"]

# Check If Command Is Exists:
if user_input in commands_list:

    if user_input == "s":

        show_skills()

    elif user_input == "a":

        add_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        update_skill()
    
    else:

        print("App Is Closed.")
        commit_and_close()
else:

    print(f"Sorry This Command \"{user_input}\" Is Not Found :(")
