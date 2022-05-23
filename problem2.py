def divisible(num):
    if num%3==0 and num%5==0 :
        print("FIZZBUZZ")
    elif num%3==0 :
        print ("FIZZ")
    elif num%5==0 :
        print("BUZZ")
    else :
        print ("not divisble by 3 or 5")
    

divisible(2)
