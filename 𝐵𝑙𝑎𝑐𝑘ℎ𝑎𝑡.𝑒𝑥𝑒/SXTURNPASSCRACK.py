import string
import random
password = input("Enter your password: ")
# print(char)

while True:
   var = random.choices(char, k=len(password))
   print(">>>>>>>>>>>", var,">>>>>>>>>>")
   ps = "".join(var)
   if password == ps
       print ("Your Password is ", ps)
       break