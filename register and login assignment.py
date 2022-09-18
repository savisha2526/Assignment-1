def register():
    db = open("database.txt","r")
    username = input("Enter Your Email Id as username:")
    password = input("create password:")
    password1 = input("confirm password:")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    SpecialSym = ['$', '@', '#', '%', '!','~','^','&','*']
    Special_char = ['@' and '.']     
    if password != password1:
        print("password dont match, restart")
        register()
    else:
        if len(password)<=5:
            print("password too short, restart:")
            register()
        elif len(password)>=16:
            print("password too long, restart:")
            register()
        elif not any(char.isupper() for char in password):
            print("Must have minimum one uppercase")
            register()
        elif not any(char.islower() for char in password):
            print("Must have minimum one lowercase")
            register() 
        elif not any(char in SpecialSym for char in password):
            print("Must have minimum one special character")
            register()
        elif not any(char.isdigit() for char in password):
            print("Must have minimum one digit")
            register()
        elif not any(char in Special_char for char in username):
            print("email or username should have @ and followed by . ")
            register()
        elif not username[0].isalpha():
            print("username should be start with alphabetical")
            register()
        elif username in d:
            print("username already exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(username+", "+password+"\n")
            print("Success!") 
 
def access():
    db = open("database.txt", "r")
    username = input("Enter Your Email Id as username:")
    password = input("Enter your password:")
    
    if not len(username or password)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login success")
                        print("hi,", username)
                    else:
                        print("password or uesername incorrect")
                except:
                    print("incorrect username or password")
            else:
                print("username or password dosen't exist")                               
        except:
            print("username or password dosen't exist")            
    else:
        print("Please enter a value")
        
def home(option=None):
    option = input("Login | Registration:")
    if option == "Login":
        access()
    elif option == "Registration":
        register()
    else:
        print("please enter an option")
home()            