import platform
import subprocess


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
