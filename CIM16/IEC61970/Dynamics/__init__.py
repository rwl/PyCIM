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

# Modified by Gustav Holm (guholm@kth.se) & Francis J. Gomez (fragom@kth.se)
# Modified date: 05/06/2017

from CIM16.IEC61970.Dynamics.DynamicsFunctionBlock import DynamicsFunctionBlock
from CIM16.IEC61970.Dynamics.RotatingMachineDynamics import RotatingMachineDynamics
from CIM16.IEC61970.Dynamics.SynchronousMachineDynamics import SynchronousMachineDynamics
from CIM16.IEC61970.Dynamics.SynchronousMachineUserDefined import SynchronousMachineUserDefined
from CIM16.IEC61970.Dynamics.SynchronousMachineDetailed import SynchronousMachineDetailed
from CIM16.IEC61970.Dynamics.SynchronousMachineSimplified import SynchronousMachineSimplified
from CIM16.IEC61970.Dynamics.SynchronousMachineTimeConstantReactance import SynchronousMachineTimeConstantReactance
from CIM16.IEC61970.Dynamics.SynchronousMachineEquivalentCircuit import SynchronousMachineEquivalentCircuit

nsURI = "http://iec.ch/TC57/2013/CIM-schema-cim16#Dynamics"
nsPrefix = "cimDynamics"

