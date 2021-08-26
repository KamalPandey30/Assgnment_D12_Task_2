import os.path
spcl = ['@', '#','!','~','$','%','^','&','*','(',',','-','+','/',':','.',',','<','>','?','|']

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def emailIsValid(mail):
    c = 0
    f = 0
    if ((mail[0] in spcl) | (mail[0] in arr)):
        return False
        
    if (" " in mail):
        return False

    if ("@" in mail) and ("." in mail):
        for i in range(len(mail)):
            if mail[i]=="@":
                f = i
            if mail[i] == ".":
                c = i
        if ((f+1 == c)):
            return False

    else:
        return False        
    return True

def passIsValid(password):
    if (len(password) < 5 or len(password) > 16):
        return False

    if (" " in password):
        return False
  
    if (True):
        count = 0
        for i in password:
            if i in arr:
                count = 1
                break
  
        if count == 0:
            return False

    if True:
        count = 0
  
        for i in password:
            if i in arr:
                count = 1
                break
        if count == 0:
            return False
  
    if True:
        count = 0
        for i in range(65, 91):
            if chr(i) in password:
                count = 1
        if (count == 0):
            return False
  
    if (True):
        count = 0
        for i in range(90, 123):
  
            if chr(i) in password:
                count = 1
  
        if (count == 0):
            return False
    return True



def register():
	Username = input("Enter a username:")
	Flg = emailIsValid(Username)
	if Flg == False:
	    print("Enter Username again")
	    register()
	else:
	    Password = input("Create password:")
	    Flgp = passIsValid(Password)
	    if Flgp == False:
	        print("Password does not meet the criteria. please enter Username and passwrod again")
	        register()
	    else:
	        d = []
	        if os.path.isfile("database.txt"):
	            db = open("database.txt", "r")
	            for i in db:
	                a,b = i.split(",")
	                b = b.strip()
	                c = a,b
	                d.append(a)
	            db.close()
	            if Username in d:
	                print("Username exists")
	                register()
	            else:
	                db = open("database.txt", "a")
	                db.write(Username+", "+Password+"\n")
	                db.close()
	                print("User created successfully!")
	                print("Please login to proceed:")
	                userinput()
	        else:
	            db = open("database.txt", "a")
	            db.write(Username+", "+Password+"\n")
	            db.close()
	            print("User created successfully!")
	            print("Please login to proceed:")
	            userinput()
                       

def Login():
	Username = input("Enter your username:")
	Password = input("Enter your Password:")
		
	
	db = open("database.txt", "r")
	d = []
	f = []
	for i in db:
	    print("i is ", i)
	    a,b = i.split(",")
	    b = b.strip()
	    c = a,b
	    d.append(a)
	    f.append(b)
	    print(a,b,d,f)
	db.close()
	data = dict(zip(d, f))
	if Username not in d:
	    print("Wrong Username. Please type again. if USername doesnot exist. please register first")
	    userinput()
	else:
	    try:
	        if Password == data[Username]:
	            print("Login success!")
	            print("Hi", Username)
	        else:
	            print("Incorrect password or username")
	            print(" Please type again. if USername doesnot exist. please register first")
	            userinput()
	    except:
	        print("Incorrect password or username. Please type again. if USername doesnot exist. please register first")
	        userinput()


def forgotpasswrd():
    Username = input("Enter your username:")
    if True:
        db = open("database.txt", "r")
        d = []
        f = []
        for i in db:
            a,b = i.split(",")
            b = b.strip()
            c = a,b
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        if Username in d:
            print(data[Username])
        else:
            print("wrong username. Please enter the user name again")
            userinput()



def userinput():
    print("Welcome, Please choose an option")
    print( "1 for register, 2 for login, 3 for forgot password" )
    userInput = int(input())

    if userInput == 1:
        register()
    elif userInput ==2:
        Login()
    elif userInput ==3:
        forgotpasswrd()
    else:
        print("wrong Input")
        print(" please choose again")
        userInput()


print("Welcome. ")
userinput()




