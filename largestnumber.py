num1,num2,num3=map(int,input().split())
if (num1>=num2) and (num1>=num3):
  print("%d is largest"%num1)
elif (num2>=num3):
  print("%d is largest"%num2)
else:
  print("%d is largest"%num3)  
