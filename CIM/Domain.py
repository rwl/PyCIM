#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------




from enthought.traits.api import Float, Enum
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------
PerCent = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatNormally 0 - 100 on a defined base")
Reactance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatReactance (imaginary part of impedance), at rated frequency.")
WaterLevel = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatReservoir water level referred to a given datum such as mean sea level.")
PU = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatPer Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.")
Voltage = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatElectrical voltage.")
AngleDegrees = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatMeasurement of angle in degrees")
Susceptance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatImaginary part of admittance.")
ApparentPower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of the RMS value of the voltage and the RMS value of the current")
ActivePower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the in-phase component of the current")
Damping = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatPer-unit active power variation with per-unit frequency referenced on the system apparent power base. Typical values in range 1.0 - 2.0.")
CurrentFlow = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatElectrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)")
Seconds = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatTime, in seconds")
LongLength = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatLong unit of length.")
Resistance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatResistance (real part of impedance).")
RealEnergy = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatReal electrical energy")
Conductance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatFactor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.")
ReactivePower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the quadrature component of the current.")
Volume = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatVolume.")
Money = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatAmount of money")
Impedance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatRatio of voltage to current.")
AngleRadians = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatPhase angle in radians")
Temperature = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatValue of temperature in degrees Celsius.")
ActivePowerChangeRate = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#float")
Hours = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatTime, in hours")
Frequency = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatCycles per second")
ShortLength = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatShort unit of length.")
VoltagePerReactivePower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatVoltage variation with reactive power")
Inductance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatInductance.")
CostPerEnergyUnit = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatCost, in units of currency, per quantity of electrical energy generated.")
CostRate = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatCost, in units of currency, per hour of elapsed time")
Admittance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatRatio of current to voltage.")
RotationSpeed = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatNumber of revolutions per second.")
Pressure = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatPressure in Pascal.")
KWActivePower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatActive power in kilowatts.")

# The unit multipliers defined for the CIM
UnitMultiplier = Enum("k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p", desc="The unit multipliers defined for the CIM")
# Monetary amount per joule.
MonetaryAmountPerHeatUnit = Enum("EUR_per_J", "USD_per_J", desc="Monetary amount per joule.")
# Monetary amount per second.
MonetaryAmountRate = Enum("EUR_per_s", "USD_per_s", desc="Monetary amount per second.")
# The units defiend for usage in the CIM
UnitSymbol = Enum("N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "degC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V", desc="The units defiend for usage in the CIM")
# Monetary currencies. Apologies for this list not being exhaustive.
Currency = Enum("CNY", "EUR", "INR", "AUD", "CHF", "DKK", "other", "RUR", "SEK", "GBP", "JPY", "NOK", "CAD", "USD", desc="Monetary currencies. Apologies for this list not being exhaustive.")
# Monetary amount per energy unit.
MonetaryAmountPerEnergyUnit = Enum("EUR_per_Wh", "USD_per_Wh", desc="Monetary amount per energy unit.")



# EOF -------------------------------------------------------------------------
