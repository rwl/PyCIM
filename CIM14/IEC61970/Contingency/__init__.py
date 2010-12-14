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

"""Contingencies to be studied.
"""

nsPrefix = "cimContingency"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Contingency"

from CIM14.IEC61970.Contingency.ContingencyElement import ContingencyElement
from CIM14.IEC61970.Contingency.ContingencyEquipment import ContingencyEquipment
from CIM14.IEC61970.Contingency.Contingency import Contingency

class ContingencyEquipmentStatusKind(str):
    """Indicates the state which the contingency equipment is to be in when the contingency is applied.
    Values are: outOfService, inService
    """
    pass
