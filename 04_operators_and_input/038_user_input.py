# Lesson 038 - User Input
# Video: https://www.youtube.com/watch?v=2EY1CCnByK4

# ----------------
# -- User Input --
# ----------------

fName = input("What Is Your First Name ?")
mName = input("What Is Your Middle Name ?")
lName = input("What Is Your last Name ?")

# الجماليات والتنسيق 
fName = fName.strip().capitalize()
mName = mName.strip().capitalize()[0] # -> لو بدي أجيب أول حرف فقط من إسم الأب
lName = lName.strip().capitalize()
# strip -> عشان أحذف المسافات الي قبل وبعد الإدخال الى ما إلها أي لازمة
# capitalize -> بتكبر أول حرف من النص فقط، وبتصغر باقي الحروف

print(f"Hello {fName} {mName:.1s} {lName} Happy To See You") # -> طريقة ثانية لو بدي أجيب أول حرف فقط من إسم الأب 

