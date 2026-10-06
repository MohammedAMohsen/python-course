# Lesson 071 - Built In Functions Part 3
# Video: https://www.youtube.com/watch?v=XRw7mArOyok

# ------------------------
# -- Built In Functions --
# ------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------

# abs() القيمة المطلقة بين الصفر والقيمة الي هعطلو اياها ويكون الناتج بالموجب

print(abs(100)) # 100
print(abs(-100)) # 100
print(abs(10.19)) # 10.19
print(abs(-10.19)) # 10.19

# pow(base(اجباري), exp(اجباري), mod(إختياري)) => Power

print(pow(2, 5)) # 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10)) # 32 % 10 = 2

# min(item, item , item, or iterator)

print(min(42,5,2,33,223,-10,-1, 3)) # -10
print(min([552,23,5,5635])) # 5
print(min("a","b","A","X","B")) # A
print(min("a","b","X","Z","Mohammed")) # Mohammed
# المقارنة بين النصوص تتم حسب ترتيب الحروف في جدول الرموز
# الحروف الكبيرة تأتي قبل الحروف الصغيرة، لذلك تعتبر أصغر منها

# max(item, item , item, or iterator)

print(max(42,5,2,33,223,-10,-1, 3)) # 223
print(max([552,23,5,5635])) # 5635
print(max("a","b","A","X","B")) # b
print(max("a","b","X","Z","Mohammed")) # b

# slice(start(إختياري) = 0, end(إجباري), step(إختياري) = 1)

a = ["A","B","C","D","E","F","G"]

print(a[:5]) # ['A', 'B', 'C', 'D', 'E']
print(a[slice(5)]) # ['A', 'B', 'C', 'D', 'E'] / اعتبرها لنهاية لأنها إجبارية Endالخمسة قيمة ال 
print(a[slice(0,5,2)]) # ['A', 'C', 'E']
