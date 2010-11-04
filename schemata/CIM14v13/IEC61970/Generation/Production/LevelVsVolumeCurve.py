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

class LevelVsVolumeCurve(Curve):
    """Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.
    """

    def __init__(self, Reservoir=None, **kw_args):
        """Initializes a new 'LevelVsVolumeCurve' instance.

        @param Reservoir: A reservoir may have a level versus volume relationship.
        """
        self._Reservoir = None
        self.Reservoir = Reservoir

        super(LevelVsVolumeCurve, self).__init__(**kw_args)

    def getReservoir(self):
        """A reservoir may have a level versus volume relationship.
        """
        return self._Reservoir

    def setReservoir(self, value):
        if self._Reservoir is not None:
            filtered = [x for x in self.Reservoir.LevelVsVolumeCurves if x != self]
            self._Reservoir._LevelVsVolumeCurves = filtered

        self._Reservoir = value
        if self._Reservoir is not None:
            self._Reservoir._LevelVsVolumeCurves.append(self)

    Reservoir = property(getReservoir, setReservoir)

