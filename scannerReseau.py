import socket
import os
import re
import subprocess
import sys

print('[+] Choice :')
print('1- Scan Network')
print('2- Scan port of ip adress')

hosts=[]
choice=int(input())
ip = '192.0.43.'
x=0
if choice==1:
    while x<=30:
        p=subprocess.Popen('ping '+ip+str(x)+" -t 2",stdout=subprocess.PIPE,shell=True)
        print(p)
        out, ERROR = p.communicate()
        out=str(out)
        print(out)
        find=re.search('Destination host unreachable',out)
        if find is None:
            hosts.append(ip+str(x))
            print("[+] Host found")
        x = x+1
print('+-----------------------+')
print('l            Host        ')
print('+-----------------------+')
for host in hosts:
    try:
        name,a,b=socket.gethostbyaddr(host)
        
    except:
        name="Not Found"
    print('l '+host+'l'+name+"l")


if choice==2:
    Ip = input('Ip à scanner : ')
    print("Scan de l'ip : "+Ip+" en cours ...")
    try:
        for port in range(1,1025):
            print(port)
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print(sock)
            result= sock.connect_ex((Ip,port))
            print(result)
            if result == 0:
                print('[+] Port n°'+str(port)+' Ouvert')
            else:
                print('[-] Port n°'+str(port)+' fermé')
            sock.close()
    except socket.gaierror:
        print('[-] serveur non joignable')
        sys.exit()
    except socket.error:
        print('[-] serveur non joignable')
        sys.exit()

    print('Scan finis !')
    

