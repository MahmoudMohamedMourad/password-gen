#1- import string module
#2- store all characters in lists (upper ,lower case , digists , punctuations)
#3_ take number of characters from usr
#-4 make sur the namber of characters is 6 or more
# 5 shuffle all lists 
# 6 calculate 30% and 20% of namber of character 
# 7create password 60% letters and 40 % digits and punctution 2  
import string 
import random
s1 =list(string.ascii_lowercase)
s2 =list(string.ascii_uppercase)
s3 =list(string.digits)
s4 =list(string.punctuation)


chracters_number= input("how many chracters for the password")

while True: 
    try:
        chracters_number = int (chracters_number)
        if chracters_number< 6 :
            print ("you need at least 6 chracters")
            chracters_number= input("please enter the number again")
        else :
            break
    except : 
        print("please enter number only")
        chracters_number= input("please enter the number again")
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(chracters_number* (30/100))
part2 = round(chracters_number*(20/100))

password = []

for i in range (part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range (part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)      

password= "".join(password[0:])
print(password)