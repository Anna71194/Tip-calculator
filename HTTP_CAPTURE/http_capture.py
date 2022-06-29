##import scapy as scapy
import scapy.all as scapy
##import layer for calling
from scapy.layers.http import HTTPRequest

##function for sniffing argument is interface you want to sniff on
def cap(interface):
        ##sniff scapy to start sniffing, iface is interface passed, prn is proccessing packet and filter to filter out port 80 (HTTP traffic)
       scapy.sniff(iface = interface,prn = disp_packet, filter = 'port 80')

##called by sniff function, dispalys packets captured
def disp_packet(packets):
    ##for loop to iterate over each packet sniffed
    for packet in packets:
        ## if statement to pull out TCP port 80 packets, and show them to conole
        if packet and packet.haslayer(HTTPRequest):
            packet.show()
            ##print break to signify next packet
            print("---- END Packet ----")
        ##if not statment to signify no TCP packets have been captured
        if not packet and packet.haslayer(HTTPRequest):
        ##print error and try again
          print("NO HTTP RESPONSE")
          cap("Wi-Fi")

##call the capture function
cap('Wi-Fi')





