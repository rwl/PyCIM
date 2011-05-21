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

class ShutdownCurve(Curve):
    """Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)
    """

    def __init__(self, shutdownCost=0.0, shutdownDate='', ThermalGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'ShutdownCurve' instance.

        @param shutdownCost: Fixed shutdown cost 
        @param shutdownDate: The date and time of the most recent generating unit shutdown 
        @param ThermalGeneratingUnit: A thermal generating unit may have a shutdown curve
        """
        #: Fixed shutdown cost
        self.shutdownCost = shutdownCost

        #: The date and time of the most recent generating unit shutdown
        self.shutdownDate = shutdownDate

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(ShutdownCurve, self).__init__(*args, **kw_args)

    _attrs = ["shutdownCost", "shutdownDate"]
    _attr_types = {"shutdownCost": float, "shutdownDate": str}
    _defaults = {"shutdownCost": 0.0, "shutdownDate": ''}
    _enums = {}
    _refs = ["ThermalGeneratingUnit"]
    _many_refs = []

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have a shutdown curve
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._ShutdownCurve = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit.ShutdownCurve = None
            self._ThermalGeneratingUnit._ShutdownCurve = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

