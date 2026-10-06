# Lesson 050 - Loop - While Training's Password Guess
# Video: https://www.youtube.com/watch?v=7NIcsmfHIrg

# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4
mainPassword = "Python@123"
inputPassword = input('Write Your Password: ')

while inputPassword != mainPassword:

    tries -= 1

    print(f"Wrong Password, {'Last' if tries == 0 else tries} Chance Left") # Last في آخر محاولة إطبع كلمة

    inputPassword = input('Write Your Password: ')

    if tries == 0:

        print("All Tries Is Finished")

        break
        
        print("Will Not Print :|")

else: # -> في حال كتب كلمة المرور صح بطبعلو الرسالة هادي , غير هيك لو إنتهت المحاولات بطلع برا اللوب وما بطبع إشي

    print("Correct Password")
