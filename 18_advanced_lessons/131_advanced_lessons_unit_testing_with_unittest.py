# Lesson 131 - Advanced Lessons - Unit Testing With Unittest
# Video: https://www.youtube.com/watch?v=7qDuqwRYEhI

# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner
# - The Module That Run The Unit Testing (unittest, pytest)
# ---------------------------------------------------------
# Test Case
# - Smallest Unit Of Testing
# - It Use Asserts Methods To Check For Actions And Responses
# Test Suite
# - Collection Of Multiple Tests Or Test Cases
# Test Report
# - A Full Report Contains The Failure Or Succeed
# -------------------------------------------------------
# unittest
# - Add Tests Into Classes As Methods
# - Use a Series of Special Assertion Methods
# https://docs.python.org/3/library/unittest.html
# -----------------------------------------------
# ملاحظة: هذا الملف فيه عدة سيناريوهات متتالية، وبعضها يعطي خطأ بشكل مقصود
# التشغيل يتوقف عند أول خطأ، فلتجربة السيناريو التالي ضع علامة # أمام الذي قبله
# وانتبه: الأمر unittest.main() ينهي البرنامج بعد الاختبار، فلا ينفذ ما بعده
# -----------------------------------------------


assert 2 * 10 == 20, "Should Be 20" # -> هتلاحظ انو البرنامج ما اعطاني اي خطاء وكمل طبيعي

assert 2 * 10 == 19, "Should Be 20" # لاحظ اعطاني خطاء وكتبلي رسالة انو الناتج لازم يكون 20 وقف البرنامج

# Output

#     assert 2 * 10 == 19, "Should Be 20"
#            ^^^^^^^^^^^^
# AssertionError: Should Be 20


def test_case_one():

    assert 5 * 10 == 50, "Should Be 50"

def test_case_two():

    assert 5 * 50 == 240, "Should Be 250"

if __name__ == "__main__": # فقط اذا انتا بتشغل البرنامج بنفس الملف الى انتا فيه

    test_case_one()
    test_case_two()

    print("All Tests Passed")


# Output:

# اول اختبار عدى بدون مشاكل
# وقف البرنامج وما كمل AssertionError: Should Be 250 <- Error الثانية عملت عندي functionال

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def test_case_one():

    assert 5 * 10 == 50, "Should Be 50"

def test_case_two():

    assert 5 * 50 == 250, "Should Be 250"

if __name__ == "__main__":

    test_case_one()
    test_case_two()
    print("All Tests Passed :)")

# Output:
# All Tests Passed :)

# في الحالة السابقة ما كان اي خطأ وكمل البرنامج طبيعي

# -----------------------------------------------------------------
# فقط كنت بحاول اعمل اختبار بنفسي Module Test الى الأن لم استعمل اي
# --------------------------------

import unittest

class MyTestCase(unittest.TestCase):

    def test_one(self):
        
        self.assertTrue(100 > 88, "Should Be True")

    def test_two(self):

        self.assertEqual(40 + 60, 100, "Should Be 100")
        

if __name__ == "__main__":

    unittest.main()

# Output: -> True والنتيجة للاختبار كان True كان بستنا مني حالة assertTrue <= unittestما في اي مشاكل / ال
#         -> كان صحيح وما في مشاكل assertEqual والختبار الثاني 

# ..
# -------------------------------------------
# Ran 2 tests in 0.000s
# OK

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# ----------------------------------
# functionفي حال وجود خطأ في احدى ال
# ----------------------------------

class MyTestCase(unittest.TestCase):

    def test_one(self):
        
        self.assertTrue(100 > 90, "Should Be True")

    def test_two(self):

        self.assertEqual(40 + 60, 110, "Should Be 100")


if __name__ == "__main__":

    unittest.main()

# Output: # -> وأعطاني التقرير FAILED الإختبار الاول كان صحيح وعدى, اما الثاني كان في خطأ وعملي  

# .F
# ======================================================================
# FAIL: test_two (__main__.MyTestCase.test_two)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/user/python-course/18_advanced_lessons/131_advanced_lessons_unit_testing_with_unittest.py", line 125, in test_two
#     self.assertEqual(40 + 60, 110, "Should Be 100")
# AssertionError: 100 != 110 : Should Be 100

# ----------------------------------------------------------------------
# Ran 2 tests in 0.002s

# FAILED (failures=1)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class MyTestCase(unittest.TestCase):

    def test_one(self):
        
        self.assertTrue(100 > 90, "Should Be True")

    def test_two(self):

        self.assertEqual(40 + 60, 100, "Should Be 100")
    
    def test_three(self):

        self.assertGreater(100, 80, "Should Be True")


if __name__ == "__main__":

    unittest.main()


# Output:

# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK
