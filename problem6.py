total=0
i=0
while True :
    num=input("please enter numbers only : ")
    if num=="done":
        break
    elif num.isdigit():
        number=int(num)
        total=total+number
        i=i+1
    else :
        print("invaild input")
        continue
avg=total/i
print(f"the total of your entries is {total}, the count is {i} , the avreage is {avg}")
