#!/bin/python3
from sys import exit,stdout
if __name__!='__main__':
    exit()
import socket,mimetypes,signal
from pathlib import Path
from time import sleep
from threading import Thread
from os import stat, kill, getpid, getcwd, path
from base64 import b64decode
global is_timeout,is_exit,count,pid
pid = getpid()
is_timeout = 0
is_exit = 0
max_time = 300
count = max_time
iserror = 0
def kill_process():
    if hasattr(signal, 'SIGKILL'):
        kill(pid, signal.SIGKILL)
    else:
        kill(pid, signal.SIGABRT)
    exit()
def timeout_process(max_time,soc):
    global is_timeout,is_exit,count
    while 1:
        sleep(1)
        count -= 1
        if (count<0):
            timeout_a(soc)
            return
        elif (is_exit==1):
            return
    is_timeout=1
def pause():
    try:
        input('Press Enter to Exit! ')
    except KeyboardInterrupt:
        kill_process()
    return
def timeout_a(soc):
    global is_exit
    try:
        soc.close()
    except:
        pass
    is_exit=1
    print('server not response on {} seconds!'.format(max_time))
    pause()
    kill_process()
def out_of(length,soc):
    global is_exit
    try:
        size = soc.recv(1024).decode()
        soc.close()
    except:
        pass
    is_exit=1
    print('server response this file too large! (file: {} byte) [max: {} byte]! please try another file!'.format(length,size))
    pause()
    kill_process()
def unknown(soc):
    soc.close()
    print("server return unknown data! try again later!")
    pause()
    kill_process()
try:
    file = path.abspath(str(input('PATH Batch File: ').replace("\"","")))
    my_file = Path(file)
    if my_file.is_file():
        file_name = file.replace("\\","/").split("/")[-1]
        folder = file.replace("\\","/").split("/")
        del folder[folder.index(file_name)],my_file
        folder = "/".join(folder)+"/"
        print("folder: {}".format(folder))
        print("file name: {}".format(file_name))
    else:
        print('!!! File not exist !!!')
        pause()
        kill_process()
    with open(file,'rb') as f:
        data = f.read(1)
    if data:
        if b'\x00' in open(file, 'rb').read(33554432):
            print("please choose a batch file, not binary file!")
            pause()
            kill_process()
        try:
            size_file = int(stat(file).st_size)
            print('connecting....')
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __=b'=0EVRJDTqV'
            __+=b'UNNNEN41E'
            __+=b'RRVXTqFFN'
            #soc.connect((b64decode(b64decode(__[::-1])[::-1]),12345))
            del __
            soc.connect(('127.0.0.1',12345))
            soc.settimeout(None)
            while 1:
                try:
                    string = str(soc.recv(10).decode())
                    if string=='now!':
                        break
                    elif string=='wait':
                        is_wait = 0
                        while 1:
                            turn = soc.recv(256).decode()
                            try:
                                ___=int(turn)
                                is_wait = 1
                                print('                                                 ',end='\r')
                                print('waiting to your turn.... ({} left)'.format(turn),end='\r')
                                stdout.flush()
                            except ValueError:
                                if str(turn)=='now!':
                                    if is_wait == 1:
                                        print('                                                 ',end='\r')
                                    break
                                else:
                                    continue
                        break
                    elif string.split("!")[0]=="f" and int(string.split("!")[1])>0:
                        soc.close()
                        print("server response connection is full [max: {} conn]! try again later!".format(string.split("!")[1]))
                        pause()
                        kill_process()
                    else:
                        unknown(soc)
                except ValueError:
                    continue
            Thread(target=timeout_process, args=(max_time,soc)).start()
            soc.send(b'len!')
            if str(soc.recv(5).decode())=="slen!":
                print("send file size....")
            else:
                unknown(soc)
            # send length data
            soc.send(str(size_file).encode())
            count = max_time
            string = str(soc.recv(4).decode())
            if string=='get!':
                print("send file....")
                with open(file,'rb') as f:
                    while 1:
                        count = max_time
                        data = f.read(65535)
                        if not data:
                            break
                        soc.send(data)
            elif string=='out!':
                out_of(size_file,soc)
            else:
                unknown(soc)
            # send data
            string = str(soc.recv(4).decode())
            count = max_time
            if string=='run!':
                print('process....')
            elif string=='out!':
                out_of(size_file,soc)
            else:
                unknown(soc)
            # receive file
            while 1:
                string = str(soc.recv(1).decode())
                count = max_time
                if string=='o':
                    print('receive file....')
                    break
                elif string=='a':
                    continue
                else:
                    unknown(soc)
            with open(file.split(".")[0]+'.zip','wb') as f:
                try:
                    string = " "
                    while string:
                        string = soc.recv(65535)
                        f.write(string)
                        count = max_time
                except:
                    pass
            is_exit=1
            print('Done!')
            pause()
        except PermissionError:
            try:
                soc.close()
            except:
                pass
            print("cannot write file! the file [{0}] from [{1}] is locked! please close the application that is using this file or grant permission to access this file!".format(file_name.split(".")[0]+".zip",folder))
            pause()
            kill_process()
        except OSError:
            iserror=1
            print('                                                 ',end='\r')
            print("Close connection!")
            try:
                soc.close()
            except:
                pass
            pause()
            kill_process()
        except TimeoutError:
            iserror=1
            timeout_a(soc)
        except socket.timeout:
            iserror=1
            timeout_a(soc)
    else:
        iserror=1
        print('file empty!')
        pause()
except UnicodeDecodeError:
    iserror=1
    unknown(soc)
except KeyboardInterrupt:
    try:
        soc.close()
    except:
        pass
    if iserror == 0:
        pause()
    kill_process()