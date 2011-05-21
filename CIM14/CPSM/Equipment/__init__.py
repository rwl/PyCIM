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

from CIM14.CPSM.Equipment.Element import Element
from CIM14.CPSM.Equipment.IEC61970CIMVersion import IEC61970CIMVersion

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile/CPSM/Equipment"
nsPrefix = "eq"

packageMap = {
    "Element": "CIM14.CPSM.Equipment",
    "IEC61970CIMVersion": "CIM14.CPSM.Equipment",
    "FossilFuel": "CIM14.CPSM.Equipment.Generation.Production",
    "HydroGeneratingUnit": "CIM14.CPSM.Equipment.Generation.Production",
    "GrossToNetActivePowerCurve": "CIM14.CPSM.Equipment.Generation.Production",
    "ThermalGeneratingUnit": "CIM14.CPSM.Equipment.Generation.Production",
    "HydroPump": "CIM14.CPSM.Equipment.Generation.Production",
    "WindGeneratingUnit": "CIM14.CPSM.Equipment.Generation.Production",
    "GeneratingUnit": "CIM14.CPSM.Equipment.Generation.Production",
    "NuclearGeneratingUnit": "CIM14.CPSM.Equipment.Generation.Production",
    "EquivalentShunt": "CIM14.CPSM.Equipment.Equivalents",
    "EquivalentBranch": "CIM14.CPSM.Equipment.Equivalents",
    "EquivalentInjection": "CIM14.CPSM.Equipment.Equivalents",
    "EquivalentEquipment": "CIM14.CPSM.Equipment.Equivalents",
    "EquivalentNetwork": "CIM14.CPSM.Equipment.Equivalents",
    "ApparentPowerLimit": "CIM14.CPSM.Equipment.OperationalLimits",
    "OperationalLimit": "CIM14.CPSM.Equipment.OperationalLimits",
    "CurrentLimit": "CIM14.CPSM.Equipment.OperationalLimits",
    "VoltageLimit": "CIM14.CPSM.Equipment.OperationalLimits",
    "ActivePowerLimit": "CIM14.CPSM.Equipment.OperationalLimits",
    "OperationalLimitSet": "CIM14.CPSM.Equipment.OperationalLimits",
    "OperationalLimitType": "CIM14.CPSM.Equipment.OperationalLimits",
    "EnergyArea": "CIM14.CPSM.Equipment.LoadModel",
    "Season": "CIM14.CPSM.Equipment.LoadModel",
    "SubLoadArea": "CIM14.CPSM.Equipment.LoadModel",
    "NonConformLoadSchedule": "CIM14.CPSM.Equipment.LoadModel",
    "LoadResponseCharacteristic": "CIM14.CPSM.Equipment.LoadModel",
    "ConformLoadSchedule": "CIM14.CPSM.Equipment.LoadModel",
    "NonConformLoadGroup": "CIM14.CPSM.Equipment.LoadModel",
    "ConformLoadGroup": "CIM14.CPSM.Equipment.LoadModel",
    "ConformLoad": "CIM14.CPSM.Equipment.LoadModel",
    "NonConformLoad": "CIM14.CPSM.Equipment.LoadModel",
    "StationSupply": "CIM14.CPSM.Equipment.LoadModel",
    "SeasonDayTypeSchedule": "CIM14.CPSM.Equipment.LoadModel",
    "LoadArea": "CIM14.CPSM.Equipment.LoadModel",
    "DayType": "CIM14.CPSM.Equipment.LoadModel",
    "LoadGroup": "CIM14.CPSM.Equipment.LoadModel",
    "ControlAreaGeneratingUnit": "CIM14.CPSM.Equipment.ControlArea",
    "TieFlow": "CIM14.CPSM.Equipment.ControlArea",
    "ControlArea": "CIM14.CPSM.Equipment.ControlArea",
    "AccumulatorValue": "CIM14.CPSM.Equipment.Meas",
    "Accumulator": "CIM14.CPSM.Equipment.Meas",
    "Discrete": "CIM14.CPSM.Equipment.Meas",
    "AnalogValue": "CIM14.CPSM.Equipment.Meas",
    "Analog": "CIM14.CPSM.Equipment.Meas",
    "MeasurementValueSource": "CIM14.CPSM.Equipment.Meas",
    "Measurement": "CIM14.CPSM.Equipment.Meas",
    "DiscreteValue": "CIM14.CPSM.Equipment.Meas",
    "MeasurementValue": "CIM14.CPSM.Equipment.Meas",
    "LoadBreakSwitch": "CIM14.CPSM.Equipment.Wires",
    "TransformerWinding": "CIM14.CPSM.Equipment.Wires",
    "SwitchSchedule": "CIM14.CPSM.Equipment.Wires",
    "PhaseVariationCurve": "CIM14.CPSM.Equipment.Wires",
    "RegulatingControl": "CIM14.CPSM.Equipment.Wires",
    "ACLineSegment": "CIM14.CPSM.Equipment.Wires",
    "PhaseTapChanger": "CIM14.CPSM.Equipment.Wires",
    "SeriesCompensator": "CIM14.CPSM.Equipment.Wires",
    "PowerTransformer": "CIM14.CPSM.Equipment.Wires",
    "EnergyConsumer": "CIM14.CPSM.Equipment.Wires",
    "Switch": "CIM14.CPSM.Equipment.Wires",
    "RegulationSchedule": "CIM14.CPSM.Equipment.Wires",
    "ShuntCompensator": "CIM14.CPSM.Equipment.Wires",
    "Conductor": "CIM14.CPSM.Equipment.Wires",
    "BusbarSection": "CIM14.CPSM.Equipment.Wires",
    "TapChanger": "CIM14.CPSM.Equipment.Wires",
    "ImpedanceVariationCurve": "CIM14.CPSM.Equipment.Wires",
    "ReactiveCapabilityCurve": "CIM14.CPSM.Equipment.Wires",
    "Disconnector": "CIM14.CPSM.Equipment.Wires",
    "RatioVariationCurve": "CIM14.CPSM.Equipment.Wires",
    "TapSchedule": "CIM14.CPSM.Equipment.Wires",
    "MutualCoupling": "CIM14.CPSM.Equipment.Wires",
    "SynchronousMachine": "CIM14.CPSM.Equipment.Wires",
    "RatioTapChanger": "CIM14.CPSM.Equipment.Wires",
    "RegulatingCondEq": "CIM14.CPSM.Equipment.Wires",
    "Line": "CIM14.CPSM.Equipment.Wires",
    "StaticVarCompensator": "CIM14.CPSM.Equipment.Wires",
    "Breaker": "CIM14.CPSM.Equipment.Wires",
    "ConnectivityNodeContainer": "CIM14.CPSM.Equipment.Core",
    "RegularIntervalSchedule": "CIM14.CPSM.Equipment.Core",
    "RegularTimePoint": "CIM14.CPSM.Equipment.Core",
    "Bay": "CIM14.CPSM.Equipment.Core",
    "Equipment": "CIM14.CPSM.Equipment.Core",
    "EquipmentContainer": "CIM14.CPSM.Equipment.Core",
    "IdentifiedObject": "CIM14.CPSM.Equipment.Core",
    "SubGeographicalRegion": "CIM14.CPSM.Equipment.Core",
    "PowerSystemResource": "CIM14.CPSM.Equipment.Core",
    "BasicIntervalSchedule": "CIM14.CPSM.Equipment.Core",
    "Curve": "CIM14.CPSM.Equipment.Core",
    "VoltageLevel": "CIM14.CPSM.Equipment.Core",
    "Unit": "CIM14.CPSM.Equipment.Core",
    "BaseVoltage": "CIM14.CPSM.Equipment.Core",
    "ConnectivityNode": "CIM14.CPSM.Equipment.Core",
    "Substation": "CIM14.CPSM.Equipment.Core",
    "ConductingEquipment": "CIM14.CPSM.Equipment.Core",
    "Terminal": "CIM14.CPSM.Equipment.Core",
    "GeographicalRegion": "CIM14.CPSM.Equipment.Core",
    "CurveData": "CIM14.CPSM.Equipment.Core",
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
