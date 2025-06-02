class chatbook:
    
    __user_id = 0
    
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = 'Default User'
        self.username = ''
        self.password = ''
        self.loggedin = False
        #self.menu()
        
    @staticmethod    
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val
        
    def get_name(self):
        return self.__name
    
    def set_name(self,value):
        self.__name = value
        
        
    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed? 
                           1. Press 1 to sign up
                           2. Press 2 to sign in
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           -> """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.send_message()
        else:
            exit()
            
    def signup(self):
        email = input("Enter your email here ->: ")
        pwd = input("setup your password here ->: ")
    
        self.username = email
        self.password = pwd
        print("You have signed up successfully!")
        print("\n")
        self.menu()
        
        
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please sign up first!")
        else:
            uname = input("Enter your username here ->: ")
            pwd = input("Enter your password here ->: ")
            
            if self.username == uname and self.password == pwd:
               print("You have signed in successfully!")    
               self.loggedin = True 
            else:
                print("Invalid username or password. Please try again.")
        
        print("\n")
        self.menu()
        
    def my_post(self):
        if self.loggedin == True:
            post = input("Write your post here ->: ")
            print(f"Your post: {post}")
        else:
            print("You need to sign in first to write a post.")
        print("\n")
        self.menu()
        
    def send_message(self):
        if self.loggedin == True:
            msg = input("Write your message here ->: ")
            frnd = input("Enter the name of your friend ->: ")
            print(f"Message sent to {frnd}: {msg}")
        else:
            print("You need to sign in first to write a post.")
        print("\n")
        self.menu()
        
obj = chatbook()

