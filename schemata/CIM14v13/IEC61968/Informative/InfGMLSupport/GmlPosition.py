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

from CIM14v13.IEC61968.Common.PositionPoint import PositionPoint

class GmlPosition(PositionPoint):
    """Position point with a GML coordinate reference system.
    """

    def __init__(self, GmlCoordinateSystem=None, **kw_args):
        """Initializes a new 'GmlPosition' instance.

        @param GmlCoordinateSystem:
        """
        self._GmlCoordinateSystem = None
        self.GmlCoordinateSystem = GmlCoordinateSystem

        super(GmlPosition, self).__init__(**kw_args)

    def getGmlCoordinateSystem(self):
        
        return self._GmlCoordinateSystem

    def setGmlCoordinateSystem(self, value):
        if self._GmlCoordinateSystem is not None:
            filtered = [x for x in self.GmlCoordinateSystem.GmlPositions if x != self]
            self._GmlCoordinateSystem._GmlPositions = filtered

        self._GmlCoordinateSystem = value
        if self._GmlCoordinateSystem is not None:
            self._GmlCoordinateSystem._GmlPositions.append(self)

    GmlCoordinateSystem = property(getGmlCoordinateSystem, setGmlCoordinateSystem)

