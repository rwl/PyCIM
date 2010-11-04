# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.Curve import Curve

class StartUpTimeCurve(Curve):
    """Startup time curve as a function of down time, where time is specified in seconds.  Relationship between unit startup time (Y1-axis) vs. unit elapsed down time (X-axis).
    """

    def __init__(self, GeneratingBids=None, **kw_args):
        """Initializes a new 'StartUpTimeCurve' instance.

        @param GeneratingBids:
        """
        self._GeneratingBids = []
        self.GeneratingBids = [] if GeneratingBids is None else GeneratingBids

        super(StartUpTimeCurve, self).__init__(**kw_args)

    def getGeneratingBids(self):
        
        return self._GeneratingBids

    def setGeneratingBids(self, value):
        for x in self._GeneratingBids:
            x._StartUpTimeCurve = None
        for y in value:
            y._StartUpTimeCurve = self
        self._GeneratingBids = value

    GeneratingBids = property(getGeneratingBids, setGeneratingBids)

    def addGeneratingBids(self, *GeneratingBids):
        for obj in GeneratingBids:
            obj._StartUpTimeCurve = self
            self._GeneratingBids.append(obj)

    def removeGeneratingBids(self, *GeneratingBids):
        for obj in GeneratingBids:
            obj._StartUpTimeCurve = None
            self._GeneratingBids.remove(obj)

