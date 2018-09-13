# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
numNodes = 4

link = request.LAN("lan")

for i in range(numNodes):
    node = request.XenVM("node-" + str(i + 1))
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
    iface = node.addInterface("if" + str(i + 1))
    iface.component_id = "eth1"
    iface.addAddress(pg.IPv4Address("192.168.1." + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    if i == 0:
        node.routable_control_ip = True

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
