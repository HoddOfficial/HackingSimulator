import time
from random import randint

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

#Making the Terminalines
failed = ['complete!', 'failed!']
yes = randint(0,len(failed)-1)
pos = 493485
prompt = bcolors.OKBLUE + 'root@user:' + bcolors.ENDC + ' '
start_time = time.time()
print prompt + 'ping (192.168.0.1)'
print prompt + 'ping (192.168.0.1) 56(84) bytes of data'
print prompt + '64 bytes ev.e-bnk.org (192.168.0.1): icmp_req=1 ttl=11'
print prompt + 'waiting for new data...'
time.sleep(1.5)
print prompt + 'recieved new data:'
print prompt + '1 packet(s) transmitted, 1 received, 0% packet loss, time 0.5'
print prompt + 'unpacking data...'
time.sleep(5)
print prompt + 'details to subject:'
print prompt + 'computer brand: Acer' 
print prompt + 'ip: 192.168.0.1'
time.sleep(2)
print prompt + 'hacking started...'
time.sleep(5)
print prompt + 'setting up proxy for anonymity...'
time.sleep(3)
print prompt + 'sending connection request to (192.168.0.1)...'
time.sleep(3)
print prompt + 'connection established'
time.sleep(2)
print prompt + 'try to crack users password...'
time.sleep(3)
print prompt + failed[yes]
time.sleep(4)
if failed[yes] == 'complete!':
        print prompt + 'try to log-in...'
        time.sleep(2)
        print prompt + 'log-in complete!'
        time.sleep(0.5)
        print prompt + 'detecting amount of data to copy...'
        time.sleep(0.5)
        print prompt + 'files to copy: 4934'
        print prompt + 'copiyng started...'
        for i in range(1, pos, 1):
                print prompt + 'copiyng files: ' + str(i) + ' bytes of ' + str(pos) + '\r',
        print '                                                                \r',
        print prompt + 'copiyng complete!'
        print prompt + 'Time elapsed: ' + str(time.time() - start_time)
        print prompt + 'Copied files: 4934'
        time.sleep(5)
        print prompt + 'preparing log-out...'
        time.sleep(1.5)
        print prompt + 'log-out comlete!'
        time.sleep(0.5)
        print prompt + 'hack successful!'
        print prompt + 'closing hackin program...'
        print prompt + 'complete!'

elif failed[yes] == 'failed!':
        print prompt + 'disconnecting...'
        time.sleep(1.5)
        print prompt + 'disconnected!'
        time.sleep(0.5)
        print prompt + 'disconnect to proxy...'
        time.sleep(1.5)
        print prompt + 'complete!'
        print prompt + 'closing hacking machine...'
#end
