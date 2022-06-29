##import socket and os
import socket
import os

##function for running the port scan.
def init_socket(scanningaddress):
    ##timeout to override the wait time on a connection time out so its a little faster
    timeout = .5
    open = 0
    ##try except to catch errors
    try:
        ##well known ports so the scan is faster
        for port in range(0,1053):
            ##init socket connection
            sock = socket.socket()
            ##set timeout for socket connection for faster scanning
            sock.settimeout(timeout)
            ##sol tells pc to use connection before the natual wait time on a half open connection is terminated
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            ##connect to the specified address and port, return 0 or 1
            scan = sock.connect_ex((scanningaddress, port))
            ##if port is open return a statement saying it is open
            if scan == open:
                print("Port {}: is open".format(port))
                ##close the connetion
            sock.close()
    ##if user presses ctrl and c this will end the process
    except KeyboardInterrupt:
        print("Goodbye")
        get_ip()
    ##if user enters a hostname or ip that can not be resolved this error prints
    except socket.gaierror:
        print("Sorry, we cant find that IP or Hostname. Try again")
        get_ip()
    ##if IP or hostname denies access this error occurs
    except socket.error:
        print("Sorry we couldnt connect. Try again")
        get_ip()
##function to get the desiered address for scanning
def get_ip():
    ##get IP or servername
    address = input('Address you would like to scan: (i.e 10.10.10.10): ')
    ##resolve ip or servername by socket
    scanningaddress = socket.gethostbyname(address)
    ##print that proccess is running
    print("Scanning host........................")
    ##call scanning function
    init_socket(scanningaddress)

##call function
get_ip()


