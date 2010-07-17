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




from enthought.traits.api import Float, Str, Int, Enum
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------
AngleDegrees = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatMeasurement of angle in degrees")
Reactance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatReactance (imaginary part of impedance), at rated frequency.")
ActivePower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the in-phase component of the current")
Resistance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatResistance (real part of impedance).")
CostPerEnergyUnit = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatCost, in units of currency, per quantity of electrical energy generated.")
AbsoluteDate = Str(desc="http://www.w3.org/2001/XMLSchema#stringDate and time as 'yyyy-mm-dd', which conforms with ISO 8601. UTC time zone is specified as 'yyyy-mm-dd'.")
PU = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatPer Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.")
Frequency = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatCycles per second")
Seconds = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatTime, in seconds")
Money = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatAmount of money")
Capacitance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatA Farad, the typical unit, is the capacitance in which a charge of 1 coulomb produces 1 volt potential difference between its terminals.")
PerCent = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatNormally 0 - 100 on a defined base")
CurrentFlow = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatElectrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)")
Length = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatUnit of length.")
KWActivePower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatActive power in kilowatts.")
Hours = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatTime, in hours")
CostRate = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatCost, in units of currency, per hour of elapsed time")
Voltage = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatElectrical voltage.")
Susceptance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatImaginary part of admittance.")
ApparentPower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of the RMS value of the voltage and the RMS value of the current")
Temperature = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatValue of temperature in degrees Celsius.")
StringQuantity = Str(desc="http://www.w3.org/2001/XMLSchema#stringQuantity with string value (when it is not important whether it is an integral or a floating point number) and associated unit information.")
RotationSpeed = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatNumber of revolutions per second.")
RealEnergy = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatReal electrical energy")
IntegerQuantity = Int(0, desc="http://www.w3.org/2001/XMLSchema#integerQuantity with integer value and associated unit information.")
Conductance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatFactor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.")
Minutes = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatTime in minutes")
Weight = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatThe weight of an object.")
Pressure = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatPressure in Pascal.")
ActivePowerChangeRate = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#float")
Inductance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatInductance.")
Damping = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatPer-unit active power variation with per-unit frequency referenced on the system apparent power base. Typical values in range 1.0 - 2.0.")
ReactivePower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the quadrature component of the current.")
FloatQuantity = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatQuantity with float value and associated unit information.")
Volume = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatVolume.")
AngleRadians = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatPhase angle in radians")
VoltagePerReactivePower = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatVoltage variation with reactive power")
Impedance = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatRatio of voltage to current.")
WaterLevel = Float(0.0, desc="http://www.w3.org/2001/XMLSchema#floatReservoir water level referred to a given datum such as mean sea level.")

# The unit multipliers defined for the CIM
UnitMultiplier = Enum("m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none", desc="The unit multipliers defined for the CIM")
# The units defiend for usage in the CIM
UnitSymbol = Enum("m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "degC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh", desc="The units defiend for usage in the CIM")
# Monetary amount per energy unit.
MonetaryAmountPerEnergyUnit = Enum("USD_per_Wh", "EUR_per_Wh", desc="Monetary amount per energy unit.")
# Monetary amount per second.
MonetaryAmountRate = Enum("EUR_per_s", "USD_per_s", desc="Monetary amount per second.")
# Monetary amount per joule.
MonetaryAmountPerHeatUnit = Enum("EUR_per_J", "USD_per_J", desc="Monetary amount per joule.")
# Monetary currencies. Apologies for this list not being exhaustive.
Currency = Enum("EUR", "other", "JPY", "DKK", "NOK", "CNY", "USD", "INR", "SEK", "AUD", "CHF", "CAD", "RUR", "GBP", desc="Monetary currencies. Apologies for this list not being exhaustive.")



# EOF -------------------------------------------------------------------------
