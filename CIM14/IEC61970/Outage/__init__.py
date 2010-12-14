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

"""An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
"""

nsPrefix = "cimOutage"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Outage"

from CIM14.IEC61970.Outage.ClearanceTag import ClearanceTag
from CIM14.IEC61970.Outage.ClearanceTagType import ClearanceTagType
from CIM14.IEC61970.Outage.OutageSchedule import OutageSchedule
from CIM14.IEC61970.Outage.SwitchingOperation import SwitchingOperation

class SwitchState(str):
    """Possible states for a switch.
    Values are: open, close
    """
    pass
