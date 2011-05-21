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


nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#Domain"
nsPrefix = "cimDomain"


class UnitSymbol(str):
    """Values are: A, rad, none, g, W/Hz, V, m2, VA, VArh, N, Pa, VAh, F, H, Hz-1, W/s, J, m, S, min, deg, J/s, s, Wh, m3, oC, V/VAr, s-1, h, W, ohm, Hz, VAr, kg/J
    """
    pass

class Money(float):
    """Amount of money
    """
    pass

class ApparentPower(float):
    """Product of the RMS value of the voltage and the RMS value of the current
    """
    pass

class Resistance(float):
    """Resistance (real part of impedance).
    """
    pass

class ActivePower(float):
    """Product of RMS value of the voltage and the RMS value of the in-phase component of the current
    """
    pass

class Susceptance(float):
    """Imaginary part of admittance.
    """
    pass

class CurrentFlow(float):
    """Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)
    """
    pass

class Conductance(float):
    """Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.
    """
    pass

class Length(float):
    """Unit of length.
    """
    pass

class Reactance(float):
    """Reactance (imaginary part of impedance), at rated frequency.
    """
    pass

class Seconds(float):
    """Time, in seconds
    """
    pass

class VoltagePerReactivePower(float):
    """Voltage variation with reactive power
    """
    pass

class Voltage(float):
    """Electrical voltage.
    """
    pass

class ReactivePower(float):
    """Product of RMS value of the voltage and the RMS value of the quadrature component of the current.
    """
    pass

class AngleDegrees(float):
    """Measurement of angle in degrees
    """
    pass

class PerCent(float):
    """Normally 0 - 100 on a defined base
    """
    pass
