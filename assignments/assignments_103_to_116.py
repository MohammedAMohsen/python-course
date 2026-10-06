# Assignment 01

class Game:

    def __init__(self, name, developer, year, price):

        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):

        return self.price * 15.6
    
game_one = Game("PUBG", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# Output:

# Game Name Is "PUBG", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0
        
# _______________________________________________________________________________________________________
# Assignment 02

class User:
    
    def __init__(self, fname, lname, age, gender):

        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def full_details(self):

        if self.gender.lower() == "male":

            return f"Hello Mr {self.fname} {self.lname[0]}. [{str(40-self.age).zfill(2)}] Years To Reach 40"
        
        elif self.gender.lower() == "female":

            return f"Hello Mrs {self.fname} {self.lname[0]}. [{str(40-self.age).zfill(2)}] Years To Reach 40"
        
        else:

            return f"Hello {self.fname} {self.lname}: [{str(40-self.age).zfill(2)}] Years To Reach 40"
        
user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40

# _______________________________________________________________________________________________________
# Assignment 03

class Message:
    
    @staticmethod
    def print_message():
    
        return "Hello From Class Message"


print(Message.print_message()) # Hello From Class Message

# _______________________________________________________________________________________________________
# Assignment 04

class Games:
  
    def __init__(self, games):

       self.games = games

    def show_games(self):

        if isinstance(self.games, str):

            print(f"I Have One Game Called \"{self.games}\"")
        
        elif isinstance(self.games, list):

            print("I Have Many Games:")

            for g in self.games:

                print(f"-- {g}")

        elif isinstance(self.games, int):

            print(f"I Have {self.games} Games.")
        
        else:
            print("Invalid Data")
        

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games() # I Have One Game Called "Shadow Of Mordor"

my_games_count.show_games() # I Have 80 Games.

my_games_names.show_games()

# Output

# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

# _______________________________________________________________________________________________________
# Assignment 05

class Members:

    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"
  
  
class Admins(Members):
  
    def __init__(self, n, p):
       
        Members.__init__(self, n, p)


class Moderators(Members):
   
    def __init__(self, n, p):
       
       super().__init__(n, p)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info()) # Your Name Is Osama And You Are Admin
print(member_two.show_info()) # Your Name Is Ahmed And You Are Moderator

# _______________________________________________________________________________________________________
# Assignment 06

class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three

class Name(A, B, C):
  
    def __init__(self, one, two, three):
        A.__init__(self,one)
        B.__init__(self,two)
        C.__init__(self,three)
      
    def show_name(self):
    
      return f"The Name Is {self.one}{self.two}{self.three}"
    
the_name = Name("El", "ze", "ro")

print(the_name.show_name()) # The Name Is Elzero
