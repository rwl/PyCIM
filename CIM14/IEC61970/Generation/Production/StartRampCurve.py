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

class StartRampCurve(Curve):
    """Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line
    """

    def __init__(self, hotStandbyRamp=0.0, StartupModel=None, *args, **kw_args):
        """Initialises a new 'StartRampCurve' instance.

        @param hotStandbyRamp: The startup ramp rate in gross for a unit that is on hot standby 
        @param StartupModel: The unit's startup model may have a startup ramp curve
        """
        #: The startup ramp rate in gross for a unit that is on hot standby
        self.hotStandbyRamp = hotStandbyRamp

        self._StartupModel = None
        self.StartupModel = StartupModel

        super(StartRampCurve, self).__init__(*args, **kw_args)

    _attrs = ["hotStandbyRamp"]
    _attr_types = {"hotStandbyRamp": float}
    _defaults = {"hotStandbyRamp": 0.0}
    _enums = {}
    _refs = ["StartupModel"]
    _many_refs = []

    def getStartupModel(self):
        """The unit's startup model may have a startup ramp curve
        """
        return self._StartupModel

    def setStartupModel(self, value):
        if self._StartupModel is not None:
            self._StartupModel._StartRampCurve = None

        self._StartupModel = value
        if self._StartupModel is not None:
            self._StartupModel.StartRampCurve = None
            self._StartupModel._StartRampCurve = self

    StartupModel = property(getStartupModel, setStartupModel)

