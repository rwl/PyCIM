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

"""The OperationalLimits package models a specification of limits associated with equipment and other operational entities.
"""

nsPrefix = "cimOperationalLimits"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#OperationalLimits"

from CIM14.IEC61970.OperationalLimits.OperationalLimit import OperationalLimit
from CIM14.IEC61970.OperationalLimits.CurrentLimit import CurrentLimit
from CIM14.IEC61970.OperationalLimits.BranchGroup import BranchGroup
from CIM14.IEC61970.OperationalLimits.BranchGroupTerminal import BranchGroupTerminal
from CIM14.IEC61970.OperationalLimits.ApparentPowerLimit import ApparentPowerLimit
from CIM14.IEC61970.OperationalLimits.OperationalLimitSet import OperationalLimitSet
from CIM14.IEC61970.OperationalLimits.VoltageLimit import VoltageLimit
from CIM14.IEC61970.OperationalLimits.ActivePowerLimit import ActivePowerLimit
from CIM14.IEC61970.OperationalLimits.OperationalLimitType import OperationalLimitType

class OperationalLimitDirectionKind(str):
    """The direction of an operational limit.
    Values are: low, absoluteValue, high
    """
    pass
