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

class TargetLevelSchedule(Curve):
    """Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days
    """

    def __init__(self, highLevelLimit=0.0, lowLevelLimit=0.0, Reservoir=None, *args, **kw_args):
        """Initialises a new 'TargetLevelSchedule' instance.

        @param highLevelLimit: High target level limit, above which the reservoir operation will be penalized 
        @param lowLevelLimit: Low target level limit, below which the reservoir operation will be penalized 
        @param Reservoir: A reservoir may have a water level target schedule.
        """
        #: High target level limit, above which the reservoir operation will be penalized
        self.highLevelLimit = highLevelLimit

        #: Low target level limit, below which the reservoir operation will be penalized
        self.lowLevelLimit = lowLevelLimit

        self._Reservoir = None
        self.Reservoir = Reservoir

        super(TargetLevelSchedule, self).__init__(*args, **kw_args)

    _attrs = ["highLevelLimit", "lowLevelLimit"]
    _attr_types = {"highLevelLimit": float, "lowLevelLimit": float}
    _defaults = {"highLevelLimit": 0.0, "lowLevelLimit": 0.0}
    _enums = {}
    _refs = ["Reservoir"]
    _many_refs = []

    def getReservoir(self):
        """A reservoir may have a water level target schedule.
        """
        return self._Reservoir

    def setReservoir(self, value):
        if self._Reservoir is not None:
            self._Reservoir._TargetLevelSchedule = None

        self._Reservoir = value
        if self._Reservoir is not None:
            self._Reservoir.TargetLevelSchedule = None
            self._Reservoir._TargetLevelSchedule = self

    Reservoir = property(getReservoir, setReservoir)

