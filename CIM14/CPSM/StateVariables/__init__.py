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

from CIM14.CPSM.StateVariables.Element import Element

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile/CPSM/StateVariables"
nsPrefix = "sv"

packageMap = {
    "Element": "CIM14.CPSM.StateVariables",
    "TopologicalNode": "CIM14.CPSM.StateVariables.Topology",
    "Terminal": "CIM14.CPSM.StateVariables.Core",
    "SvTapStep": "CIM14.CPSM.StateVariables.StateVariables",
    "SvInjection": "CIM14.CPSM.StateVariables.StateVariables",
    "SvVoltage": "CIM14.CPSM.StateVariables.StateVariables",
    "TopologicalIsland": "CIM14.CPSM.StateVariables.StateVariables",
    "SvPowerFlow": "CIM14.CPSM.StateVariables.StateVariables",
    "SvShortCircuit": "CIM14.CPSM.StateVariables.StateVariables",
    "SvShuntCompensatorSections": "CIM14.CPSM.StateVariables.StateVariables",
    "ShuntCompensator": "CIM14.CPSM.StateVariables.Wires",
    "TapChanger": "CIM14.CPSM.StateVariables.Wires",
}


class ApparentPower(float):
    """Product of the RMS value of the voltage and the RMS value of the current
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

class AngleRadians(float):
    """Phase angle in radians
    """
    pass

class ActivePower(float):
    """Product of RMS value of the voltage and the RMS value of the in-phase component of the current
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
