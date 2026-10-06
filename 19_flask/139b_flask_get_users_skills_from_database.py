# Extra exercise for lesson 139 (my own practice, not a video lesson)
# Lesson 139 video: https://www.youtube.com/watch?v=mciHTWGhh4w

# ---------------------------------------
# -- Flask => Users Skills From Database --
# -----------------------------------------
# هذا التمرين يقرأ قاعدة البيانات database/big_app.db
# أنشئها وأضف لها مستخدمين ومهارات أولا عن طريق دروس تطبيق المهارات (123 - 126)

from flask import Flask, render_template
import sqlite3

skill_app = Flask(__name__)

db = sqlite3.connect("database/big_app.db")
cr = db.cursor()

cr.execute("SELECT * FROM users")
my_users = cr.fetchall()
data = []

for user in my_users:
    cr.execute(f"SELECT * FROM skills where user_id = {user[0]}")
    my_skills = cr.fetchall()
    list_skill = []

    for skill in my_skills:
        list_skill.append((skill[0], skill[1]))
    data.append({"id":user[0], "name":user[1], "skills":list_skill})

@skill_app.route("/")
def skills():

    return render_template("user_skills.html",
                            title="Skills",
                            custom_css="skills",
                            page_head="Users Skills",
                            description="This is Users Skills Page",
                            users_skills=data)

if __name__ == "__main__":

    skill_app.run(debug=True, port=9100)

# ---------------------------------------------------------------------
#      حل آخر بطريقة مختلفة لجلب البيانات بطريقة اكثر احترافية
# ---------------------------------------------------------------------
# ملاحظة: هذا الجزء يعمل فقط بعد إيقاف السيرفر لأنه بعد سطر التشغيل
# لتجربته في الصفحة، انقله فوق المسارات وأرسل final_data بدلا من data
# واستخدمنا اسما جديدا للقاموس users_dict حتى لا يغطي على المتغير data الذي تستخدمه الصفحة
# الحل الثاني أفضل لأنه يجلب كل شيء باستعلام واحد بدلا من استعلام لكل مستخدم

cr.execute("SELECT users.user_id, users.name, skills.name, skills.progress FROM users JOIN skills ON users.user_id = skills.user_id")
rows = cr.fetchall()
users_dict = {}

for row in rows:

    user_id = row[0]
    user_name = row[1]
    skill_name = row[2]
    progress = row[3]

    if user_id not in users_dict: # اذا المستخدم مش موجود ضيفو واذا موجود تجاهل, هيك بمنع التكرار

        users_dict[user_id] = {"name": user_name, "skills":[]} # هيك بضيف المستخدمين بدون تكرار, كل مستخدم اسمو وقائمة فارغة بالمهارات
    
    users_dict[user_id]["skills"].append((skill_name, progress)) # هيك بضيف المهارات كلها لكل مستخدم داخل القائمة الفارغة

final_data = list(users_dict.values()) # هيك بحول القاموس الى قائمة بدون المفتاح لانو ما بلزمني


# طباعة توضيحية لكل خطوة سابفا

# print(row)
# (1, 'Mohammed', 'Mysql', 92)
# (2, 'Maha', 'Php', 67)
# (1, 'Mohammed', 'Css', 70)
# (2, 'Maha', 'Java', 88)
# (1, 'Mohammed', 'Sqli', 34)
# (3, 'Alaa', 'Pascal', 78)
# (4, 'Jamel', 'Pascal', 81)

# print(users_dict)
# {
#  1: {'name': 'Mohammed', 'skills': [('Mysql', 92), ('Css', 70), ('Sqli', 34)]},
#  2: {'name': 'Maha', 'skills': [('Php', 67), ('Java', 88)]},
#  3: {'name': 'Alaa', 'skills': [('Pascal', 78)]},
#  4: {'name': 'Jamel', 'skills': [('Pascal', 81)]}
# }

# print(final_data)
# [
# {'name': 'Mohammed', 'skills': [('Mysql', 92), ('Css', 70), ('Sqli', 34)]},
# {'name': 'Maha', 'skills': [('Php', 67), ('Java', 88)]},
# {'name': 'Alaa', 'skills': [('Pascal', 78)]},
# {'name': 'Jamel', 'skills': [('Pascal', 81)]}
# ]
