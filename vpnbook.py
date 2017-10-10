"""
created_by = pranaylikhitkar
created_on = 1st October 2017
VPN Script-OpenVPN script for vpnbook.com
NOTE: This script is designed for Linux based system.
Before using this script make sure you have installed the following packets
1. network-manager 
2. network-manager-gnome
3. network-manager-openvpn
4. network-manager-openvpn-gnome 
"""

import urllib
import subprocess
import signal
import os
import time
import sys
import pexpect

""" Constants"""

URL = "https://vpnbook.com/freevpn"
httpResponse = urllib.urlopen(URL)

#Function connection looks for response.
U_PASS = sys.argv[1] #Password for your username.
VPN_PASS = sys.argv[2] #Password for vpnbook.
def connection():
    """Getting HTTP response to see for Internet Connection or Website availability"""
    if httpResponse.code == 200:
        print "Connection Test : PASSED."
        get_config()
    else:
        print "Status Code : " % (httpResponse.code)
def get_config():
    """Getting OpenVPN certificates from https://www.vpnbook.com"""
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip -P /home/slyrobot/Downloads")
    os.system("unzip /home/slyrobot/Downloads/VPNBook.com-OpenVPN-US1.zip -d Downloads")
    openvpn() #Call function openvpn()
def openvpn():
    """OpenVPN Sesssion begins"""
    session = pexpect.spawn('sudo openvpn --config /home/slyrobot/Downloads/vpnbook-us1-tcp80.ovpn')
    session.expect("password")
    time.sleep(2)
    session.send(U_PASS + "\r")
    print "OpenVPN Configuration Submitted"
    time.sleep(5)
    session.expect("Username")
    session.send("vpnbook" + "\r")
    time.sleep(5)
    session.expect("Password")
    session.send("pk7x1v3" + "\r")
    print "VPN Log In Successful"
    raw_input("Press Enter To Continue : ")
    process_end()
    sys.exit(0)
def process_end():
    """When the program ends / terminates it makes sure that it kills the openvpn"""
    os.system('rm /home/$USER/VPN*')
    os.system('rm /home/$USER/vpnbook*')
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    for line in out.splitlines():
        if 'openvpn' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)
    os.system()
def main():
    connection()

main()
