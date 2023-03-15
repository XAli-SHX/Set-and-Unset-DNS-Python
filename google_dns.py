import subprocess

primary_dns = "8.8.8.8"
secondary_dns = "8.8.4.4"

subprocess.run(["python3", "core.py", primary_dns, secondary_dns])
