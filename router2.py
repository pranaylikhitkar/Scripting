import pexpect
import time,sys


telconn = pexpect.spawn('telnet 192.168.0.1')
password = raw_input("Enter your Password : ")
time.sleep(5)
telconn.logfile = sys.stdout
telconn.expect(":")
time.sleep(5)
telconn.send("Admin" + "\r")
telconn.expect(":")
time.sleep(5)
telconn.send(password + "\r")
print "Logged In Successfully"
time.sleep(3)
telconn.expect ("AP#")
#Below change restart to make your automated function.
telconn.send("restart"+ "\r")
