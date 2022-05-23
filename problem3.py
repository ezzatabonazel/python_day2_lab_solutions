def reverse(s:str):
    s2 = ""
    for i in s:
        s2 = i + s2
    print(s2)

string = input("enter a string : \n ")
reverse(string)