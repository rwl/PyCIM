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

"""The domain package define primitive datatypes that are used by classes in other packages. Stereotypes are used to describe the datatypes. The following sterotypes are defined  &lt;&lt;enumeration&gt;&gt; A list of permissable constant values.  &lt;&lt;Primitive&gt;&gt; The most basic data types that all other data types derive from.  &lt;&lt;CIMDataType&gt;&gt; A datatype that contains a value attribute, an optional unit of measure and a unit multiplier. The unit and multiplier are specified as a static variable initialized to the allowed value.  &lt;&lt;Compound&gt;&gt; A composite of two or more attributes.
"""

from CIM15.IEC61970.Domain.DateTimeInterval import DateTimeInterval

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#Domain"
nsPrefix = "cimDomain"


class UnitSymbol(str):
    """Values are: N, A, rad, VAh, Pa, J, h, Hz, VArh, ohm, H, m3, deg, V, oC, F, Wh, s, g, min, S, none, W, VAr, m2, m, VA
    """
    pass

class Currency(str):
    """Values are: CAD, EUR, CHF, INR, AUD, USD, RUR, GBP, CNY, SEK, JPY, other, NOK, DKK
    """
    pass

class UnitMultiplier(str):
    """Values are: M, G, d, micro, c, p, n, T, k, m, none
    """
    pass

class ReactancePerLength(float):
    """Reactance (imaginary part of impedance) per unit of length, at rated frequency.
    """
    pass

class ApparentPower(float):
    """Product of the RMS value of the voltage and the RMS value of the current
    """
    pass

class Damping(float):
    """Per-unit active power variation with per-unit frequency referenced on the system apparent power base. Typical values in range 1.0 - 2.0.
    """
    pass

class Susceptance(float):
    """Imaginary part of admittance.
    """
    pass

class ResistancePerLength(float):
    """Resistance (real part of impedance) per unit of length.
    """
    pass

class PU(float):
    """Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.
    """
    pass

class CurrentFlow(float):
    """Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)
    """
    pass

class AngleDegrees(float):
    """Measurement of angle in degrees
    """
    pass

class CostRate(float):
    """Cost, in units of currency, per hour of elapsed time
    """
    pass

class CostPerEnergyUnit(float):
    """Cost, in units of currency, per quantity of electrical energy generated.
    """
    pass

class Displacement(float):
    """Unit of displacement relative a reference position, hence can be negative.
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

class Pressure(float):
    """Pressure in Pascal.
    """
    pass

class Temperature(float):
    """Value of temperature in degrees Celsius.
    """
    pass

class RotationSpeed(float):
    """Number of revolutions per second.
    """
    pass

class SusceptancePerLength(float):
    """Imaginary part of admittance per unit of length.
    """
    pass

class StringQuantity(str):
    """Quantity with string value (when it is not important whether it is an integral or a floating point number) and associated unit information.
    """
    pass

class ActivePowerChangeRate(float):
    pass

class AbsoluteDate(str):
    """Date and time as 'yyyy-mm-dd', which conforms with ISO 8601. UTC time zone is specified as 'yyyy-mm-ddZ'. A local timezone relative UTC is specified as 'yyyy-mm-dd(+/-)hh:mm'.
    """
    pass

class ActivePower(float):
    """Product of RMS value of the voltage and the RMS value of the in-phase component of the current
    """
    pass

class Volume(float):
    """Volume.
    """
    pass

class Conductance(float):
    """Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.
    """
    pass

class Inductance(float):
    """Inductance.
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

class Frequency(float):
    """Cycles per second
    """
    pass

class Capacitance(float):
    """A Farad, the typical unit, is the capacitance in which a charge of 1 coulomb produces 1 volt potential difference between its terminals.
    """
    pass

class Money(float):
    """Amount of money
    """
    pass

class RealEnergy(float):
    """Real electrical energy
    """
    pass

class KWActivePower(float):
    """Active power in kilowatts.
    """
    pass

class Minutes(float):
    """Time in minutes
    """
    pass

class Impedance(float):
    """Ratio of voltage to current.
    """
    pass

class VoltagePerReactivePower(float):
    """Voltage variation with reactive power
    """
    pass

class VolumeFlowRate(float):
    pass

class ConductancePerLength(float):
    """Real part of admittance per unit of length.
    """
    pass

class PerCent(float):
    """Normally 0 - 100 on a defined base
    """
    pass

class Weight(float):
    """The weight of an object.
    """
    pass

class Resistance(float):
    """Resistance (real part of impedance).
    """
    pass

class Seconds(float):
    """Time, in seconds
    """
    pass

class FloatQuantity(float):
    """Quantity with float value and associated unit information.
    """
    pass

class WaterLevel(float):
    """Reservoir water level referred to a given datum such as mean sea level.
    """
    pass

class Length(float):
    """Unit of length.
    """
    pass

class Hours(float):
    """Time, in hours
    """
    pass

class IntegerQuantity(str):
    """Quantity with integer value and associated unit information.
    """
    pass

class CostPerVolume(float):
    pass
