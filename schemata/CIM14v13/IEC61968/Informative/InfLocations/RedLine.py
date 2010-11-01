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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class RedLine(IdentifiedObject):
    """This class is used for handling the accompanying annotations, time stamp, author, etc. of designs, drawings and maps. A red line can be associated with any Location object.
    """

    def __init__(self, status=None, Locations=None, *args, **kw_args):
        """Initializes a new 'RedLine' instance.

        @param status:
        @param Locations:
        """
        self.status = status

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        super(RedLine, self).__init__(*args, **kw_args)

    status = None

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.RedLines if q != self]
            self._Locations._RedLines = filtered
        for r in value:
            if self not in r._RedLines:
                r._RedLines.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._RedLines:
                obj._RedLines.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._RedLines:
                obj._RedLines.remove(self)
            self._Locations.remove(obj)

