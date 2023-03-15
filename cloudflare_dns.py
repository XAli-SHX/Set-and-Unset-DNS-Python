import subprocess

primary_dns = "1.1.1.1"
secondary_dns = "1.0.0.1"

subprocess.run(["python3", "core.py", primary_dns, secondary_dns])
