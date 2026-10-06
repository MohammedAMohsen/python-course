# Lesson 039 - Practical - Email Slice
# Video: https://www.youtube.com/watch?v=jQVMF7kEzvI

# ---------------------------
# -- Practical Slice Email --
# ---------------------------

# email = "user.name@example.org"
# print(email[0:email.index("@")]) # user.name -> @ضلك ماشي بطباعة لحد ما توصل علامة ال 


theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input('What\'s Your Email ?').strip()

theUsername = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@")+1:] # (+1) -> @إطبع من بعد ال

# طريقة ثانية للإستخراج
# theUsername = theEmail.split("@")[0]
# theWebsite = theEmail.split("@")[-1]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername}\nYour Website Is {theWebsite}")
