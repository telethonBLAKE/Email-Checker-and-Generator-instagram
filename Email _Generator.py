# Python version: 3.9.7
# Date: 6/23/2022
# Author: Blake @A_W_9
# Description: Email Generator
# Telegram channel: https://t.me/J_P_1

#Libraries
import string
import random

#Msg start
print("Telegram Channel:"'\n'"https://t.me/J_P_1")
print("1 - yahoo"'\n'"2 - gmail"'\n'"3- Hotmail"'\n'"Choose any domain")

#Variables
letters = string.ascii_lowercase
email = int(input("domain : "))
Generator = int(input("How many emails: "))
STOP = 0
Letters = 0
File_Email = open("email.txt", "w")
ranges = int(input("email characters range : "))

#Loop
while True:


    if email == 1:
        File_Email.write(''.join(random.choice(letters) for i in range(ranges))+'@yahoo.com'+'\n')
        STOP += 1
        if STOP == Generator:
            break

    if email == 2:
        File_Email.write(''.join(random.choice(letters) for i in range(ranges)) + '@gmail.com' + '\n')
        STOP += 1
        if STOP == Generator:
            break

    if email == 3:
        File_Email.write(''.join(random.choice(letters) for i in range(ranges)) + '@Hotmail.com' + '\n')
        STOP += 1
        if STOP == Generator:
            break

#Msg end
print("Done Generator!")

