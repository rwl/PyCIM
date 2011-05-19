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

"""The IEC 61968 subpackages of the CIM are developed, standardized and maintained by IEC TC57 Working Group 14: interfaces for distribution management (WG14). Currently, normative parts of the model support the needs of information exchange defined in IEC 61968-9 and in IEC 61968-13.
"""

from CDPSM.Connectivity.Element import Element

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15?profile=http://iec.ch/TC57/2011/iec61968-13/CDPSM/Connectivity"
nsPrefix = "conn"

packageMap = {
    "Element": "CDPSM.Connectivity",
    "Fuse": "CDPSM.Connectivity.IEC61970.Wires",
    "EnergyConsumer": "CDPSM.Connectivity.IEC61970.Wires",
    "Switch": "CDPSM.Connectivity.IEC61970.Wires",
    "Disconnector": "CDPSM.Connectivity.IEC61970.Wires",
    "ACLineSegment": "CDPSM.Connectivity.IEC61970.Wires",
    "SynchronousMachine": "CDPSM.Connectivity.IEC61970.Wires",
    "BusbarSection": "CDPSM.Connectivity.IEC61970.Wires",
    "LoadBreakSwitch": "CDPSM.Connectivity.IEC61970.Wires",
    "TransformerTank": "CDPSM.Connectivity.IEC61970.Wires",
    "GroundDisconnector": "CDPSM.Connectivity.IEC61970.Wires",
    "PowerTransformerEnd": "CDPSM.Connectivity.IEC61970.Wires",
    "Junction": "CDPSM.Connectivity.IEC61970.Wires",
    "SeriesCompensator": "CDPSM.Connectivity.IEC61970.Wires",
    "Breaker": "CDPSM.Connectivity.IEC61970.Wires",
    "TransformerTankEnd": "CDPSM.Connectivity.IEC61970.Wires",
    "Sectionaliser": "CDPSM.Connectivity.IEC61970.Wires",
    "DCLineSegment": "CDPSM.Connectivity.IEC61970.Wires",
    "Line": "CDPSM.Connectivity.IEC61970.Wires",
    "Conductor": "CDPSM.Connectivity.IEC61970.Wires",
    "PowerTransformer": "CDPSM.Connectivity.IEC61970.Wires",
    "Ground": "CDPSM.Connectivity.IEC61970.Wires",
    "TransformerEnd": "CDPSM.Connectivity.IEC61970.Wires",
    "ShuntCompensator": "CDPSM.Connectivity.IEC61970.Wires",
    "EnergySource": "CDPSM.Connectivity.IEC61970.Wires",
    "Jumper": "CDPSM.Connectivity.IEC61970.Wires",
    "ShuntCompensatorPhase": "CDPSM.Connectivity.IEC61970.WiresPhaseModel",
    "SwitchPhase": "CDPSM.Connectivity.IEC61970.WiresPhaseModel",
    "Terminal": "CDPSM.Connectivity.IEC61970.Core",
    "Bay": "CDPSM.Connectivity.IEC61970.Core",
    "NameTypeAuthority": "CDPSM.Connectivity.IEC61970.Core",
    "VoltageLevel": "CDPSM.Connectivity.IEC61970.Core",
    "SubGeographicalRegion": "CDPSM.Connectivity.IEC61970.Core",
    "PSRType": "CDPSM.Connectivity.IEC61970.Core",
    "EquipmentContainer": "CDPSM.Connectivity.IEC61970.Core",
    "ConductingEquipment": "CDPSM.Connectivity.IEC61970.Core",
    "GeographicalRegion": "CDPSM.Connectivity.IEC61970.Core",
    "NameType": "CDPSM.Connectivity.IEC61970.Core",
    "Equipment": "CDPSM.Connectivity.IEC61970.Core",
    "IdentifiedObject": "CDPSM.Connectivity.IEC61970.Core",
    "ConnectivityNodeContainer": "CDPSM.Connectivity.IEC61970.Core",
    "Substation": "CDPSM.Connectivity.IEC61970.Core",
    "ConnectivityNode": "CDPSM.Connectivity.IEC61970.Core",
    "Name": "CDPSM.Connectivity.IEC61970.Core",
    "BaseVoltage": "CDPSM.Connectivity.IEC61970.Core",
    "PowerSystemResource": "CDPSM.Connectivity.IEC61970.Core",
}


class Length(float):
    """Unit of length.
    """
    pass

class Voltage(float):
    """Electrical voltage.
    """
    pass

class CIMTime(str):
    pass

class CIMDateTime(str):
    pass

class CIMDuration(str):
    pass

class CIMGYear(str):
    pass

class CIMDate(str):
    pass

class CIMGMonthDay(str):
    pass

class CIMGMonth(str):
    pass

class CIMGDay(str):
    pass

class CIMGYearMonth(str):
    pass
