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

class GmlSelector(IdentifiedObject):
    """A diagram element that allows selection by a user, i.e. as 'hyperNode' for navigating between diagrams, or as composite object representing multiple grouped objects.
    """

    def __init__(self, Locations=None, ChangeItems=None, **kw_args):
        """Initializes a new 'GmlSelector' instance.

        @param Locations:
        @param ChangeItems:
        """
        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        super(GmlSelector, self).__init__(**kw_args)

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.GmlSelectors if q != self]
            self._Locations._GmlSelectors = filtered
        for r in value:
            if self not in r._GmlSelectors:
                r._GmlSelectors.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._GmlSelectors:
                obj._GmlSelectors.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._GmlSelectors:
                obj._GmlSelectors.remove(self)
            self._Locations.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._GmlSelector = None
        for y in value:
            y._GmlSelector = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._GmlSelector = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._GmlSelector = None
            self._ChangeItems.remove(obj)

