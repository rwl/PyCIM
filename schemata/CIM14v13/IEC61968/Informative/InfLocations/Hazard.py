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

class Hazard(IdentifiedObject):
    """A hazard is any object or condition that is a danger for causing loss or perils to an asset and/or people. Examples of hazards are trees growing under overhead power lines, a park being located by a substation (i.e., children climb fence to recover a ball), a lake near an overhead distribution line (fishing pole/line contacting power lines), etc.
    """

    def __init__(self, category='', Assets=None, Locations=None, status=None, *args, **kw_args):
        """Initializes a new 'Hazard' instance.

        @param category: Category by utility's corporate standards and practices. 
        @param Assets:
        @param Locations: The point or polygon location of a given hazard.
        @param status:
        """
        #: Category by utility's corporate standards and practices.
        self.category = category

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self.status = status

        super(Hazard, self).__init__(*args, **kw_args)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.Hazards if q != self]
            self._Assets._Hazards = filtered
        for r in value:
            if self not in r._Hazards:
                r._Hazards.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._Hazards:
                obj._Hazards.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._Hazards:
                obj._Hazards.remove(self)
            self._Assets.remove(obj)

    def getLocations(self):
        """The point or polygon location of a given hazard.
        """
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.Hazards if q != self]
            self._Locations._Hazards = filtered
        for r in value:
            if self not in r._Hazards:
                r._Hazards.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._Hazards:
                obj._Hazards.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._Hazards:
                obj._Hazards.remove(self)
            self._Locations.remove(obj)

    status = None

