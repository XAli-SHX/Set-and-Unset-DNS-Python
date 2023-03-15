import core

primary_dns = "1.1.1.1"
secondary_dns = "1.0.0.1"

core.unset_dns()
core.set_dns(primary_dns, secondary_dns)
