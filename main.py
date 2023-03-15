import platform
import subprocess
import sys


def set_dns(primary_ip, secondary_ip):
    system = platform.system()
    if system == "Windows":
        subprocess.run(["netsh", "interface", "ip", "set", "dns", "name=\"Wi-Fi\"", "static", primary_ip, "primary"])
        subprocess.run(
            ["netsh", "interface", "ip", "add", "dns", "name=\"Wi-Fi\"", "addr={}".format(secondary_ip), "index=2"])
    elif system == "Darwin":
        subprocess.run(["networksetup", "-setdnsservers", "Wi-Fi", primary_ip, secondary_ip])
    elif system == "Linux":
        subprocess.run(["nmcli", "connection", "modify", "Wi-Fi", "ipv4.dns", "{} {}".format(primary_ip, secondary_ip)])


def unset_dns():
    system = platform.system()
    if system == "Windows":
        subprocess.run(["netsh", "interface", "ip", "set", "dns", "name=\"Wi-Fi\"", "dhcp"])
    elif system == "Darwin":
        subprocess.run(["networksetup", "-setdnsservers", "Wi-Fi", "Empty"])
    elif system == "Linux":
        subprocess.run(["nmcli", "connection", "modify", "Wi-Fi", "ipv4.ignore-auto-dns", "yes"])


def main():
    args = sys.argv
    if len(args) == 1:
        unset_dns()
    elif args == 3:
        primary_dns = args[1]
        secondary_dns = args[2]
        set_dns(primary_dns, secondary_dns)
    else:
        print("Error: Not Enough Arguments")
        print("Usage -> `python3 core.py` to unset dns")
        print("Usage -> `python3 core.py <primary_dns> <secondary_dns>` to unset dns")


if __name__ == "__main__":
    main()
