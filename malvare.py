import platform
import getpass
import socket

user getpass.getuser()
computer = socket.gethostname()
ip = socket.gethostbyname(computer)
os = platform.system()

file = open("data.txt", "w")
file.write("User: "+ user+"\n")
file.write("user PC Name:" + computer"+\n")
file.write("IP : " + ip + "\n")
file.write("OS: " + os + "\n")
file.close()
