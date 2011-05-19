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

from CIM15.IEC61970.Core.Curve import Curve

class PenstockLossCurve(Curve):
    """Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.
    """

    def __init__(self, HydroGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'PenstockLossCurve' instance.

        @param HydroGeneratingUnit: A hydro generating unit has a penstock loss curve
        """
        self._HydroGeneratingUnit = None
        self.HydroGeneratingUnit = HydroGeneratingUnit

        super(PenstockLossCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["HydroGeneratingUnit"]
    _many_refs = []

    def getHydroGeneratingUnit(self):
        """A hydro generating unit has a penstock loss curve
        """
        return self._HydroGeneratingUnit

    def setHydroGeneratingUnit(self, value):
        if self._HydroGeneratingUnit is not None:
            self._HydroGeneratingUnit._PenstockLossCurve = None

        self._HydroGeneratingUnit = value
        if self._HydroGeneratingUnit is not None:
            self._HydroGeneratingUnit.PenstockLossCurve = None
            self._HydroGeneratingUnit._PenstockLossCurve = self

    HydroGeneratingUnit = property(getHydroGeneratingUnit, setHydroGeneratingUnit)

