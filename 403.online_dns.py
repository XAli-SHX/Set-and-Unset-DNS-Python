import core

primary_dns = "10.202.10.202"
secondary_dns = "10.202.10.102"

core.unset_dns()
core.set_dns(primary_dns, secondary_dns)
