# Lesson 078 - Modules Part 3 - Install External Packages
# Video: https://www.youtube.com/watch?v=aA96q7oBdVk

# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------

# [1] Module vs Package => File و Module البكج تتكون من
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------

# أمر التثبيت من الطرفية
# pip install termcolor pyfiglet

import termcolor
import pyfiglet

# print(dir(pyfiglet)) بعطيني جميع المديول او الأوامر الي جوا البكج هاد

print(pyfiglet.figlet_format("AlBasha")) # بطبع بتنسيق معين
#     _    _ ____            _
#    / \  | | __ )  __ _ ___| |__   __ _
#   / _ \ | |  _ \ / _` / __| '_ \ / _` |
#  / ___ \| | |_) | (_| \__ \ | | | (_| |
# /_/   \_\_|____/ \__,_|___/_| |_|\__,_|

print(termcolor.colored(pyfiglet.figlet_format("AlBasha"),"red")) # بطبع التنسيق باللون الأحمر بغير اللون يعني
#     _    _ ____            _
#    / \  | | __ )  __ _ ___| |__   __ _
#   / _ \ | |  _ \ / _` / __| '_ \ / _` |
#  / ___ \| | |_) | (_| \__ \ | | | (_| |
# /_/   \_\_|____/ \__,_|___/_| |_|\__,_|
