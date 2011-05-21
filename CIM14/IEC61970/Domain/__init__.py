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

"""The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.
"""


nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Domain"
nsPrefix = "cimDomain"


class UnitMultiplier(str):
    """The unit multipliers defined for the CIM
    Values are: k, d, n, M, none, G, micro, T, c, m, p
    """
    pass

class MonetaryAmountPerHeatUnit(str):
    """Monetary amount per joule.
    Values are: USD_per_J, EUR_per_J
    """
    pass

class MonetaryAmountRate(str):
    """Monetary amount per second.
    Values are: USD_per_s, EUR_per_s
    """
    pass

class UnitSymbol(str):
    """The units defiend for usage in the CIM
    Values are: N, VArh, VA, none, m3, kg/J, deg, W/Hz, g, Wh, W/s, Pa, V/VAr, ohm, h, F, H, m2, VAr, A, rad, s, S, VAh, Hz, oC, s-1, min, J, Hz-1, J/s, m, W, V
    """
    pass

class Currency(str):
    """Monetary currencies. Apologies for this list not being exhaustive.
    Values are: CNY, EUR, INR, AUD, CHF, DKK, other, RUR, SEK, GBP, JPY, NOK, CAD, USD
    """
    pass

class MonetaryAmountPerEnergyUnit(str):
    """Monetary amount per energy unit.
    Values are: USD_per_Wh, EUR_per_Wh
    """
    pass

class PerCent(float):
    """Normally 0 - 100 on a defined base
    """
    pass

class PU(float):
    """Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.
    """
    pass

class Money(float):
    """Amount of money
    """
    pass

class AbsoluteDate(str):
    """Date and time as 'yyyy-mm-dd', which conforms with ISO 8601. UTC time zone is specified as 'yyyy-mm-dd'.
    """
    pass

class Seconds(float):
    """Time, in seconds
    """
    pass

class Voltage(float):
    """Electrical voltage.
    """
    pass

class Reactance(float):
    """Reactance (imaginary part of impedance), at rated frequency.
    """
    pass

class WaterLevel(float):
    """Reservoir water level referred to a given datum such as mean sea level.
    """
    pass

class ActivePowerChangeRate(float):
    pass

class ActivePower(float):
    """Product of RMS value of the voltage and the RMS value of the in-phase component of the current
    """
    pass

class Length(float):
    """Unit of length.
    """
    pass

class ApparentPower(float):
    """Product of the RMS value of the voltage and the RMS value of the current
    """
    pass

class Frequency(float):
    """Cycles per second
    """
    pass

class Susceptance(float):
    """Imaginary part of admittance.
    """
    pass

class Resistance(float):
    """Resistance (real part of impedance).
    """
    pass

class Conductance(float):
    """Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.
    """
    pass

class CurrentFlow(float):
    """Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)
    """
    pass

class RealEnergy(float):
    """Real electrical energy
    """
    pass

class Damping(float):
    """Per-unit active power variation with per-unit frequency referenced on the system apparent power base. Typical values in range 1.0 - 2.0.
    """
    pass

class StringQuantity(str):
    """Quantity with string value (when it is not important whether it is an integral or a floating point number) and associated unit information.
    """
    pass

class ReactivePower(float):
    """Product of RMS value of the voltage and the RMS value of the quadrature component of the current.
    """
    pass

class AngleRadians(float):
    """Phase angle in radians
    """
    pass

class Temperature(float):
    """Value of temperature in degrees Celsius.
    """
    pass

class KWActivePower(float):
    """Active power in kilowatts.
    """
    pass

class CostPerEnergyUnit(float):
    """Cost, in units of currency, per quantity of electrical energy generated.
    """
    pass

class VoltagePerReactivePower(float):
    """Voltage variation with reactive power
    """
    pass

class Impedance(float):
    """Ratio of voltage to current.
    """
    pass

class Weight(float):
    """The weight of an object.
    """
    pass

class AngleDegrees(float):
    """Measurement of angle in degrees
    """
    pass

class RotationSpeed(float):
    """Number of revolutions per second.
    """
    pass

class Volume(float):
    """Volume.
    """
    pass

class FloatQuantity(float):
    """Quantity with float value and associated unit information.
    """
    pass

class CostRate(float):
    """Cost, in units of currency, per hour of elapsed time
    """
    pass

class Inductance(float):
    """Inductance.
    """
    pass

class Pressure(float):
    """Pressure in Pascal.
    """
    pass

class Hours(float):
    """Time, in hours
    """
    pass

class Minutes(float):
    """Time in minutes
    """
    pass
