# Lesson 076 - Modules Part 1 - Intro And Built In Modules
# Video: https://www.youtube.com/watch?v=z7g9gCYYLiU

# --------------------------------------------------
# -- Modules => Built In Modules -------------------
# --------------------------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module

import random

# ملاحظة: الأرقام في هذا الدرس عشوائية، فالناتج عندك سيختلف في كل تشغيل

print(f"Print Random Float Number {random.random():.4f}") # Print Random Float Number 0.3587

# ---------------------------------------------------

# Show All Functions Inside Module(random)

print(dir(random)) # الي داخل مديول الراندوم functionهيطبع كل الأوامر وال

# ---------------------------------------------------

print(f"Print Random Integer {random.randint(100, 200)}") # Print Random Integer 192

# Import One Or Two Functions From Module

from random import randint # هيك انا بستدعي امر واحد فقط من داخل مديول الراندوم

print(f"Print Random Integer {randint(100, 200)}") # Print Random Integer 154

# ...................

from random import randint, random # هيك انا بستدعي امرين اثنين من داخل مديول الراندوم

print(f"Print Random Integer {randint(100, 200)}") # Print Random Integer 126
print(f"Print Random Float Number {random():.4f}") # Print Random Float Number 0.3703

# ...................

from random import *   # هيك انا بستدعي جميع اوامر الراندوم من داخل مديول الراندوم
