from ast import arguments
import imp
import subprocess
import optparse as opt

parse_object = opt.OptionParser()
parse_object.add_option("-i","interface",dest="interface",help="interface to change")
parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")

(user_inputs,arguments) = parse_object.parse_args()
print(user_inputs.interface)
print(user_inputs.mac_address)

interface = "eth0"
mac_address = "00:11:22:33:33:44"

print("My Mac Changer Started!")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw",mac_address])
subprocess.call(["ifconfig",interface,"up"])