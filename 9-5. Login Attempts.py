"""9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another 
method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. Print the value of 
login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0."""

from datetime import date, datetime

class User():
    def __init__(self, first_name, last_name, profile_picture, age, date_account_created, login_attempts):
        self.fname = first_name
        self.lname = last_name
        self.profile_Pic = profile_picture
        self.age = age
        self.date_Acc_Created = date_account_created
        self.login_attempts = login_attempts
    
    def describe_user(self):
        print("\nUser's First Name: "+self.fname)
        print("User's Last Name: "+self.lname)
        print("User's Age: "+str(self.age))
        print("User's Profile Picture: "+self.profile_Pic)
        print("User's Account's Creation Date: "+str(self.date_Acc_Created))

    def greet_user(self):
        print("\nYo what up "+self.fname+" ma friggin "+self.lname+"er!")
        print("I see your profile pics lookin slick af o:"+self.profile_Pic)
        print("Sooo wacha plannin on doin? yk you're "+str(self.age)+" yea? you got any plans?")
        print('Maaaaaan its been so long since we first met, honestly... so glad i met you on '+str(self.date_Acc_Created)+". \nYou're awesome :D")

    def incriment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


AmyDateCreated = date(year=2022, month=1,day=24)

User_Amy = User("Amy", "8765", "Cat Pic.png", 19, AmyDateCreated.strftime("%x"), 0)

User_Amy.describe_user()

User_Amy.greet_user()

User_Amy.incriment_login_attempts()
User_Amy.incriment_login_attempts()
User_Amy.incriment_login_attempts()
User_Amy.incriment_login_attempts()
User_Amy.incriment_login_attempts()



print("Login attempts before reset: "+str(User_Amy.login_attempts))

User_Amy.reset_login_attempts()

print("Login attempts after reset: "+str(User_Amy.login_attempts))