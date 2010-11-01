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

from CIM14v13.IEC61970.Meas.LimitSet import LimitSet

class AnalogLimitSet(LimitSet):
    """An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.
    """

    def __init__(self, Limits=None, Measurements=None, *args, **kw_args):
        """Initializes a new 'AnalogLimitSet' instance.

        @param Limits: The limit values used for supervision of Measurements.
        @param Measurements: The Measurements using the LimitSet.
        """
        self._Limits = []
        self.Limits = [] if Limits is None else Limits

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        super(AnalogLimitSet, self).__init__(*args, **kw_args)

    def getLimits(self):
        """The limit values used for supervision of Measurements.
        """
        return self._Limits

    def setLimits(self, value):
        for x in self._Limits:
            x._LimitSet = None
        for y in value:
            y._LimitSet = self
        self._Limits = value

    Limits = property(getLimits, setLimits)

    def addLimits(self, *Limits):
        for obj in Limits:
            obj._LimitSet = self
            self._Limits.append(obj)

    def removeLimits(self, *Limits):
        for obj in Limits:
            obj._LimitSet = None
            self._Limits.remove(obj)

    def getMeasurements(self):
        """The Measurements using the LimitSet.
        """
        return self._Measurements

    def setMeasurements(self, value):
        for p in self._Measurements:
            filtered = [q for q in p.LimitSets if q != self]
            self._Measurements._LimitSets = filtered
        for r in value:
            if self not in r._LimitSets:
                r._LimitSets.append(self)
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            if self not in obj._LimitSets:
                obj._LimitSets.append(self)
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            if self in obj._LimitSets:
                obj._LimitSets.remove(self)
            self._Measurements.remove(obj)

