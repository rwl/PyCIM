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

class Medium(IdentifiedObject):
    """A substance that either (1) provides the means of transmission of a force or effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping substance, such as oil in a transformer or circuit breaker.
    """

    def __init__(self, kind='solid', volumeSpec=0.0, Assets=None, Specification=None, *args, **kw_args):
        """Initializes a new 'Medium' instance.

        @param kind: Kind of this medium. Values are: "solid", "gas", "liquid"
        @param volumeSpec: The volume of the medium specified for this application. Note that the actual volume is a type of measurement associated witht the asset. 
        @param Assets:
        @param Specification:
        """
        #: Kind of this medium.Values are: "solid", "gas", "liquid"
        self.kind = kind

        #: The volume of the medium specified for this application. Note that the actual volume is a type of measurement associated witht the asset.
        self.volumeSpec = volumeSpec

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._Specification = None
        self.Specification = Specification

        super(Medium, self).__init__(*args, **kw_args)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.Mediums if q != self]
            self._Assets._Mediums = filtered
        for r in value:
            if self not in r._Mediums:
                r._Mediums.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._Mediums:
                obj._Mediums.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._Mediums:
                obj._Mediums.remove(self)
            self._Assets.remove(obj)

    def getSpecification(self):
        
        return self._Specification

    def setSpecification(self, value):
        if self._Specification is not None:
            filtered = [x for x in self.Specification.Mediums if x != self]
            self._Specification._Mediums = filtered

        self._Specification = value
        if self._Specification is not None:
            self._Specification._Mediums.append(self)

    Specification = property(getSpecification, setSpecification)

