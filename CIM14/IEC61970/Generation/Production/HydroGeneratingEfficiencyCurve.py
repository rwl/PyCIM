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

class HydroGeneratingEfficiencyCurve(Curve):
    """Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.
    """

    def __init__(self, HydroGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'HydroGeneratingEfficiencyCurve' instance.

        @param HydroGeneratingUnit: A hydro generating unit has an efficiency curve
        """
        self._HydroGeneratingUnit = None
        self.HydroGeneratingUnit = HydroGeneratingUnit

        super(HydroGeneratingEfficiencyCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["HydroGeneratingUnit"]
    _many_refs = []

    def getHydroGeneratingUnit(self):
        """A hydro generating unit has an efficiency curve
        """
        return self._HydroGeneratingUnit

    def setHydroGeneratingUnit(self, value):
        if self._HydroGeneratingUnit is not None:
            filtered = [x for x in self.HydroGeneratingUnit.HydroGeneratingEfficiencyCurves if x != self]
            self._HydroGeneratingUnit._HydroGeneratingEfficiencyCurves = filtered

        self._HydroGeneratingUnit = value
        if self._HydroGeneratingUnit is not None:
            if self not in self._HydroGeneratingUnit._HydroGeneratingEfficiencyCurves:
                self._HydroGeneratingUnit._HydroGeneratingEfficiencyCurves.append(self)

    HydroGeneratingUnit = property(getHydroGeneratingUnit, setHydroGeneratingUnit)

