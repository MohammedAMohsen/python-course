# Lesson 137 - Flask - Advanced Css Task Using Jinja
# Video: https://www.youtube.com/watch?v=CP8gG1gDbAw

# --------------------------------------------
# -- Flask => Advanced Css Task Using Jinja --
# --------------------------------------------

from flask import Flask, render_template

skill_app = Flask(__name__)

@skill_app.route("/")
def homepage():

    return render_template("homepage2.html", title="Homepage", custom_css="home")

@skill_app.route("/add")
def add():

    return render_template("add.html", title="Add Skill", custom_css="add")

@skill_app.route("/about")
def about():

    return render_template("about2.html", title="Aboutpage")


if __name__ == "__main__":

    skill_app.run(debug=True, port=9000)
