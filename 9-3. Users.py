"""9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the users information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user."""
from datetime import date, datetime

class User():
    def __init__(self, first_name, last_name, profile_picture, age, date_account_created):
        self.fname = first_name
        self.lname = last_name
        self.profile_Pic = profile_picture
        self.age = age
        self.date_Acc_Created = date_account_created
    
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

HuzDateCreated = date(year=2022, month=1,day=24)
AmyDateCreated = date(year=2022, month=1,day=24)
IbsDateCreated = date(year=2022, month=1,day=20)

User_Huz = User("Huz", "Pro", "Huz logo.png", 19, HuzDateCreated.strftime("%x"))
User_Amy = User("Amy", "8765", "Cat Pic.png", 19, AmyDateCreated.strftime("%x"))
User_Ibs = User("Is", "Ibs", "Reaper.png", 16, IbsDateCreated.strftime("%x"))

User_Huz.describe_user()
User_Amy.describe_user()
User_Ibs.describe_user()

User_Huz.greet_user()
User_Amy.greet_user()
User_Ibs.greet_user()