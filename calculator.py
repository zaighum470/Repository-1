def add(a,b):
    return a+b 
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Math error"
        return a/b
while True:

  print("\nsimple calculator")
  print("\n1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVIDE\n5.EXIT")
  choice = int(input("Enter number between (1-5): "))
  if choice >=6:
     print("sorry you have only 5 choices! \nRefresh agian !")
     break
  if choice ==5 :
    print("GOOD BYE!")
    break
  
  num1=int(input("Enter the first number: "))
  num2=int(input("Enter the second number: "))
  
  if choice == 1:
     print("Results:",add(num1,num2))
  elif choice == 2:
     print("Results:",subtract(num1,num2))
  elif choice == 3:
     print("Results:",multiply(num1,num2))
  elif choice == 4:
     print("Results:",divide(num1,num2))
  else:
     print("Invalid inputs")