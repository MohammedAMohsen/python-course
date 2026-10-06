# Assignment 01

my_list = [1, 2, 3, 3, 4, 5, 1]

mySet = set(my_list)
unique_list1 = list(mySet)

myTuple = tuple(unique_list1[0:-1])
unique_list2 = list(myTuple)

print(unique_list1) # [1, 2, 3, 4, 5]
print(unique_list2) # [1, 2, 3, 4]
print(type(unique_list1)) # <class 'list'>
# _______________________________________________________________________________________________________
# Assignment 02

nums = {1, 2, 3}
letters = {"A", "B", "C"}

nums.update(letters)
print(nums)                 # {1, 2, 3, 'C', 'B', 'A'} -> ترتيب الحروف قد يختلف عندك

print(nums | letters)       # {1, 2, 3, 'C', 'B', 'A'}

print(nums.union(letters))  # {1, 2, 3, 'C', 'B', 'A'}
# _______________________________________________________________________________________________________
# Assignment 03

my_set = {1, 2, 3}

print(my_set) # {1, 2, 3}

my_set.clear()
print(my_set) # set()

my_set.update({"A", "B"}) 
print(my_set) # {'A', 'B'}

my_set.discard("C")
# _______________________________________________________________________________________________________
# Assignment 04

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two)) # True
# _______________________________________________________________________________________________________
# Assignment 05

mySkills = {
    "skillOne" : {
        "name" : "Html",
        "progress" : "95%"
    },
    "skillTwo" : {
        "name" : "Css",
        "progress" : "90%"
    },
    "skillThree" : {
        "name" : "Js",
        "progress" : "80%"
    } 
}

print(f"{mySkills['skillOne']['name']} Progress Is {mySkills['skillOne']['progress']}")
print(f"{mySkills['skillTwo']['name']} Progress Is {mySkills['skillTwo']['progress']}")
print(f"{mySkills['skillThree']['name']} Progress Is {mySkills['skillThree']['progress']}")

mySkills.update({"skillFour" : {"name" : "Python", "progress" : "99.9%"}})

print(f"{mySkills['skillFour']['name']} Progress Is {mySkills['skillFour']['progress']}")
