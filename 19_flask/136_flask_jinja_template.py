# Lesson 136 - Flask - Jinja Template
# Video: https://www.youtube.com/watch?v=VdANhdo9pTo

# ------------------------------------
# -- Flask => Jinja Template Engine --
# ------------------------------------

from flask import Flask, render_template

skill_app = Flask(__name__)

@skill_app.route("/")
def homepage():

    return render_template("homepage2.html", title="Homepage", test="Hello A")


@skill_app.route("/about")
def about():

    return render_template("about2.html", title="Aboutpage", test="Hello B")

if __name__ == "__main__":

    skill_app.run(debug=True, port=4300)


# Cssشرحنا طريقة استدعاء ملفات ال

# <head>
# <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}" />
# </head>

# static داخل مجلد اسمو Cssوضروري يكون ملف ال
# معرف انو يدور على الملف داخل هذا المجلد طالما انا لم اغير التعريف بنفسي flaskلأنو ال
# Templateلازم تكون في مجلد ال htmlنفس قصة ملفات ال
