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

"""The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""

from CIM14.CPSM.Equipment.Generation.Production.FossilFuel import FossilFuel
from CIM14.CPSM.Equipment.Generation.Production.HydroGeneratingUnit import HydroGeneratingUnit
from CIM14.CPSM.Equipment.Generation.Production.GrossToNetActivePowerCurve import GrossToNetActivePowerCurve
from CIM14.CPSM.Equipment.Generation.Production.ThermalGeneratingUnit import ThermalGeneratingUnit
from CIM14.CPSM.Equipment.Generation.Production.HydroPump import HydroPump
from CIM14.CPSM.Equipment.Generation.Production.WindGeneratingUnit import WindGeneratingUnit
from CIM14.CPSM.Equipment.Generation.Production.GeneratingUnit import GeneratingUnit
from CIM14.CPSM.Equipment.Generation.Production.NuclearGeneratingUnit import NuclearGeneratingUnit

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#Production"
nsPrefix = "cimProduction"


class FuelType(str):
    """Values are: oil, coal, lignite, gas
    """
    pass

class GeneratorControlSource(str):
    """Values are: onAGC, unavailable, plantControl, offAGC
    """
    pass
