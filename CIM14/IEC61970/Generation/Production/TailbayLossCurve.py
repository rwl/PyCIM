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

class TailbayLossCurve(Curve):
    """Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level
    """

    def __init__(self, HydroGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'TailbayLossCurve' instance.

        @param HydroGeneratingUnit: A hydro generating unit has a tailbay loss curve
        """
        self._HydroGeneratingUnit = None
        self.HydroGeneratingUnit = HydroGeneratingUnit

        super(TailbayLossCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["HydroGeneratingUnit"]
    _many_refs = []

    def getHydroGeneratingUnit(self):
        """A hydro generating unit has a tailbay loss curve
        """
        return self._HydroGeneratingUnit

    def setHydroGeneratingUnit(self, value):
        if self._HydroGeneratingUnit is not None:
            filtered = [x for x in self.HydroGeneratingUnit.TailbayLossCurve if x != self]
            self._HydroGeneratingUnit._TailbayLossCurve = filtered

        self._HydroGeneratingUnit = value
        if self._HydroGeneratingUnit is not None:
            if self not in self._HydroGeneratingUnit._TailbayLossCurve:
                self._HydroGeneratingUnit._TailbayLossCurve.append(self)

    HydroGeneratingUnit = property(getHydroGeneratingUnit, setHydroGeneratingUnit)

