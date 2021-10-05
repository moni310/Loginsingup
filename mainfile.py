import json
detail={}
new ={}
user=input("what do you want to do for singup 1 \n for login 2-----")
if user=="1":
    user_name=input("enter the name----")
    password1=input("enter your  password1 \n  please enter your confirm password----")
    password2=input("enter your password2=")
    if len(password1)>=1 and len(password1)<=12:
        if "@" in password1 or "$" in password1 or "#" in password1:
            if "0" or "9" in password1:
                if "A" or "Z" in password1:
                    if "a" or "z" in password1:
                        pass
                        # print("strong password")
                    else:
                        print("there is not small later")
                else:
                    print("week password")
            else:
                print("wrong password")
        else:
            print("wrong")
    else:
        print("your lenth is long")
    if password1==password2:
        pass
    else:
        print("both are not equal")
    with open("underdeatils1.json") as f:
        data=json.load(f)
    for i in data["user"]:
        if user_name in i["name"]:
            print("user already exists")
            print("your signup id is succesfully")
            break
    else:
        ("signed up successfully!")
        description=input("enter the description=")
        dob=input("enter the dob=")
        hobbies=input("enter the hobbies=")
        gender=input("enter the gender=")
        detail["name"]=user_name
        detail["password"]=password1
        new["description"]=description
        new["dob"]=dob
        new["hobbies"]=hobbies
        new["gender"]=gender
        detail["profile"]=new
        data["user"].append(detail)
        with open("underdeatils1.json","w") as f:
            json.dump(data,f,indent=2)
elif user=="2":    
    with open("underdeatils1.json") as f:
        data=json.load(f)
    user_name=input("enter the name=")
    password1=input("enter the pasword=")
    file=open("underdeatils1.json","r")
    maindata=json.load(file)
    file.close()
    i=0
    while i<len(data["user"]):
        load_data=(maindata["user"][i])
        if load_data["name"] ==user_name and load_data["password"]==password1:
            
            print(user_name,"congratulation your login is succesfull")
            print("---profile----")
            print("Username",user_name)
            print("gender",load_data["profile"]["gender"])
            print("bio",load_data["profile"]["description"])
            print("hobby",load_data["profile"]["hobbies"])
            print("dob",load_data["profile"]["dob"])
            break
        i=i+1
    else:
        print("Invalid password")