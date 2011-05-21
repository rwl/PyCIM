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

from CIM14.ENTSOE.Dynamics.Element import Element
from CIM14.ENTSOE.Dynamics.Thing import Thing

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile/ENTSOE/Dynamics"
nsPrefix = "dyn"

packageMap = {
    "Element": "CIM14.ENTSOE.Dynamics",
    "Thing": "CIM14.ENTSOE.Dynamics",
    "AssetsAsset": "CIM14.ENTSOE.Dynamics.IEC61968.Assets",
    "CustomersCustomerAgreement": "CIM14.ENTSOE.Dynamics.IEC61968.Customers",
    "CommonLocation": "CIM14.ENTSOE.Dynamics.IEC61968.Common",
    "CoreEquipment": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CoreIdentifiedObject": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CorePSRType": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CoreBaseVoltage": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CoreEquipmentContainer": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CoreTerminal": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CorePowerSystemResource": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CoreOperatingShare": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CoreReportingGroup": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CoreConductingEquipment": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "CorePsrList": "CIM14.ENTSOE.Dynamics.IEC61970.Core",
    "ContingencyContingencyEquipment": "CIM14.ENTSOE.Dynamics.IEC61970.Contingency",
    "WiresSynchronousMachine": "CIM14.ENTSOE.Dynamics.IEC61970.Wires",
    "WiresRegulatingControl": "CIM14.ENTSOE.Dynamics.IEC61970.Wires",
    "WiresRegulatingCondEq": "CIM14.ENTSOE.Dynamics.IEC61970.Wires",
    "OutageOutageSchedule": "CIM14.ENTSOE.Dynamics.IEC61970.Outage",
    "OutageClearanceTag": "CIM14.ENTSOE.Dynamics.IEC61970.Outage",
    "OperationalLimitsOperationalLimitSet": "CIM14.ENTSOE.Dynamics.IEC61970.OperationalLimits",
    "InfCoreModelingAuthoritySet": "CIM14.ENTSOE.Dynamics.IEC61970.Informative.InfCore",
    "MeasMeasurement": "CIM14.ENTSOE.Dynamics.IEC61970.Meas",
    "MeasControl": "CIM14.ENTSOE.Dynamics.IEC61970.Meas",
    "StateVariablesSvStatus": "CIM14.ENTSOE.Dynamics.IEC61970.StateVariables",
    "ProtectionProtectionEquipment": "CIM14.ENTSOE.Dynamics.IEC61970.Protection",
    "DynamicsMetaBlockState": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockConSignal": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockReference": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockSignal": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsAttributeBlockParameter": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockConnection": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockConOutput": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockInput": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockOutputReference": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockStateReference": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsBlockConnection": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockConnectivity": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlock": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockConInput": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockParameter": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockConnectable": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockInputReference": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsRotatingMachine": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsBlockConnectivity": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockParameterReference": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsAsynchronousMachine": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsBlockParameter": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsBlock": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "DynamicsMetaBlockOutput": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics",
    "ExcitationSystemsExcDC4B": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcDC2A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcDC1A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcAC3A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcAC2A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcAC1A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcAC8B": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcST5B": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcAC7B": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcAC4A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcST4B": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcST6B": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcAC6A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcAC5A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcSCRX": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcSEXS": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcST7B": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcST2A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcST1A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcDC3A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "ExcitationSystemsExcST3A": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.ExcitationSystems",
    "GeneratorsGenEquiv": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.Generators",
    "TurbineGovernorsGovHydro2": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.TurbineGovernors",
    "TurbineGovernorsGovSteam0": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.TurbineGovernors",
    "TurbineGovernorsGovHydro1": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.TurbineGovernors",
    "TurbineGovernorsGovSteam1": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.TurbineGovernors",
    "TurbineGovernorsGovCT1": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.TurbineGovernors",
    "LoadsLoadStatic": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.Loads",
    "LoadsLoadMotor": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.Loads",
    "MotorsMechLoad1": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.Motors",
    "VoltageCompensatorVcompCross": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.VoltageCompensator",
    "VoltageCompensatorVcompIEEE": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.VoltageCompensator",
    "PowerSystemStabilizersPssIEEE2B": "CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.PowerSystemStabilizers",
}


class Frequency(float):
    pass

class ApparentPower(float):
    pass

class ActivePower(float):
    pass

class Seconds(float):
    pass

class Voltage(float):
    pass

class Resistance(float):
    pass

class Reactance(float):
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
