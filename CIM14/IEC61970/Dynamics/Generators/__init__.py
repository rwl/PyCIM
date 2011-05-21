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


from CIM14.IEC61970.Dynamics.Generators.GenLoad import GenLoad
from CIM14.IEC61970.Dynamics.Generators.GenEquiv import GenEquiv
from CIM14.IEC61970.Dynamics.Generators.GenAsync import GenAsync

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Generators"
nsPrefix = "cimGenerators"


class IfdBaseType(str):
    """Values are: other, iffl, ifag, ifnl
    """
    pass

class SynchronousGeneratorType(str):
    """Type of synchronous generator as used in dynamic simulation applications
    Values are: roundRotor, transient, typeF, typeJ, salientPole
    """
    pass

class ParametersFormType(str):
    """Values are: timeConstantReactance, equivalentCircuit
    """
    pass
