# Lesson 097 - Regular Expressions Part 3 Characters Classes Training's
# Video: https://www.youtube.com/watch?v=MnIPbqYoOaI

# -----------------------------------------------------------------------
# -- Regular Expressions => Characters Classes Training's --
# -----------------------------------------------------------------------
# [0-9]
# [^0-9]
# [A-Z]
# [^A-Z]
# [a-z]
# [^a-z]
# -------------

import re

Phone = """
001 5456-820
Hello Mohamed MohseN
123 123 1234
ABCD ABCDEF
$^%^&#@^*(%#
a m e
"""

my_search = re.findall("ame", Phone) 

print(my_search) # ['ame'] -> Moh['ame']d

my_search = re.findall("[ame]", Phone) # في اي مكان, مش شرط يكونو ورى بعض a - m - e اي احرف 

print(my_search) # ['e', 'a', 'm', 'e', 'e', 'a', 'm', 'e']

my_search = re.findall("[a-z]", Phone) # a الى z جميع الأحرف الصغيرة من 

print(my_search) # ['e', 'l', 'l', 'o', 'o', 'h', 'a', 'm', 'e', 'd', 'o', 'h', 's', 'e', 'a', 'm', 'e']

my_search = re.findall("[a-zA-Z0-9]", Phone) # والأرقام من 0 الى 9 Z الى A والكبيرة من a الى z جميع الأحرف الصغيرة من 

print(my_search) # ['0', '0', '1', '5', '4', '5', '6', '8', '2', '0', 'H', 'e',.....]

my_search = re.findall("[N]", Phone) # Nاعمل ماتش مع حرف ال

print(my_search) # ['N']

my_search = re.findall("[^N]", Phone) # Nاعمل ماتش مع اي شيء ما عدا حرف ال

print(my_search) # ['\n', '0', '0', '1', ' ', '5', '4', '5', '6', '-', '8', '2', '0',.....]

my_search = re.findall("[^A-Z]", Phone) # اعمل ماتش مع اي شيء ما عدا الأحرف الكبيرة

my_search = re.findall("[^A-Z0-9]", Phone) # اعمل ماتش مع اي شيء ما عدا الأحرف الكبيرة والأرقام

test_text = """
 AL 059 Hell0
AL 059 Hell0
"""

my_search = re.findall(r"\s[A-Z]{2}\s[0-9]{3}\s\w{,6}",test_text)

print(my_search) # [' AL 059 Hell0', '\nAL 059 Hell0']
