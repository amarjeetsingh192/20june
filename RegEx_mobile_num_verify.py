import re
def isValid(num):
    # 1) Begins with 0 or 91
    # 2) Then contains 6,7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    return Pattern.match(num)

num = input("Enter your mobile number : ")
if (isValid(num)):
    print("Valid Number")
else:
    print("Invalid Number")

