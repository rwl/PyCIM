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

"""
"""

from CIM14.ENTSOE.Equipment.Element import Element
from CIM14.ENTSOE.Equipment.OperationalLimit import OperationalLimit
from CIM14.ENTSOE.Equipment.IEC61970CIMVersion import IEC61970CIMVersion

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile/ENTSOE/Equipment"
nsPrefix = "eq"

packageMap = {
    "Element": "CIM14.ENTSOE.Equipment",
    "OperationalLimit": "CIM14.ENTSOE.Equipment",
    "IEC61970CIMVersion": "CIM14.ENTSOE.Equipment",
    "ControlArea": "CIM14.ENTSOE.Equipment.ControlArea",
    "ControlAreaGeneratingUnit": "CIM14.ENTSOE.Equipment.ControlArea",
    "TieFlow": "CIM14.ENTSOE.Equipment.ControlArea",
    "BusbarSection": "CIM14.ENTSOE.Equipment.Wires",
    "LoadBreakSwitch": "CIM14.ENTSOE.Equipment.Wires",
    "TapChanger": "CIM14.ENTSOE.Equipment.Wires",
    "TransformerWinding": "CIM14.ENTSOE.Equipment.Wires",
    "RegulatingControl": "CIM14.ENTSOE.Equipment.Wires",
    "ReactiveCapabilityCurve": "CIM14.ENTSOE.Equipment.Wires",
    "ACLineSegment": "CIM14.ENTSOE.Equipment.Wires",
    "Disconnector": "CIM14.ENTSOE.Equipment.Wires",
    "PhaseTapChanger": "CIM14.ENTSOE.Equipment.Wires",
    "SeriesCompensator": "CIM14.ENTSOE.Equipment.Wires",
    "MutualCoupling": "CIM14.ENTSOE.Equipment.Wires",
    "SynchronousMachine": "CIM14.ENTSOE.Equipment.Wires",
    "RatioTapChanger": "CIM14.ENTSOE.Equipment.Wires",
    "PowerTransformer": "CIM14.ENTSOE.Equipment.Wires",
    "EnergyConsumer": "CIM14.ENTSOE.Equipment.Wires",
    "Switch": "CIM14.ENTSOE.Equipment.Wires",
    "RegulatingCondEq": "CIM14.ENTSOE.Equipment.Wires",
    "Line": "CIM14.ENTSOE.Equipment.Wires",
    "StaticVarCompensator": "CIM14.ENTSOE.Equipment.Wires",
    "ShuntCompensator": "CIM14.ENTSOE.Equipment.Wires",
    "Breaker": "CIM14.ENTSOE.Equipment.Wires",
    "Conductor": "CIM14.ENTSOE.Equipment.Wires",
    "Measurement": "CIM14.ENTSOE.Equipment.Meas",
    "MeasurementValueSource": "CIM14.ENTSOE.Equipment.Meas",
    "MeasurementValue": "CIM14.ENTSOE.Equipment.Meas",
    "Curve": "CIM14.ENTSOE.Equipment.Core",
    "ConnectivityNodeContainer": "CIM14.ENTSOE.Equipment.Core",
    "RegularIntervalSchedule": "CIM14.ENTSOE.Equipment.Core",
    "VoltageLevel": "CIM14.ENTSOE.Equipment.Core",
    "Unit": "CIM14.ENTSOE.Equipment.Core",
    "Equipment": "CIM14.ENTSOE.Equipment.Core",
    "BaseVoltage": "CIM14.ENTSOE.Equipment.Core",
    "ConnectivityNode": "CIM14.ENTSOE.Equipment.Core",
    "EquipmentContainer": "CIM14.ENTSOE.Equipment.Core",
    "IdentifiedObject": "CIM14.ENTSOE.Equipment.Core",
    "Substation": "CIM14.ENTSOE.Equipment.Core",
    "ConductingEquipment": "CIM14.ENTSOE.Equipment.Core",
    "SubGeographicalRegion": "CIM14.ENTSOE.Equipment.Core",
    "Terminal": "CIM14.ENTSOE.Equipment.Core",
    "GeographicalRegion": "CIM14.ENTSOE.Equipment.Core",
    "PowerSystemResource": "CIM14.ENTSOE.Equipment.Core",
    "CurveData": "CIM14.ENTSOE.Equipment.Core",
    "BasicIntervalSchedule": "CIM14.ENTSOE.Equipment.Core",
    "VoltageLimit": "CIM14.ENTSOE.Equipment.OperationalLimits",
    "CurrentLimit": "CIM14.ENTSOE.Equipment.OperationalLimits",
    "OperationalLimit": "CIM14.ENTSOE.Equipment.OperationalLimits",
    "OperationalLimitSet": "CIM14.ENTSOE.Equipment.OperationalLimits",
    "OperationalLimitType": "CIM14.ENTSOE.Equipment.OperationalLimits",
    "EquivalentEquipment": "CIM14.ENTSOE.Equipment.Equivalents",
    "EquivalentNetwork": "CIM14.ENTSOE.Equipment.Equivalents",
    "WindGeneratingUnit": "CIM14.ENTSOE.Equipment.Generation.Production",
    "GeneratingUnit": "CIM14.ENTSOE.Equipment.Generation.Production",
    "FossilFuel": "CIM14.ENTSOE.Equipment.Generation.Production",
    "NuclearGeneratingUnit": "CIM14.ENTSOE.Equipment.Generation.Production",
    "HydroGeneratingUnit": "CIM14.ENTSOE.Equipment.Generation.Production",
    "ThermalGeneratingUnit": "CIM14.ENTSOE.Equipment.Generation.Production",
    "HydroPump": "CIM14.ENTSOE.Equipment.Generation.Production",
    "NonConformLoad": "CIM14.ENTSOE.Equipment.LoadModel",
    "EnergyArea": "CIM14.ENTSOE.Equipment.LoadModel",
    "Season": "CIM14.ENTSOE.Equipment.LoadModel",
    "SubLoadArea": "CIM14.ENTSOE.Equipment.LoadModel",
    "LoadResponseCharacteristic": "CIM14.ENTSOE.Equipment.LoadModel",
    "NonConformLoadGroup": "CIM14.ENTSOE.Equipment.LoadModel",
    "SeasonDayTypeSchedule": "CIM14.ENTSOE.Equipment.LoadModel",
    "ConformLoadGroup": "CIM14.ENTSOE.Equipment.LoadModel",
    "DayType": "CIM14.ENTSOE.Equipment.LoadModel",
    "LoadGroup": "CIM14.ENTSOE.Equipment.LoadModel",
    "ConformLoad": "CIM14.ENTSOE.Equipment.LoadModel",
}


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
