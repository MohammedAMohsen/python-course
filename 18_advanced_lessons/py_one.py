# File One -> ملف مساعد للدرس 128، شغله مباشرة ثم شغل الملف py_two.py وقارن الناتج

print("Print From File One")

def hello():

    print("Print Function From File One")

if True:

    print("True")


if __name__ == "__main__": # معناته اذا انتا بتشغل الملف وأنتا داخل الملف نفسو اطبع

    print("File One Is Running Directly (File One)")

    # من هذا الملف Import اي اشي بعرفو هان او بأنشأو او بقوم بكتابته لا يظهر في أي ملف قمت فيه بعمل 
    # وعند التشغيل لا يظهر اي شيء قمت بتعريفة هنا
    # الي انا فيها حاليا ifهنا وقمت بستدعائها في نفس الملف خارج ال function على سبيل المثال لو عرفت 
    # وشغلت البرنامج هيستدعي الفنقشن الي عرفتها وهيشتغل طبيعي لاني أنا بشغل الملف تبعي وانا بنفس الملف
    # هتلاحظ وجود خطاء في النتائج Import لكن لو شغلت الملف تاعي من ملف ثاني بعد ما اعمل
    # داخل شرط ان اني بالملف functionوالسبب اني عرفت ال
    # بالإسم هاذ function تعتي عبر تشغيل البرنامج من ملف ثاني فحكالي لا يوجد functionلكن انا استعديت ال
    # functionلأنها معرفة داخل الملف الأساسي فقط على انها خاصة بالملف الأساسي, اي أن الملف الأساسي هو الذي يستطيع رؤية ال

    def say():

        print("SAY HALLO :)")

else: # أما اذا بتشغل هذا الملف من ملف ثاني اطبع التالي

    print("You Are NOT Running File One Directly (file Two)")


say()

# Output:

# Print From File One
# True
# File One Is Running Directly (File One)
# SAY HALLO :)
