import random;
target=random.randint(1,100)
count=1
while True:
    n=input("Enter the target number or Quit(Q) option to quit:")
    if(n.upper()=="Q"):
        print("Exited from the game")
        break
    try:
        n=int(n)
    except ValueError:
        print("Invalid input,Try again with a valid input")
        continue
    if(n==target):
        print(f"Target found in {count} tries, Congratulations")
        break
    elif(n>target):
        print("n is greater than target,Try again with a smaller number")
        count+=1
    else:
        print("n is less than target,Try again with a greater number")
        count+=1
   
print("---GAME OVER---")