# Lesson 092 - Exceptions Handling Advanced Example
# Video: https://www.youtube.com/watch?v=RjkKwZ-p7YU

# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------

the_file = None
the_tries = 5

while the_tries > 0:

    try: # Try To Open The File

        print("Enter The File Name With Absolute Path To Open")

        print(f"You Have {the_tries} Tries Left")

        print("Example: files/text1.txt")
        
        file_name_and_path = input("File Name => : ").strip()

        the_file = open(file_name_and_path, "r")
        print("-"*60)
        print(f"\n{the_file.read()}\n")
        print("-"*60)

        # the_file.close()

        break

    except FileNotFoundError: # خطأ خاص بأن الملف غير موجود

        print("File Not Found Please Be Sure The Name Is Valid")

        the_tries -= 1

    except: # للأخطاء العامة except يستحسن اني اعمل 

        print("Error Happen")

    finally: # سواء ظهر خطأ ولا ماظهر خطأ أغلق الملف بشرط ان يكون مفتوح

        # بعمل شرط للإغلاق None وعشان ما يغلق الملف من البداية لان القيمة الإبتدائية للملف 

        if the_file is not None:

            the_file.close()

            print("File Closed.")

            # ؟؟ Try بس السؤال هل ممكن اضيف اغلاق الملف بعد الإنتهاء من قراءة الملف داخل ال
            # الجواب: نعم ممكن، لكن لو حدث خطأ قبل سطر الإغلاق فلن يصل إليه البرنامج ويبقى الملف مفتوحا
            # أما finally فتعمل دائما، لذلك الإغلاق فيها أضمن
            # والطريقة الأسهل هي with التي تغلق الملف تلقائيا (راجع الدرس 068)

else:

    print("All Tries Is Done")
