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

"""State variables for analysis solutions such as powerflow.
"""

from CIM16.IEC61970.StateVariables.SvVoltage import SvVoltage
from CIM16.IEC61970.StateVariables.SvShortCircuit import SvShortCircuit
from CIM16.IEC61970.StateVariables.SvShuntCompensatorSections import SvShuntCompensatorSections
from CIM16.IEC61970.StateVariables.StateVariable import StateVariable
from CIM16.IEC61970.StateVariables.SvTapStep import SvTapStep
from CIM16.IEC61970.StateVariables.SvStatus import SvStatus
from CIM16.IEC61970.StateVariables.SvInjection import SvInjection
from CIM16.IEC61970.StateVariables.SvPowerFlow import SvPowerFlow
from CIM16.IEC61970.StateVariables.TopologicalIsland import TopologicalIsland

nsURI = "http://iec.ch/TC57/2013/CIM-schema-cim16#StateVariables"
nsPrefix = "cimStateVariables"

