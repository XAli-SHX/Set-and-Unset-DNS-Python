import core

primary_dns = "8.8.8.8"
secondary_dns = "8.8.4.4"

core.unset_dns()
core.set_dns(primary_dns, secondary_dns)
