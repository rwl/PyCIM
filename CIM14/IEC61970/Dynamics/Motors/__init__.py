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


from CIM14.IEC61970.Dynamics.Motors.MechanicalLoad import MechanicalLoad
from CIM14.IEC61970.Dynamics.Motors.MotorSync import MotorSync
from CIM14.IEC61970.Dynamics.Motors.MechLoad1 import MechLoad1
from CIM14.IEC61970.Dynamics.Motors.MotorAsync import MotorAsync

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Motors"
nsPrefix = "cimMotors"


class SynchronousMotorType(str):
    """Type of synchronous motor
    Values are: salientPole, roundRotor
    """
    pass
