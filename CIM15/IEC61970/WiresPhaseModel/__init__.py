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


from CIM15.IEC61970.WiresPhaseModel.SwitchPhase import SwitchPhase
from CIM15.IEC61970.WiresPhaseModel.ShuntCompensatorPhase import ShuntCompensatorPhase
from CIM15.IEC61970.WiresPhaseModel.EnergyConsumerPhase import EnergyConsumerPhase
from CIM15.IEC61970.WiresPhaseModel.ACLineSegmentPhase import ACLineSegmentPhase

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#WiresPhaseModel"
nsPrefix = "cimWiresPhaseModel"


class SinglePhaseKind(str):
    """Values are: C, N, s1, B, s2, A
    """
    pass
