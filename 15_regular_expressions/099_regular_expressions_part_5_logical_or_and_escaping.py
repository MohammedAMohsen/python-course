# Lesson 099 - Regular Expressions Part 5 Logical Or & Escaping
# Video: https://www.youtube.com/watch?v=CD8HsbCG-T8

# ----------------------------------------------------
# -- Regular Expressions => Logical Or And Escaping --
# ----------------------------------------------------
# |	  Or
# \	  Escape Special Characters
# ()  Separate Groups
# -----------------------------

# (\d-|\d\)|\d>) (\w+)
# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))
# ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$
# -----------------------------

# أمثلة للتجربة على الأنماط السابقة

import re

# النمط الأول: رقم بعده واحد من ثلاث علامات، ثم مسافة ثم كلمة
# العلامة \) تعني القوس نفسه، لأن القوس بدون الشرطة له معنى خاص

names = ["1- Mohammed", "2) Ahmed", "3> Sayed", "4# Ali"]

for name in names:
    print(re.search(r"(\d-|\d\)|\d>) (\w+)", name))

# <re.Match object; span=(0, 11), match='1- Mohammed'>
# <re.Match object; span=(0, 8), match='2) Ahmed'>
# <re.Match object; span=(0, 8), match='3> Sayed'>
# None -> العلامة # ليست من الخيارات

# النمط الثالث: رابط موقع

urls = ["https://www.elzero.org", "http://google.com", "https://site.xyz"]

for url in urls:
    result = re.search(r"^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$", url)
    print(result.groups() if result else None)

# ('https://', 'www.', 'elzero', 'org')
# ('http://', None, 'google', 'com') -> None لأن الجزء www غير موجود، والعلامة ? جعلته اختياريا
# None -> الامتداد xyz ليس من الخيارات
