# Assignment 01

import unittest

class MyTest(unittest.TestCase):

    def test_one(self):
        self.assertIn(10, [2, 33, 64, 10, 5])

    def test_two(self):
        self.assertIsInstance(10, int)

    def test_three(self):
        self.assertTrue(100, True) # انتبه: القيمة الثانية هنا رسالة الخطأ، وليست القيمة المتوقعة

    def test_four(self):
        self.assertFalse([], False)

    def test_five(self):
        self.assertGreaterEqual(100, 90)
        self.assertGreaterEqual(100, 100)
        # self.assertGreaterEqual(100, 101) -> AssertionError: 100 not greater than or equal to 101

if __name__ == "__main__":

    unittest.main(exit=False) # exit=False حتى يكمل البرنامج بعد الاختبار وينفذ الواجب الثاني

# Output:

# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s

# OK

# _______________________________________________________________________________________________________
# Assignment 02 -> ال السيريل نمبر يكون عبارة عن أربع ارقام بعدهم – بعدهم أربع ارقام ثم – بعد ذلك ست ارقام

import string, random

def make_serial(count):

    all_chars = string.ascii_letters + string.digits
    myList = []

    while count > 0:
        myList.append(all_chars[random.randint(0,len(all_chars)-1)])
        count -= 1
    return "".join(myList)
    
print(make_serial(4), make_serial(4), make_serial(6), sep="-") # k6cb-AbJN-b3XP95

# ----------------------------
# حل آخر اكثر احترافية
# ----------------------------

def make_serial(count):

    all_chars = string.ascii_letters + string.digits
    return "".join(random.choice(all_chars) for _ in range(count))

def generate_serial():
    return f"{make_serial(4)}-{make_serial(4)}-{make_serial(6)}"

print(generate_serial()) # S86c-Qp6i-E4S9aa
