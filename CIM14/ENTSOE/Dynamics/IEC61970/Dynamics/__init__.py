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


from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockState import DynamicsMetaBlockState
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockConSignal import DynamicsMetaBlockConSignal
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockReference import DynamicsMetaBlockReference
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockSignal import DynamicsMetaBlockSignal
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsAttributeBlockParameter import DynamicsAttributeBlockParameter
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockConnection import DynamicsMetaBlockConnection
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockConOutput import DynamicsMetaBlockConOutput
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockInput import DynamicsMetaBlockInput
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockOutputReference import DynamicsMetaBlockOutputReference
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockStateReference import DynamicsMetaBlockStateReference
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsBlockConnection import DynamicsBlockConnection
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockConnectivity import DynamicsMetaBlockConnectivity
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlock import DynamicsMetaBlock
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockConInput import DynamicsMetaBlockConInput
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockParameter import DynamicsMetaBlockParameter
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockConnectable import DynamicsMetaBlockConnectable
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockInputReference import DynamicsMetaBlockInputReference
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsRotatingMachine import DynamicsRotatingMachine
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsBlockConnectivity import DynamicsBlockConnectivity
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockParameterReference import DynamicsMetaBlockParameterReference
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsAsynchronousMachine import DynamicsAsynchronousMachine
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsBlockParameter import DynamicsBlockParameter
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsBlock import DynamicsBlock
from CIM14.ENTSOE.Dynamics.IEC61970.Dynamics.DynamicsMetaBlockOutput import DynamicsMetaBlockOutput

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#Dynamics"
nsPrefix = "cimDynamics"


class DynamicsBlockKind(str):
    pass
