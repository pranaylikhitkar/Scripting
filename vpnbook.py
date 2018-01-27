"""
created_by = pranaylikhitkar
created_on = 1st October 2017
script_url = https://www.github.com/pranaylikhitkar/Scripting/blob/master/vpnbook.py
VPN Script-OpenVPN script for vpnbook.com
NOTE: This script is designed for Debian/Ubuntu Systems.
Before using this script make sure you have installed the following packages.
1. network-manager 
2. network-manager-gnome
3. network-manager-openvpn
4. network-manager-openvpn-gnome 
"""

from bs4 import BeautifulSoup
import urllib
import pexpect
import subprocess
import signal
import os
import time
import sys
import pexpect
import atexit

"""Constants"""
URL = "https://vpnbook.com/freevpn" #URL.
httpResponse = urllib.urlopen(URL) # HTTPResponse Code
soup = BeautifulSoup(httpResponse,"lxml")
username = "vpnbook"
PASS = sys.argv[1]

"""Functions"""
def connection():
    if httpResponse.code == 200:
        print "Connection Result : Passed."
    else:
        print "Error Code : " + str(httpResponse.code + ". Please check internet connection.")
    getconfig()

def getconfig():
    os.system("mkdir /home/$USER/openvpn")
    os.system("wget https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip -P /home/$USER/openvpn")
    os.system("unzip /home/$USER/openvpn/VPNBook.com-OpenVPN-US1.zip -d /home/$USER/openvpn")
    getpass()

def getpass():
    """Getting OpenVPN Certificates from the URL."""
    pop = soup.find(text="Password: ")
    pop1 = str(pop.next).replace("<strong>","").replace("</strong>","")
    print pop1
    openvpn(pop1)

def openvpn(passwd):
    """OpenVPN Session Begins"""
    session = pexpect.spawn("sudo openvpn --config /home/$USER/openvpn/vpnbook-us1-tcp80.ovpn")
    session.expect("password")
    time.sleep(2)
    session.send(PASS)
    print "Password Accepted."
    time.sleep(5)
    session.send(username + "\r")
    print "Username Sent"
    time.sleep(2)
    session.expect("[pP]assword")
    print "Expectation Reached"
    session.sendline(passwd+'\r')
    print "Password Accepted."
    print "VPN Login Successful"
    raw_input("Press Enter To Continue : ")
    fallback()

def fallback():
    os.system("rm -rvf /home/$USER/openvpn")
    p = subprocess.Popen(['ps','-A'], stdout=subprocess.PIPE)
    out,err = p.communicate()
    for line in out.splitlines():
        if 'openvpn' in line:
            pid = int(line.split(None,1)[0])
            os.kill(pid, signal.SIGKILL)
            if 'openvpn_cli' in line:
                pid = int(line.split(None,1)[0])
                os.kill(pid, signal.SIGKILL)
            print "Process OpenVPN Killed."
    print "Fallback procedure completed."
atexit.register(fallback)
connection()
