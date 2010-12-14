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


nsPrefix = "cimPowerSystemStabilizers"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#PowerSystemStabilizers"

from CIM14.Dynamics.PowerSystemStabilizers.PowerSystemStabilizer import PowerSystemStabilizer
from CIM14.Dynamics.PowerSystemStabilizers.PssIEEE3B import PssIEEE3B
from CIM14.Dynamics.PowerSystemStabilizers.PssSK import PssSK
from CIM14.Dynamics.PowerSystemStabilizers.PssIEEE4B import PssIEEE4B
from CIM14.Dynamics.PowerSystemStabilizers.PssIEEE1A import PssIEEE1A
from CIM14.Dynamics.PowerSystemStabilizers.PssPTIST1 import PssPTIST1
from CIM14.Dynamics.PowerSystemStabilizers.PssIEEE2B import PssIEEE2B
from CIM14.Dynamics.PowerSystemStabilizers.PssSB import PssSB
from CIM14.Dynamics.PowerSystemStabilizers.PssSB4 import PssSB4
from CIM14.Dynamics.PowerSystemStabilizers.PssSH import PssSH
from CIM14.Dynamics.PowerSystemStabilizers.PssPTIST3 import PssPTIST3
from CIM14.Dynamics.PowerSystemStabilizers.PssWSCC import PssWSCC

class InputSignalCodeJ(str):
    """Values are: 2, 4, 3, 5, 1, 6
    """
    pass
