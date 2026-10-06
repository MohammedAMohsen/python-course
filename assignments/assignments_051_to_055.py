# Assignment 01

my_nums = [15, 81, 5, 17, 20, 21, 13]
x = 0
for number in sorted(my_nums, reverse=True):
    if number % 5 == 0:
        x += 1
        print(f"{x} => {number}")
else:
    print("All Numbers Printed")
# _______________________________________________________________________________________________________
# Assignment 02

for num in range(1,21):
    if num == 6 or num == 8 or num == 12:
        continue
    print(str(num).zfill(2))
else:
    print("All Numbers Printed")
# _______________________________________________________________________________________________________
# Assignment 03

my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}
sumRank = 0
for key_rank, val_rank in my_ranks.items():
    if val_rank == 'A':
        newRank = 100
    elif val_rank == 'B':
        newRank = 80
    elif val_rank == 'C':
        newRank = 40
    sumRank += newRank
    print(f"My Rank in {key_rank} Is {val_rank} And This Equal {newRank} Points.")
else:
    print(f"Total Points Is {sumRank}")
# _______________________________________________________________________________________________________
# Assignment 04

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

points_rank = {"A":100, "B":80, "C":40, "D":20}

# ===================================================
# ================== First Method ===================
# ===================================================

for stud in students:

    sumRank = 0

    print("-" * 35)
    print(f"-- Student Name => {stud}")
    print("-" * 35)

    for supject in students[stud]:

        sumRank += points_rank[students[stud][supject]]

        print(f"- {supject} => {points_rank[students[stud][supject]]} Points.")

    print(f"Total Points For {stud} Is {sumRank}")

# ===================================================
# ================== Second Method ==================
# ===================================================

for key_student, val_student in students.items():

    sumRank = 0

    print("-" * 35)
    print(f"-- Student Name => {key_student}")
    print("-" * 35)

    for supject, rank in val_student.items():

        sumRank += points_rank[rank]

        print(f"- {supject} => {points_rank[rank]} Points.")

    print(f"Total Points For {key_student} Is {sumRank}")
