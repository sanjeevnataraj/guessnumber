import random
print("WELCOME TO THE GAME")
print("Guess the number between 0 to 100")
r=random.randint(0,100)
def guess(n,r):
    m=r-n
    if r==n:
        print("\nYour number is "+str(n)+" and random number is "+str(r)+" both are same")
        print("\nCongrats you finded the right one ")
        return 1
    if m<=10 and m>=0:
        print("Your guess is too close")
    elif m>=-10 and m<0:
        print("Your guess is little far")
    elif n>r:
        print("Your guess is greater than the number")
    else:
        print("Your guess is smaller than the number")
while True:
    n=int(input("Enter the number : "))
    c=guess(n,r)
    if c==1:
        break
    
