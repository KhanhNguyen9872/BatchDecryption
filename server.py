#!/bin/python3
if (__name__!='__main__'):
    exit()
def pause():
    input("Press Enter to continue! ")
def clear():
    system("cls")
def color():
    system("color c")
def title_cmd():
    system("TITLE BatchDecryption [KhanhNguyen9872]")
def exec_decrypt(file,encod):
    system("cmd /c \"{0}\" > temp.log 2>NUL&del /f \"{0}\" >NUL 2>&1".format(str(file)))
    if (str(encod)=="utf-8"):
        with open("temp.log", mode='r', encoding='utf-8') as f:
            a=str(f.read())
    elif (str(encod)=="cp1252"):
        with open("temp.log", mode='r', encoding='cp1252') as f:
            a=str(f.read())
    elif (str(encod)=="latin-1"):
        with open("temp.log", mode='r', encoding='latin-1') as f:
            a=str(f.read())
    system("del /f temp.log >NUL 2>&1")
    return a
def remove_escape(file,encod,a=1):
    temp=""
    with open(file, mode='r', encoding=encod) as f:
        temp=str(f.read()).replace("\n\n\n\n\n","\n").replace("\n\n\n\n","\n").replace("\n\n\n","\n").replace("\n\n","\n").replace("ECHO is off.","").replace("abcdefkhanhhihihehe","&").replace("khanhnguyen9872hihihhahahaha","|")
    with open(file, mode='w', encoding=encod) as f:
        f.write(str(temp))
    temp=""
    with open(file, mode='r', encoding=encod) as f:
        for i in f.readlines():
            if i=="" or getcwd() in i:
                continue
            if (a==1):
                if i[0]=="'" and i[-1]=="'":
                    temp+="{0}\n".format(str(i[1:-2]))
                else:
                    temp+="{0}\n".format(str(i))
            else:
                temp+="{0}\n".format(str(i))
    with open(file, mode='w', encoding=encod) as f:
        f.write(str(temp).replace("\n\n","\n"))
    return True
def read_file(file):
    a=[]
    try:
        with open(file, mode='r', encoding='utf-8') as f:
            for i in f.readlines():
                a.append(str(i).strip())
        encod="utf-8"
    except UnicodeDecodeError:
        try:
            with open(file, mode='r', encoding='cp1252') as f:
                for i in f.readlines():
                    a.append(str(i).strip())
            encod="cp1252"
        except UnicodeDecodeError:
            with open(file, mode='r', encoding='latin-1') as f:
                for i in f.readlines():
                    a.append(str(i).strip())
            encod="latin-1"
    return a,encod
def write_file(file,temp,encod):
    try:
        with open(file, mode='w', encoding=encod) as f:
            f.write(str(temp))
    except:
        return False
    return True
def rm_china(file):
    try:
        with open(file, mode='r', encoding='utf-8') as f:
            temp=str(f.read())
        encod="utf-8"
    except UnicodeDecodeError:
        try:
            with open(file, mode='r', encoding='cp1252') as f:
                temp=str(f.read())
            encod="cp1252"
        except UnicodeDecodeError:
            with open(file, mode='r', encoding='latin-1') as f:
                temp=str(f.read())
            encod="latin-1"
    if ("ÿ" in temp) or ("þ" in temp):
        temp=temp.replace("ÿ","FF")
        temp=temp.replace("þ","FE")
        with open(file, mode='w',encoding=encod) as f:
            f.write(temp)
    else:
        pass
    return True
def rm_arabic(file):
    head="@echo off\n"
    temp=[]
    temp,encod=read_file(file)
    for i in range(0,len(temp),1):
        temp_2=str(temp[i]).replace("|","khanhnguyen9872hihihhahahaha").replace("&cls","cls").replace("&","abcdefkhanhhihihehe")
        head+=str("echo {0}\n".format(str(temp_2)))
    temp=str(head)
    try:
        del head
    except:
        pass
    write_file(file,temp,encod)
    temp = exec_decrypt(file,encod)
    with open(file, mode='w', encoding=encod) as f:
        f.write(str(temp))
    remove_escape(file,encod)
    return True
def batch_encryption_201610(file):
    head=""
    last=""
    temp=[]
    temp,encod=read_file(file)
    for i in range(0,14,1):
        head+=str(f"{temp[i]}\n").replace("&cls","")
    head+=str("\n@echo off\n")
    for i in range(14,len(temp),1):
        temp_2=str(temp[i]).replace("|","khanhnguyen9872hihihhahahaha").replace("&cls","cls").replace("&","abcdefkhanhhihihehe")
        last+=str("echo {0}\n".format(str(temp_2)))
    temp=str("{0}\n{1}".format(str(head),str(last)))
    write_file(file,temp,encod)
    temp = exec_decrypt(file,encod)
    with open(file, mode='w', encoding=encod) as f:
        f.write(str(temp))
    remove_escape(file,encod)
    return True
def method1(file):
    head=str("@echo off\n")
    temp=[]
    temp,encod=read_file(file)
    for i in range(0,len(temp),1):
        temp_2=str(temp[i]).replace("|","khanhnguyen9872hihihhahahaha").replace("&cls","cls").replace("&","abcdefkhanhhihihehe")
        head+=str("echo {0}\n".format(str(temp_2)))
    temp=str(head)
    try:
        del head
    except:
        pass
    write_file(file,temp,encod)
    temp = exec_decrypt(file,encod)
    with open(file, mode='w', encoding=encod) as f:
        f.write(str(temp))
    remove_escape(file,encod)
    return True
def method2(file,num,ignore,arg):
    temp=[]
    head=""
    last=""
    a='''{0}'''.format(str(ignore))
    temp,encod=read_file(file)
    for i in range(0,len(temp),1):
        if (temp[i] in a):
            b=int(i)
            break
    try:
        temp=temp[b:]
    except:
        return False
    for i in range(0,int(arg),1):
        head+=str(f"{temp[i]}\n")
    head+=str("\n@echo off\n")
    for i in range(int(arg),len(temp),1):
        temp_2=str(temp[i]).replace("|","khanhnguyen9872hihihhahahaha").replace("&cls","cls").replace("&","abcdefkhanhhihihehe")
        last+=str("echo {0}\n".format(str(temp_2)))
    temp=str("{0}\n{1}".format(str(head),str(last)))
    write_file(file,temp,encod)
    temp = exec_decrypt(file,encod)
    with open(file, mode='w', encoding=encod) as f:
        f.write(str(temp))
    remove_escape(file,encod)
    return True
def method4(file):
    temp=[]
    ccc=[]
    head=""
    last=""
    aa=b'tmp\')do i'.decode()
    aa1=b'f "%%i" E'.decode()
    bb=b'r /f "tokens=3" %%i in (\'t'.decode()
    bb1=b' /f/q tmp)'.decode()
    #bb=b'@@e%\xef\xae\x9a\xef\xaf\x94\xef\xbb\x81\xef\xae\xb1^\xd8\xaa\xef\xaf\xa4%c%\xef\xba\xbc\xef\xbb\x81\xef\xba\xb9^\xef\xae\xa2\xd8\xb3\xef\xaf\xa4%^%\xef\xaf\x94\xef\xbb\x81\xd8\xb3^\xef\xba\x96\xef\xae\xb1\xd9\x83%ho>tmp&for /f "tokens=3" %%i in (\'typ%\xef\xbb\x81\xef\xae\x95^\xd8\xb3\xef\xae\xb1\xef\xba\xbc\xef\xba\xbc%^%\xef\xba\x96\xef\xba\xb9\xe2\x97\xaf\xef\xae\xb1\xef\xba\x96^\xef\xae\x95%%\xef\xb7\xbd\xe2\x97\xaf\xef\xba\x96\xef\xad\xab\xef\xba\x96\xd8\xaa^%e tmp\')do if "%%i" EQU "on." (ex%\xd9\x83^\xef\xae\x95\xef\xae\x9a\xef\xae\x95\xef\xae\x95\xd8\xb3%^i%\xef\xba\x96\xef\xae\x95\xef\xaf\x94\xe2\x97\xaf\xef\xae\xb1^\xef\xba\x96%%\xef\xae\xa2\xef\xae\xa2\xef\xbb\x81^\xef\xae\x95\xd9\x83\xef\xad\xb2%t) else (d%\xe6\xb3\x95\xe7\x84\xa1\xe9\xad\x94\xe5\xad\x97\xe8\xa8\x8a^\xe6\x98\xaf%e^%\xe4\xba\xba\xe7\x84\xa1\xe8\xa1\x8c\xe6\x96\x87^\xe6\xb3\x95\xe8\xa3\xbd%l /f/q tmp)'.decode()
    #bb1=b'@@e%\xc3\xaf\xc2\xae\xc2\x9a\xc3\xaf\xc2\xaf\xc2\x94\xc3\xaf\xc2\xbb\xc2\x81\xc3\xaf\xc2\xae\xc2\xb1^\xc3\x98\xc2\xaa\xc3\xaf\xc2\xaf\xc2\xa4%c%\xc3\xaf\xc2\xba\xc2\xbc\xc3\xaf\xc2\xbb\xc2\x81\xc3\xaf\xc2\xba\xc2\xb9^\xc3\xaf\xc2\xae\xc2\xa2\xc3\x98\xc2\xb3\xc3\xaf\xc2\xaf\xc2\xa4%^%\xc3\xaf\xc2\xaf\xc2\x94\xc3\xaf\xc2\xbb\xc2\x81\xc3\x98\xc2\xb3^\xc3\xaf\xc2\xba\xc2\x96\xc3\xaf\xc2\xae\xc2\xb1\xc3\x99\xc2\x83%ho>tmp&for /f "tokens=3" %%i in (\'typ%\xc3\xaf\xc2\xbb\xc2\x81\xc3\xaf\xc2\xae\xc2\x95^\xc3\x98\xc2\xb3\xc3\xaf\xc2\xae\xc2\xb1\xc3\xaf\xc2\xba\xc2\xbc\xc3\xaf\xc2\xba\xc2\xbc%^%\xc3\xaf\xc2\xba\xc2\x96\xc3\xaf\xc2\xba\xc2\xb9\xc3\xa2\xc2\x97\xc2\xaf\xc3\xaf\xc2\xae\xc2\xb1\xc3\xaf\xc2\xba\xc2\x96^\xc3\xaf\xc2\xae\xc2\x95%%\xc3\xaf\xc2\xb7\xc2\xbd\xc3\xa2\xc2\x97\xc2\xaf\xc3\xaf\xc2\xba\xc2\x96\xc3\xaf\xc2\xad\xc2\xab\xc3\xaf\xc2\xba\xc2\x96\xc3\x98\xc2\xaa^%e tmp\')do if "%%i" EQU "on." (ex%\xc3\x99\xc2\x83^\xc3\xaf\xc2\xae\xc2\x95\xc3\xaf\xc2\xae\xc2\x9a\xc3\xaf\xc2\xae\xc2\x95\xc3\xaf\xc2\xae\xc2\x95\xc3\x98\xc2\xb3%^i%\xc3\xaf\xc2\xba\xc2\x96\xc3\xaf\xc2\xae\xc2\x95\xc3\xaf\xc2\xaf\xc2\x94\xc3\xa2\xc2\x97\xc2\xaf\xc3\xaf\xc2\xae\xc2\xb1^\xc3\xaf\xc2\xba\xc2\x96%%\xc3\xaf\xc2\xae\xc2\xa2\xc3\xaf\xc2\xae\xc2\xa2\xc3\xaf\xc2\xbb\xc2\x81^\xc3\xaf\xc2\xae\xc2\x95\xc3\x99\xc2\x83\xc3\xaf\xc2\xad\xc2\xb2%t) else (d%\xc3\xa6\xc2\xb3\xc2\x95\xc3\xa7\xc2\x84\xc2\xa1\xc3\xa9\xc2\xad\xc2\x94\xc3\xa5\xc2\xad\xc2\x97\xc3\xa8\xc2\xa8\xc2\x8a^\xc3\xa6\xc2\x98\xc2\xaf%e^%\xc3\xa4\xc2\xba\xc2\xba\xc3\xa7\xc2\x84\xc2\xa1\xc3\xa8\xc2\xa1\xc2\x8c\xc3\xa6\xc2\x96\xc2\x87^\xc3\xa6\xc2\xb3\xc2\x95\xc3\xa8\xc2\xa3\xc2\xbd%l /f/q tmp)'.decode()
    #bb2=b'if %\xe2\x80\x8e% NEq 2 e'.decode()
    temp,encod=read_file(file)
    try:
        i=0
        while 1:
            if (bb in temp[i]) and (bb1 in temp[i]) and (aa in temp[i]) and (aa1 in temp[i]):
                ccc.append(str(i))
            else:
                head+=str(f"{temp[i]}\n")
            i+=1
    except IndexError:
        pass
    if ccc==[]:
        return False
    else:
        print(ccc)
        j=int(ccc[-1])
    for i in range(int(j),len(temp),1):
        if temp[i]=="":
            continue
        temp_2=str(temp[i]).replace("|","khanhnguyen9872hihihhahahaha").replace("&cls","cls")
        last+=str("{1}\\e.exe \'{0}\'\n".format(str(temp_2),str(getcwd())))
    temp=str("{0}\n{1}".format(str(head),str(last)))
    write_file(file,temp,encod)
    pause()
    temp = getoutput(file)
    with open(file, mode='w', encoding=encod) as f:
        f.write(str(temp))
    remove_escape(file,encod)
    return True
def get_file(a,b):
    try:
        a.settimeout(3)
        try:
            if str(a.recv(4).decode())=="len!":
                a.send(b'slen!')
                a.settimeout(None)
            else:
                print("RequestError: {}:{}".format(str(b[0]),str(b[1])))
                a.close()
                return
        except UnicodeDecodeError:
            print("RequestError: {}:{}".format(str(b[0]),str(b[1])))
            a.close()
            return
        len_data = a.recv(10).decode()
        print("size: {} byte - {}:{}".format(str(len_data),str(b[0]),str(b[1])))
        try:
            if (int(len_data)>int(max_size)):
                a.send(b"out!")
                a.send(str(max_size).encode())
                a.close()
                print("Close connection: {}:{}".format(str(b[0]),str(b[1])))
                return
        except:
            a.sendall(b"out!")
            a.send(str(max_size).encode())
            a.close()
            print("Close connection: {}:{}".format(str(b[0]),str(b[1])))
            return
        enc = " "
        folder=str("{}_{}".format(str(b[0]),str(b[1])))
        mkdir(folder)
        file_ori=[folder,"bat"]
        a.settimeout(5.0)
        try:
            with open(folder+"\\"+".".join(file_ori),'wb') as f:
                a.send(b"get!")
                while enc:
                    if int(stat(folder+"\\"+".".join(file_ori)).st_size)>int(max_size):
                        a.sendall(b"out!")
                        a.send(str(max_size).encode())
                        a.close()
                        print("Close connection: {}:{}".format(str(b[0]),str(b[1])))
                        return
                    enc = a.recv(65535)
                    f.write(enc)
        except socket.timeout:
            pass
        sleep(1)
        a.send(b'run!')
        a.settimeout(None)
        print("process: {}:{}".format(str(b[0]),str(b[1])))
        sleep(0.5)
        # copy original file
        shutil.copyfile(folder+"\\\\"+".".join(file_ori), folder+"\\\\"+".".join(file_ori[:-1])+"_original.bat")
        a.send(b'a')
        rm_china(folder+"\\"+".".join(file_ori))
        for i in range(0,len(process_dec),1):
            a.send(b'a')
            file = folder+"\\"+".".join(file_ori[:-1])+"_"+str(process_dec[i])+"."+str(file_ori[-1])
            shutil.copyfile(folder+"\\\\"+".".join(file_ori), file)
            try:
                exec("""file = r"{}"\nif not ({}):int("khanhnguyen9872")""".format(str(file),str(run_process[i])))
            except:
                with open(file,'w',encoding='utf-8') as f:
                    f.write("@echo off\necho Cannot deobfuscate from {}\npause".format(str(process_dec[i])))
        with open(folder+"\\"+"readme.txt","w",encoding='utf-8') as f:
            f.write("Deobfuscate Batch Script by KhanhNguyen9872\nGithub: https://github.com/KhanhNguyen9872\nFB: https://fb.me/khanh10a1\n\nIf this tool cannot deobfuscate your batch script, please inbox my Facebook!\nI will improve this tool soon!\n\nThanks for used! <3\n")
        print("zip: {}:{}".format(str(b[0]),str(b[1])))
        shutil.make_archive(folder, 'zip', folder)
        a.send(b'o')
        print("send: {}:{}".format(str(b[0]),str(b[1])))
        with open(folder+".zip",'rb') as f:
            while 1:
                data = f.read(65535)
                if not data:
                    break
                a.send(data)
        sleep(1)
        a.close()
        print("Done! Close connection: {}:{}".format(str(b[0]),str(b[1])))
    except TimeoutError:
        print("Timeout: {}:{}".format(str(b[0]),str(b[1])))
    except ConnectionAbortedError:
        print("Aborted connection: {}:{}".format(str(b[0]),str(b[1])))
    except ConnectionResetError:
        print("Close connection: {}:{}".format(str(b[0]),str(b[1])))
    except ConnectionRefusedError:
        print("Connection refused: {}:{}".format(str(b[0]),str(b[1])))
    except UnicodeDecodeError:
        print("RequestError: {}:{}".format(str(b[0]),str(b[1])))
    except socket.timeout:
        pass
    try:
        shutil.rmtree(folder)
    except:
        pass
    try:
        remove(folder+".zip")
    except:
        pass
    return
def not_multi(a,b):
    global list_user
    count=0
    globals()[str(b)]=a
    globals()[str(b)+"i"]=b
    if str(b) not in list_user:
        list_user.append(str(b))
    while 1:
        if str(b) not in list_user:
            return
        elif list_user[0]==str(b):
            return
        else:
            if (count==0):
                count=1
                print("wait for turn: {}:{}".format(str(b[0]),str(b[1])))
            try:
                a.send("{}".format(str(int(list_user.index(str(b))))).encode())
            except:
                try:
                    a.close()
                except:
                    pass
                try:
                    del list_user[int(list_user.index(str(b)))]
                except:
                    pass
                try:
                    del globals()[str(b)]
                except:
                    pass
                try:
                    del globals()[str(b)+"i"]
                except:
                    pass
        sleep(1)
def process_not_multi():
    global list_user
    while 1:
        if list_user==[]:
            sleep(1)
            continue
        var=str(list_user[0])
        try:
            globals()[str(var)].send(b'now!')
            get_file(globals()[str(var)],globals()[str(var)+"i"])
        except:
            pass
        Thread(target=title_cmd, args=()).start()
        try:
            del list_user[int(list_user.index(str(var)))]
        except:
            pass
        try:
            del globals()[str(var)]
        except:
            pass
        try:
            del globals()[str(var)+"i"]
        except:
            pass
    return
def r_multi(a,b):
    global list_user
    if str(b) not in list_user:
        list_user.append(str(b))
    get_file(a,b)
    Thread(target=title_cmd, args=()).start()
    try:
        del list_user[int(list_user.index(str(b)))]
    except:
        pass
def send_full(a,var):
    try:
        a.send(var)
    except:
        pass
    try:
        a.close()
    except:
        pass
    return
def start_server():
    global list_user
    try:
        print("Listening on {}:{}....".format(str(host),str(port)))
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind((str(host), int(port)))
        soc.listen(25)
        if is_multi == 0:
            Thread(target=process_not_multi, args=()).start()
        var="f!{}".format(str(max_conn)).encode()
        print("Server started!")
        while 1:
            a,b = soc.accept()
            try:
                if len(list_user)>=int(max_conn):
                    Thread(target=send_full, args=(a,var)).start()
                    print("Full connection: {}:{}".format(str(b[0]),str(b[1])))
                    continue
                print("Accept: {}:{}".format(str(b[0]),str(b[1])))
                if is_multi == 1:
                    a.send(b'now!')
                    Thread(target=r_multi, args=(a,b)).start()
                else:
                    a.send(b'wait')
                    Thread(target=not_multi, args=(a,b)).start()
            except:
                a.close()
                continue
    except PermissionError:
        print(f"ERROR: Port {port} cannot be listen! Need administrator permission!!")
        return
    except OSError as e:
        print(f"ERROR: Port {port} | {e}")
        return
    except KeyboardInterrupt:
        exit()
#include
from subprocess import getoutput
import socket,shutil
from threading import Thread
from time import sleep
from os import system, name, getcwd, mkdir, remove, stat
from sys import exit
from pathlib import Path
from sys import stdout
from pathlib import Path
from config import *
global list_user
list_user=[]
#main
clear()
color()
title_cmd()
if (name!='nt'):
    print("!!! This program was made only for Windows !!!")
    exit()
start_server()
pause()