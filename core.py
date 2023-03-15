import platform
import subprocess
import sys
import pyuac


def set_dns(primary_ip, secondary_ip):
    system = platform.system()
    if system == "Windows":
        if not pyuac.isUserAdmin():
            print("Re-launching as admin!")
            pyuac.runAsAdmin()
            return
        subprocess.run(
            ["netsh", "interface", "ipv4", "add", "dnsserver", "\"Wi-Fi\"", "address={}".format(primary_ip), "index=1"])
        subprocess.run(
            ["netsh", "interface", "ipv4", "add", "dnsserver", "\"Wi-Fi\"", "address={}".format(secondary_ip),
             "index=2"])
    elif system == "Darwin":
        subprocess.run(["networksetup", "-setdnsservers", "Wi-Fi", primary_ip, secondary_ip])
    elif system == "Linux":
        subprocess.run(["nmcli", "connection", "modify", "Wi-Fi", "ipv4.dns", "{} {}".format(primary_ip, secondary_ip)])


def unset_dns():
    system = platform.system()
    if system == "Windows":
        if not pyuac.isUserAdmin():
            print("Re-launching as admin!")
            pyuac.runAsAdmin()
            return
        subprocess.run(["netsh", "interface", "ip", "set", "dns", "name=\"Wi-Fi\"", "dhcp"])
    elif system == "Darwin":
        subprocess.run(["networksetup", "-setdnsservers", "Wi-Fi", "Empty"])
    elif system == "Linux":
        subprocess.run(["nmcli", "connection", "modify", "Wi-Fi", "ipv4.ignore-auto-dns", "yes"])


def main():
    args = sys.argv
    if len(args) == 1:
        unset_dns()
    elif len(args) == 3:
        primary_dns = args[1]
        secondary_dns = args[2]
        set_dns(primary_dns, secondary_dns)
    else:
        print(f"Error: Not Enough Arguments ({len(args)})")
        print("Usage -> `python3 core.py` to unset dns")
        print("Usage -> `python3 core.py <primary_dns> <secondary_dns>` to set dns")


if __name__ == "__main__":
    main()
