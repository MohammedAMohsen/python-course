# Lesson 135 - Flask - Create And Extends HTML Templates
# Video: https://www.youtube.com/watch?v=LeQaQde-RZc

# ----------------------------------------------
# -- Flask => Create & Extends Html Templates --
# ----------------------------------------------

from flask import Flask, render_template

skill_app = Flask(__name__)

@skill_app.route("/")
def homepage():

    return render_template("homepage2.html", title ="Homepage")


@skill_app.route("/about")
def about():

    return render_template("about2.html", title ="Aboutpage")

if __name__ == "__main__":

    skill_app.run(debug=True, port=4300)



# ملاحظة: الملف base.html الموجود في مجلد templates هو النسخة النهائية بعد الدروس التالية
# لذلك العنوان فيه اسمه title بدلا من pagetitle، والنسخة الأولى منه مكتوبة هنا للشرح

# -------------------------------------
# :الأساسي htmlملف ال
# -------------------------------------

# <!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="UTF-8" />
#         <title>{{ pagetitle }}</title>
#         <link rel="stylesheet" href="css/main.css" />
#         <link rel="stylesheet" href="css/master.css" />
#   </head>
#   <body>
#         {% block body %}
#         {% endblock %}
#   </body>
# </html>

# -------------------------------------
# Homepage.html الملفات الي هتاخذ منو 
# -------------------------------------

# {% extends 'base.html' %}
# {% block body %}
#   Hello From Homepage Html File
# {% endblock %}

# -------------------------------------
# about.html الملفات الي هتاخذ منو 
# -------------------------------------

# {% extends 'base.html' %}
# {% block body %}
#   Hello From About Html File
# {% endblock %}
