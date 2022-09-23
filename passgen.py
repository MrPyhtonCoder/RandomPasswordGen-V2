import time
import random
from pyfiglet import figlet_format
print (figlet_format ("Random Password Gen V2", font = "epic"))
time.sleep (1)
print ("Welcome To The Random Password Generator")
time.sleep (2)
print("Do You Want To Generate A Random Password")
i1 = input("    yes or no only =>     ")
if i1 != "yes":
    quit ()
lower_case = "abcdefghijkmnlopqrstuvwxyz"
upper_case = "ABCDEFGHIJKMNLOPQRSTUVWXYZ"
num = "1234567890"
symbol = "[]{}*()._-"
ans = lower_case + upper_case + num + symbol
length = int(input("Enter The Length Of Your Becoming Password      "))
time.sleep (2)
password = "".join(random.sample(ans,length))
print ("Generating Password .....")
time.sleep (5)
print ("Random Generated Password Is       ",password)
print("Do You want To Generate Another Password?")
i2 = input("    yes or no only =>     ")
if i2 != "yes":
    quit ()
time.sleep (1)
length2 = int(input("Enter The Length Of Your Becoming Password      "))
print ("Generating Password .....")
time.sleep (4)
lower_case2 = "abcdefghijkmnlopqrstuvwxyz"
upper_case2 = "ABCDEFGHIJKMNLOPQRSTUVWXYZ"
num2 = "1234567890"
symbol2 = "[]{}*()._-"
ans2 = lower_case2 + upper_case2 + num2 + symbol2
password2 = "".join(random.sample(ans2,length2))
print ("Random Generated Password Is       ",password2)