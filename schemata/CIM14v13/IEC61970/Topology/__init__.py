# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

"""An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""

ns_prefix = "cimTopology"
ns_uri = "http://iec.ch/TC57/CIM-generic#Topology"

from CIM14v13.IEC61970.Topology.BusNameMarker import BusNameMarker
from CIM14v13.IEC61970.Topology.ConnectivityNode import ConnectivityNode
from CIM14v13.IEC61970.Topology.TopologicalNode import TopologicalNode
from CIM14v13.IEC61970.Topology.TopologicalIsland import TopologicalIsland
