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

from CIM14v13.IEC61970.Core.BasicIntervalSchedule import BasicIntervalSchedule

class RegularIntervalSchedule(BasicIntervalSchedule):
    """The schedule has TimePoints where the time between them is constant.
    """

    def __init__(self, timeStep=0.0, endTime='', TimePoints=None, *args, **kw_args):
        """Initializes a new 'RegularIntervalSchedule' instance.

        @param timeStep: The time between each pair of subsequent RegularTimePoints. 
        @param endTime: The time for the last time point. 
        @param TimePoints: The point data values that define a curve
        """
        #: The time between each pair of subsequent RegularTimePoints.
        self.timeStep = timeStep

        #: The time for the last time point.
        self.endTime = endTime

        self._TimePoints = []
        self.TimePoints = [] if TimePoints is None else TimePoints

        super(RegularIntervalSchedule, self).__init__(*args, **kw_args)

    def getTimePoints(self):
        """The point data values that define a curve
        """
        return self._TimePoints

    def setTimePoints(self, value):
        for x in self._TimePoints:
            x._IntervalSchedule = None
        for y in value:
            y._IntervalSchedule = self
        self._TimePoints = value

    TimePoints = property(getTimePoints, setTimePoints)

    def addTimePoints(self, *TimePoints):
        for obj in TimePoints:
            obj._IntervalSchedule = self
            self._TimePoints.append(obj)

    def removeTimePoints(self, *TimePoints):
        for obj in TimePoints:
            obj._IntervalSchedule = None
            self._TimePoints.remove(obj)

