# Lesson 140 - Flask - Adding The JS Files
# Video: https://www.youtube.com/watch?v=KdctidbJBtQ

# ----------------------------------
# -- Flask => Adding The JS Files --
# ----------------------------------

from flask import Flask, render_template

skill_app = Flask(__name__)

my_skills = [("Css",80), ("Html", 68), ("Go", 45), ("Js", 90)]

@skill_app.route("/")
def homepage():

    return render_template("homepage2.html", title="Homepage", custom_css="home")

@skill_app.route("/add")
def add():

    return render_template("add.html",title="Add Skill",custom_css="add")

@skill_app.route("/about")
def about():

    return render_template("about2.html", title="Aboutpage")

@skill_app.route("/skills")
def skills():

    return render_template("skills.html",
                            title="Skills",
                            custom_css="skills",
                            page_head="My Skills",
                            description="This is My Skills Page",
                            skills=my_skills)

if __name__ == "__main__":

    skill_app.run(debug=True, port=9100)
