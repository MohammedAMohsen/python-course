# Assignment 01

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars(Name):
    return Name[1:-1]

cleaned_list = map(remove_chars, friends_map)

for name in cleaned_list:

    print(name)

# -- With Lambda --

for NameClen in map(lambda name: name[1:-1], friends_map):

    print(NameClen)

# _______________________________________________________________________________________________________
# Assignment 02

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names(Name):
    return Name.endswith("m")

names = filter(get_names, friends_filter)

for name in names:
    print(name)

# -- With Lambda --

for name in filter(lambda name: name.endswith("m"), friends_filter):

    print(name)

# _______________________________________________________________________________________________________
# Assignment 03

nums = [2, 4, 6, 2]

from functools import reduce

def mutnum(num1, num2):
    return num1 * num2

print(reduce(mutnum, nums))

# -- With Lambda --

print(reduce(lambda num1, num2: num1 * num2, nums))

# _______________________________________________________________________________________________________
# Assignment 04

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

def filterSkills(Skill):
    return isinstance(Skill, str)

filterSkills = filter(filterSkills, skills)

for numrec, skill in enumerate(reversed(list(filterSkills)),50):
    print(f"{numrec} - {skill}")

# -- With Lambda --

for numrec, skill in enumerate(reversed(list(filter(lambda skill: isinstance(skill, str), skills))),50):
    print(f"{numrec} - {skill}")

