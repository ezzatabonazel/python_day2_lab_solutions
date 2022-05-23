print("guess the word of 3 char in 7 times by enter one char for each ")
word=["a","n","t"]
guess=["-","-","-"]
for i in range(7) :
    if word==guess :
        print("good job")
        break
    char=input("enter character  : ")
    if char == "a" :
        guess[0]="a"
        print(guess)
    elif char == "n" :
        guess[1]="n"
        print(guess)
    elif char == "t" :
        guess[2]="t"
        print(guess)
    elif char not in word :
        continue
else:
    print("opps you ran out of tries")
