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


from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PowerSystemStabilizer import PowerSystemStabilizer
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssIEEE3B import PssIEEE3B
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssSK import PssSK
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssIEEE4B import PssIEEE4B
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssIEEE1A import PssIEEE1A
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssPTIST1 import PssPTIST1
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssIEEE2B import PssIEEE2B
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssSB import PssSB
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssSB4 import PssSB4
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssSH import PssSH
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssPTIST3 import PssPTIST3
from CIM14.IEC61970.Dynamics.PowerSystemStabilizers.PssWSCC import PssWSCC

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#PowerSystemStabilizers"
nsPrefix = "cimPowerSystemStabilizers"


class InputSignalCodeJ(str):
    """Values are: 2, 4, 3, 5, 1, 6
    """
    pass
