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

class Route(IdentifiedObject):
    """Route that is followed, for example by service crews.
    """

    def __init__(self, category='', Locations=None, Crews=None, status=None, *args, **kw_args):
        """Initializes a new 'Route' instance.

        @param category: Category by utility's work management standards and practices. 
        @param Locations:
        @param Crews:
        @param status:
        """
        #: Category by utility's work management standards and practices. 
        self.category = category

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self.status = status

        super(Route, self).__init__(*args, **kw_args)

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.Routes if q != self]
            self._Locations._Routes = filtered
        for r in value:
            if self not in r._Routes:
                r._Routes.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._Routes:
                obj._Routes.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._Routes:
                obj._Routes.remove(self)
            self._Locations.remove(obj)

    def getCrews(self):
        
        return self._Crews

    def setCrews(self, value):
        for x in self._Crews:
            x._Route = None
        for y in value:
            y._Route = self
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            obj._Route = self
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            obj._Route = None
            self._Crews.remove(obj)

    status = None

