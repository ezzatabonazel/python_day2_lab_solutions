import re   
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
while True : 
    n=input("please your name : ")
    if n.isalpha() : 
        info={"name": n}
        E=input("please your your email : ")

        if(re.search(regex,E)):   
            info["Email"]= E 
        else:   
            print("Invalid Email")
            continue
        print(info)
        break
    elif n.isspace() :
        print("invaild name")
    else :
        print("invaild name")

