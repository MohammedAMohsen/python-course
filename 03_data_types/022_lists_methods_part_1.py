# Lesson 022 - Lists Methods Part One
# Video: https://www.youtube.com/watch?v=b5cFjJ278Vk

# -------------------
# -- Lists Methods --
# -------------------

# append() -> للإضافة داخل القائمة

myFriends = ["Mohammed","Noor","Ahmed"]
myOldFriends = ["Osama", "Ali", "Samah"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(12.43)
myFriends.append(True)

print(myFriends) # ['Mohammed', 'Noor', 'Ahmed', 'Alaa', 100, 12.43, True]

myFriends.append(myOldFriends) # -> هيضيف القائمة كعنصر داخل القائمة الرئيسية 

print(myFriends)       # ['Mohammed', 'Noor', 'Ahmed', 'Alaa', 100, 12.43, True, ['Osama', 'Ali', 'Samah']]
print(myFriends[2])    # Ahmed
print(myFriends[7])    # ['Osama', 'Ali', 'Samah']
print(myFriends[7][1]) # Ali -> القائمة الي داخل القائمة


# extend() -> بضيف القائمة الجديدة على القائمة القديمة كعناصر , يعني بوسع القائمة

a = [1, 2, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a) # [1, 2, 4, 'A', 'B', 'C', 'One', 'Two']


# remove() -> بتحذف عنصر معين

x = [1, 2, 3, 4, "Mohammed", True, "One"]

x.remove("Mohammed")

print(x) # [1, 2, 3, 4, True, 'One']


# sort() -> برتب العناصر

y = [1, 2, 100, 120, -10, 17, 29]
yy = ["R", "Z", "A"]
yyy = [1, 2, 100, 120, -10, 17,"Mohammed", 29] 

y.sort() # -> sort(reverse=False) القيمة الإفتارضية
print(y)  # [-10, 1, 2, 17, 29, 100, 120]

y.sort(reverse=True)
print(y) # [120, 100, 29, 17, 2, 1, -10]

yy.sort()
print(yy) # ['A', 'R', 'Z']

# print(yyy.sort()) Error -> لأن الترتيب فقط بكون للأعداد أو للأحرف على حدى ,يعني كل إشي لحال ,ما بزبط أخلط بين الأعداد والأحرف


# reverse() -> بيعكس القائمة

z = [10, 1, 9, 80, 100, "Mohammed", 100] 

z.reverse()

print(z) # [100, 'Mohammed', 100, 80, 9, 1, 10]
