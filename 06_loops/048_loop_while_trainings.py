# Lesson 048 - Loop - While Training's
# Video: https://www.youtube.com/watch?v=9rU2fImqSR4

# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "No", "Ma", "Ha", "Wa", "Ta", "Bv"]

x = 0
while x < len(myF):
    print(f"#{str(x+1).zfill(2)} {myF[x]}")
    x += 1
else:
    print("All Friends Printed to Screen :)")

#01 Os
#02 Ah
#03 Ga
#04 Al
#05 Ra
#06 Sa
#07 No
#08 Ma
#09 Ha
#10 Wa
#11 Ta
#12 Bv
#All Friends Printed to Screen :)
