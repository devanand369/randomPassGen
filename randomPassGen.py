
#!/usr/bin/python3

import random, string
import pyttsx3 as say

print("\n\n\t\t*+*+ Dev's Password Generator *+*+\n\n")

greeting = ['Welcome to Dev\'s Password Generator !',"Let's Generate a most complex password Within few seconds !","Let's get most secure password !"]
say.speak(greeting[random.randint(0,len(greeting)-1)])


say.speak('Enter the length of password you want to generate (only positive intergeral values) !')
lth = input("Enter password length to generate : \n")
say.speak('If you want number , enter any numerical or alphabetical letter,  otherwise press enter !')
query = input("If you want number , enter 'any num/alphabetical letter' : \n ")

passPow = {'1':'weak','2':'strong','3':'very'}
print('''
Choose the strength of password : \n
[1] Weak\n
[2] Strong\n
[3] Very strong\n\n
''')
say.speak('''
Choose the strength of password : \n
[1] Weak\n
[2] Strong\n
[3] Very strong\n\n
''')
strnth = input()

# function to generate random password
def password(length, num=False, strength='weak') :

    """length = length of password , it is integer type .
    num if you want number,
    and strength (weak, strong , very) """
    passPow = {'1':'weak','2':'strong','3':'very'}
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    letter=lower + upper
    dig=string.digits
    punct=string.punctuation
    psswd = ''

    if strength == 'weak' :
        if num:
            length -=2
            for i in range(2):
                psswd +=random.choice(dig)
        for i in range(length):
            psswd +=random.choice(lower)


    elif strength == 'strong' :
        if num :
            length -=2
            for i in range(2):
                psswd +=random.choice(dig)
        for i in range(length):
            psswd +=random.choice(letter)

    elif strength == 'very':
        ran = random.randint(2,4)
        if num:
            length -=ran
            for i in range(ran):
                psswd +=random.choice(dig)
        length -=ran
        for i in range(ran):
            psswd +=random.choice(punct)
        for i in range(length):
            psswd +=random.choice(letter)


    psswd = list(psswd)
    random.shuffle(psswd)

    return ''.join(psswd)

genPass=password(int(lth), num=bool(query), strength=passPow[strnth])
print("\n\nYour generated password : \t>>>>>\t"+genPass+"\t<<<<<\n")
say.speak('Your generated password be \t'+genPass)
