import subprocess

print("My Mac Changer Started!")

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","00:11:22:33:33:44"])
subprocess.call(["ifconfig","eth0","up"])