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

from CIM14.IEC61970.Core.Curve import Curve

class GenUnitOpCostCurve(Curve):
    """Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.
    """

    def __init__(self, isNetGrossP=False, GeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'GenUnitOpCostCurve' instance.

        @param isNetGrossP: Flag is set to true when output is expressed in net active power 
        @param GeneratingUnit: A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        #: Flag is set to true when output is expressed in net active power
        self.isNetGrossP = isNetGrossP

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(GenUnitOpCostCurve, self).__init__(*args, **kw_args)

    _attrs = ["isNetGrossP"]
    _attr_types = {"isNetGrossP": bool}
    _defaults = {"isNetGrossP": False}
    _enums = {}
    _refs = ["GeneratingUnit"]
    _many_refs = []

    def getGeneratingUnit(self):
        """A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            filtered = [x for x in self.GeneratingUnit.GenUnitOpCostCurves if x != self]
            self._GeneratingUnit._GenUnitOpCostCurves = filtered

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            if self not in self._GeneratingUnit._GenUnitOpCostCurves:
                self._GeneratingUnit._GenUnitOpCostCurves.append(self)

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

