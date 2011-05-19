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

class StartMainFuelCurve(Curve):
    """The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off lineThe quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """

    def __init__(self, mainFuelType="oil", StartupModel=None, *args, **kw_args):
        """Initialises a new 'StartMainFuelCurve' instance.

        @param mainFuelType: Type of main fuel Values are: "oil", "coal", "lignite", "gas"
        @param StartupModel: The unit's startup model may have a startup main fuel curve
        """
        #: Type of main fuel Values are: "oil", "coal", "lignite", "gas"
        self.mainFuelType = mainFuelType

        self._StartupModel = None
        self.StartupModel = StartupModel

        super(StartMainFuelCurve, self).__init__(*args, **kw_args)

    _attrs = ["mainFuelType"]
    _attr_types = {"mainFuelType": str}
    _defaults = {"mainFuelType": "oil"}
    _enums = {"mainFuelType": "FuelType"}
    _refs = ["StartupModel"]
    _many_refs = []

    def getStartupModel(self):
        """The unit's startup model may have a startup main fuel curve
        """
        return self._StartupModel

    def setStartupModel(self, value):
        if self._StartupModel is not None:
            self._StartupModel._StartMainFuelCurve = None

        self._StartupModel = value
        if self._StartupModel is not None:
            self._StartupModel.StartMainFuelCurve = None
            self._StartupModel._StartMainFuelCurve = self

    StartupModel = property(getStartupModel, setStartupModel)

