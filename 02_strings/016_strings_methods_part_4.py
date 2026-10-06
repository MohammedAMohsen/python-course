# Lesson 016 - Strings Methods Part Four
# Video: https://www.youtube.com/watch?v=jbV9d9H-udY

# ---------------------
# -- Strings Methods --
# -- replace, join ----
# ---------------------

# replace(Old Value, New Value, Count) -> بعمل تغيير للقيمة القديمة بالقيمة الجديدة مع عدد التغييرات اذا بدك

a = "Hello One Two Three One One"
print(a.replace("One", "1"))    # => Hello 1 Two Three 1 1
print(a.replace("One", "1", 1)) # => Hello 1 Two Three One One
print(a.replace("One", "1", 2)) # => Hello 1 Two Three 1 One

# join(Iterable) -> حسب الرابط سواء كان مسافة أو شرطة أو رمز Stringمع بعض وبرجعهم ك listبربط عناصر ال

myList = ["ALBasha", "Mohamed", "Mohsen"]
print("-".join(myList)) # => ALBasha-Mohamed-Mohsen
print(" ".join(myList)) # => ALBasha Mohamed Mohsen
print(", ".join(myList))# => ALBasha, Mohamed, Mohsen
print(type(", ".join(myList))) # => <class 'str'> String تأكيد أنو المخرج عبارة عن
