class User:
	name = ''
	email = ''
	password = ''
    login = False 

    def login(self):
    	email = input("Enter email")
    	password =input("Enter password")

    	if email == self.email and password == self.password:
    		login = True
    		print("Login Successful!")
    	else:
    		print("Login failed!")

    def logout(self):
    	login = False
    	print("Logged out!")

    def isLoggedIn(self):
    	if self.login:
    		return True
    	else:
    		return False

    	def profile(slef):
    		if isLoggedIn():
    		    print(self.name,"\n",self.email)
    		else:
    			print("User is not Loggedin!")


   user1 = User()

   user1.name = "Tusher"
   user1.email = "tushaer@gmail.com"
   user1.password = "123456"

   user1.login()
   


