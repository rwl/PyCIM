# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.
"""



from enthought.traits.api import HasTraits, Str, Enum

AbsoluteDateTime = Str(desc="Date and time as 'yyyy-mm-ddThh:mm:ss.sss', which conforms with ISO 8601. UTC time zone is specified as 'yyyy-mm-ddThh:mm:ss.sssZ'. A local timezone relative UTC is specified as 'yyyy-mm-ddThh:mm:ss.sss-hh:mm'. AbsoluteDateTime can be used both for calender time, e.g. 2007-02-07T10:30, and for relative time, e.g. 10:30.")
ActivePower = Str(desc="Product of RMS value of the voltage and the RMS value of the in-phase component of the current")
ApparentPower = Str(desc="Product of the RMS value of the voltage and the RMS value of the current")
CurrentFlow = Str(desc="Current flow in Amps (positive flow is out of the ConductingEquipment into the ConnectivityNode) ")
AngleDegrees = Str(desc="Measurement of angle in degrees")
Frequency = Str(desc="Cycles per second")
Hours = Str(desc="Time, in hours")
Inductance = Str(desc="Inductance, in millihenries")
LongLength = Str(desc="Long unit of length (e.g. mile; kilometer)")
Money = Str(desc="Amount of money")
PerCent = Str(desc="Normally 0 - 100 on a defined base")
AngleRadians = Str(desc="Phase angle in radians")
Pressure = Str(desc="Pressure given in terms of pound-force per square inch")
PU = Str(desc="Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.")
Reactance = Str(desc="Reactance (imaginary part of impedance), in ohms, at rated frequency")
ReactivePower = Str(desc="Product of RMS value of the voltage and the RMS value of the quadrature component of the current (Megavoltamperes Reactive)")
Resistance = Str(desc="Resistance (real part of impedance), in ohms")
Seconds = Str(desc="Time, in seconds")
ShortLength = Str(desc="Short unit of length (e.g. foot; meter)")
Temperature = Str(desc="Value of temperature in TemperatureUnits")
Voltage = Str(desc="Value representing kV")
Volume = Str(desc="Reservoir water volume, given in millions of cubic meters")
WaterLevel = Str(desc="Reservoir water level referred to a given datum such as mean sea level, in meters")
Admittance = Str(desc="Ratio of current to voltage.")
Impedance = Str(desc="Ratio of voltage to current.")
Conductance = Str(desc="Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.")
Susceptance = Str(desc="Imaginary part of admittance.")
Float = Str(desc="A floating point number. The range is unspecified and not limited.")
Boolean = Str(desc="A type with the value space 'true' and 'false'.")
Integer = Str(desc="An integer number. The range is unspecified and not limited.")
String = Str(desc="A string consisting of a sequence of 8 bit characters. The character encoding is UTF-8. The string length is unspecified and unlimited.")
VoltagePerReactivePower = Str(desc="Voltage variation with reactive power")
RealEnergy = Str(desc="Real electrical energy")
KWActivePower = Str()
ActivePowerChangeRate = Str()
Damping = Str(desc="Per-unit megawatt variation with per-unit frequency referenced on the system MVA base. Typical values in range 1.0 - 2.0")
RotationSpeed = Str()
Minutes = Str(desc="Time in minutes")
AbsoluteDate = Str(desc="Date and time as 'yyyy-mm-dd', which conforms with ISO 8601. UTC time zone is specified as 'yyyy-mm-dd'.")

# The units defiend for usage in the CIM
UnitSymbol = Enum("VA", "W", "VAr", "VAh", "Wh", "VArh", "V", "ohm", "A", "F", "H", "_C", "s", "min", "deg", "rad", "J", "N", "none", "Hz", "kg", "Pa", "m", "m2", "m3", "VVAr", "WHz", "Js", "s1", "kgJ", "Ws", desc="The units defiend for usage in the CIM")
# The unit multipliers defined for the CIM
UnitMultiplier = Enum("p", "n", "micro", "m", "c", "d", "k", "G", "T", "none", desc="The unit multipliers defined for the CIM")
# Monetary currencies. Apologies for this list not being exhaustive.
Currency = Enum("USD", "EUR", "AUD", "CAD", "CHF", "CNY", "DKK", "GBP", "JPY", "NOK", "RUR", "SEK", "INR", desc="Monetary currencies. Apologies for this list not being exhaustive.")
# Monetary amount per watt hour
MonetaryAmountPerEnergyUnit = Enum("USD_per_Wh", "EUR_per_Wh", desc="Monetary amount per watt hour")
# Moneraty amount per joule
MonetaryAmountPerHeatUnit = Enum("USD_per_J", "EUR_per_J", desc="Moneraty amount per joule")

MonetaryAmountRate = Enum("USD_per_s", "EUR_per_s")

class DomainVersion(HasTraits):
    version = String
    date = AbsoluteDateTime


