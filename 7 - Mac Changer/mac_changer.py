import imp
import subprocess
import optparse as opt

parse_object = opt.OptionParser()
parse_object.add_option("--i","interface",dest="interface",help="interface to change")


interface = "eth0"
mac_add = "00:11:22:33:33:44"

print("My Mac Changer Started!")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw",mac_add])
subprocess.call(["ifconfig",interface,"up"])