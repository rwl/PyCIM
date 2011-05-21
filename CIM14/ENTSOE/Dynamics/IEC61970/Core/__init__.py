# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.


from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreEquipment import CoreEquipment
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreIdentifiedObject import CoreIdentifiedObject
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CorePSRType import CorePSRType
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreBaseVoltage import CoreBaseVoltage
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreEquipmentContainer import CoreEquipmentContainer
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreTerminal import CoreTerminal
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CorePowerSystemResource import CorePowerSystemResource
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreOperatingShare import CoreOperatingShare
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreReportingGroup import CoreReportingGroup
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreConductingEquipment import CoreConductingEquipment
from CIM14.ENTSOE.Dynamics.IEC61970.Core.CorePsrList import CorePsrList

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#Core"
nsPrefix = "cimCore"


class CorePhaseCode(str):
    """Values are: ABC, splitSecondary2N, ABN, CN, ACN, BC, AN, BN, AB, splitSecondary1N, N, C, AC, ABCN, splitSecondary12N, A, B, BCN
    """
    pass
