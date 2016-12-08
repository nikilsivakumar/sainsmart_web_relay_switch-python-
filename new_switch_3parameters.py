#!/usr/bin/python

import sys
import urllib2
import urllib
import requests
import sys
import socket 

#ON = 1
#OFF =2

ValidParamCount = 4


def Usage():
    print 'Usage : switch.py <IpAddress> <switch num> <OFF/ON>'

def functionName(x):
#    print 'function -', x
    return 0

    
def ipaddress(x):
#checks for a valid IP
    global ip_addr
    ret=0

    try:
        socket.inet_pton(socket.AF_INET, x)
        ip_addr=x
    except socket.error:
        print  'IpAddress -', x,', Invalid IpAddress'
        ret=1
 
    return ret

def switch(x):
#checks for a valid switch num
    global sw_num
    ret=0
    
    try:
        sw_num=int(x)
    except ValueError:
        print 'switch# ', x, ', Not a Valid Number'
        ret=1

    return ret
	
def ip():
#convert the arguments and send to URL
	ON = 1
	OFF = 2
	
	ip_addr = str(sys.argv[1])
	sw_num = int(sys.argv[2])
	sw_state =str(sys.argv[3])

	print("The script name :%s" % str(sys.argv[0]))
	print("the port is",sw_num)

	if (sw_state == 'OFF'): 
		state = ((sw_num*2) - OFF)
		print int(state)
	elif (sw_state == 'ON'): 
		state = ((sw_num*2) -ON)
		print int(state)	
	else:	
		print "Error"
       
	#port value is hardcoded

	request = urllib.urlopen("http://%s/%s/%02d" % (ip_addr,30000,state))
	print request.url

#request = urllib2.Request("http://%s/%s" % (port,state))


def state(x):
#checks for a valid state of switch
    global sw_state
    ret=0
    
    if not ((x.upper() == 'ON') or (x.upper() == 'OFF')):
        print 'state -', x, 'Unknown state'
        ret=1
    else:
        sw_state=x.upper()

    return ret
    

def default(x):
    print 'unknown parameter -', x
    return 1


validate_params = { 0 : functionName,
                    1 : ipaddress,
                    2 : switch,
                    3 : state,
                    4 : default
            }

if __name__ == '__main__':
    count=0
    error=0
    global ip_addr,port,sw_num,sw_state

    if(len(sys.argv) < ValidParamCount):
        Usage()
        exit(1)
        
    for i in sys.argv:
        error = error or validate_params[count if (count < ValidParamCount) else ValidParamCount](i)
        count+=1

    if(error):
        Usage()
        exit(1)

ip()


