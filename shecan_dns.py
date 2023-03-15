import subprocess

primary_dns = "178.22.122.100"
secondary_dns = "185.51.200.2"

subprocess.run(["python3", "core.py", primary_dns, secondary_dns])
