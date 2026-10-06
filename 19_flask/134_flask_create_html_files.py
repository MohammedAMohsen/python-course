# Lesson 134 - Flask - Create Html Files
# Video: https://www.youtube.com/watch?v=07qgoQngK2Q

# --------------------------------
# -- Flask => Create HTML Files --
# --------------------------------

from flask import Flask, render_template

skill_app = Flask(__name__)

@skill_app.route("/")
def homepage():

    # عشان يقدر يقراء منو templates يكون داخل مجلد اسم htmlلازم ملف ال

    return render_template("homepage1.html", pagetitle ="Homepage")

    # من هان htmlبقدر اتحكم في صفحة ال
    # pagetitle -> بقدر اتحكم فيه من داخل الكود عندي هان
    # (<title>{{ pagetitle }}</title>) في العنوان هان html في كود ال
    # pagetitle ="H" الي عرفناه هان في الكود pagetitle هنكتب ال
    # وهتلاحظ تغير عنوان الصفحة

@skill_app.route("/about")
def about():

    return render_template("about1.html", pagetitle ="Aboutpage")

if __name__ == "__main__":

    skill_app.run(debug=True, port=4300)


# <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>{{ pagetitle }}</title>
#     </head>
#     <body>
#         Hello From Home Page
#     </body>
# </html>

# <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>{{ pagetitle }}</title>
#     </head>
#     <body>
#         Hello From About Page
#     </body>
# </html>
