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

"""Contains entities to model information used by Supervisory Control and Data Acquisition (SCADA) applications. Supervisory control supports operator control of equipment, such as opening or closing a breaker. Data acquisition gathers telemetered data from various sources.  The subtypes of the Telemetry entity deliberately match the UCA and IEC 61850 definitions.  This package also supports alarm presentation but it is not expected to be used by other applications.
"""

from CIM15.IEC61970.SCADA.RemoteSource import RemoteSource
from CIM15.IEC61970.SCADA.RemotePoint import RemotePoint
from CIM15.IEC61970.SCADA.RemoteUnit import RemoteUnit
from CIM15.IEC61970.SCADA.RemoteControl import RemoteControl
from CIM15.IEC61970.SCADA.CommunicationLink import CommunicationLink

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#SCADA"
nsPrefix = "cimSCADA"


class RemoteUnitType(str):
    """Values are: SubstationControlSystem, IED, ControlCenter, RTU
    """
    pass

class Source(str):
    """Values are: SUBSTITUTED, DEFAULTED, PROCESS
    """
    pass
