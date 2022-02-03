#!/usr/bin/env python
import subprocess
import optparse
import re

def get_args():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change mac address")
    parser.add_option("-m","--mac", dest="new_mac",help="new mac address")
    (options,argument)=parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Enter interface, for more info use --help :)")
    if not options.new_mac:
        parser.error("[-] Please Enter mac address, for more info use --help :)")
    return options

def change_mac(interface,new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac(interface):
    ifconfig_res=subprocess.check_output(["ifconfig", options.interface])
    mod_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_res)
    if mod_mac:
        return mod_mac.group(0)
    else:
        print("[-] Do not get MAC Address :(")
        print("[+] Try Again :)")
        exit()

options=get_args()
curr_mac=get_mac(options.interface)
print("Current MAC Address :) " + str(curr_mac))

change_mac(options.interface, options.new_mac)

mod_mac=get_mac(options.interface)
if mod_mac == options.new_mac:
    print("[+] MAC Address successfully changed to :) " + mod_mac)
else:
    print("[-] MAC Address did not get changed :(")
