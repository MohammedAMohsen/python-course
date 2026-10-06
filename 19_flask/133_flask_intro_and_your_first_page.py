# Lesson 133 - Flask - Intro And Your First Page
# Video: https://www.youtube.com/watch?v=Ze_lPWFQmXI

# ----------------------------------------
# -- Flask => Intro and Your First Page --
# ----------------------------------------
# - Flask Is Micro Framework Built With Python
# --------------------------------------------
# - HTML
# - CSS
# - JavaScript
# --------------------------------------------

# pip install flask
from flask import Flask

skill_app = Flask(__name__)

@skill_app.route("/")
def homepage():

    return "Hello From Flask Framework"

@skill_app.route("/about")
def about():

    return "About Page From Flask Framework"

if __name__ == "__main__":

    # skill_app.run()

    # debug=True للتطوير فقط، ولا يستخدم أبدا في موقع منشور للناس
    skill_app.run(debug=True, port=9300) # الى هيعرض الصفحة Portواغير ال Debugممكن اشغل ال


# Run بعد ما اعمل
# http://127.0.0.1:9300/ <- هيعطيني رابط
# @skill_app.route("/") هاد الرابط هيعرض محتوى الصفحة الأولى 

# Hello From Flask Framework

# /about لو نفس الرابط كتبت 
# http://127.0.0.1:9300/about <- يعني الرابط هيكون هيك
# @skill_app.route("/about") حسب ما انا كاتب aboutهينقلني على صفحة ال

# About Page From Flask Framework

