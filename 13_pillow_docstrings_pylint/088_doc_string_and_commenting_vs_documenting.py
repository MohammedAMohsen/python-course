# Lesson 088 - Docstring And Commenting vs Documenting
# Video: https://www.youtube.com/watch?v=6skfWbMu9MY

# --------------------------------------------
# -- Doc String & Commenting vs Documenting --
# --------------------------------------------
# [1] Documentation String For Class, Module or Function
# [2] Can Be Accessed From The Help and Doc Attributes
# [3] Made For Understanding The Functionality of The Complex Code
# [4] Theres One Line and Multiple Line Doc Strings
# -------------------------------------------------

# Documentation one line:

def albasha_function(name):

    '''This Is Function To Say Hello From ALbasha''' # => this is Documentation one line

    print(f"Hello {name} From Albasha")

albasha_function("Mohammed") # Hello Mohammed From Albasha

# print(dir(albasha_function)) # func الي كتبتها داخل ال Documentationوهذا بيظهر ال doc من ضمنهم ال func بظهر جميع محتويات والآتريبيوت لل

print(albasha_function.__doc__) # This Is Function To Say Hello From ALbasha

# help(albasha_function) # help وأيضا بقد اشوفها من خلال 

# -----------------------------------------------------------------

# Documentation Multiple Line:

def albasha_function2(name):

    '''
    This Is Function:
        To Say Hello
        From ALbasha

    parameter:
        name => Person Name That Use Function

    Return:
        Return Hello Message To The Person

    GoodBye :)
    ''' 

    print(f"Hello {name} From Albasha")


print(albasha_function2.__doc__)
