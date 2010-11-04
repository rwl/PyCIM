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

from CIM14v13.IEC61968.Assets.Asset import Asset

class AssetContainer(Asset):
    """Asset that is aggregation of other assets such as conductors, transformers, switchgear, land, fences, buildings, equipment, vehicles, etc.
    """

    def __init__(self, LandProperties=None, Assets=None, Seals=None, **kw_args):
        """Initializes a new 'AssetContainer' instance.

        @param LandProperties:
        @param Assets:
        @param Seals: All seals applied to this asset container.
        """
        self._LandProperties = []
        self.LandProperties = [] if LandProperties is None else LandProperties

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._Seals = []
        self.Seals = [] if Seals is None else Seals

        super(AssetContainer, self).__init__(**kw_args)

    def getLandProperties(self):
        
        return self._LandProperties

    def setLandProperties(self, value):
        for p in self._LandProperties:
            filtered = [q for q in p.AssetContainers if q != self]
            self._LandProperties._AssetContainers = filtered
        for r in value:
            if self not in r._AssetContainers:
                r._AssetContainers.append(self)
        self._LandProperties = value

    LandProperties = property(getLandProperties, setLandProperties)

    def addLandProperties(self, *LandProperties):
        for obj in LandProperties:
            if self not in obj._AssetContainers:
                obj._AssetContainers.append(self)
            self._LandProperties.append(obj)

    def removeLandProperties(self, *LandProperties):
        for obj in LandProperties:
            if self in obj._AssetContainers:
                obj._AssetContainers.remove(self)
            self._LandProperties.remove(obj)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for x in self._Assets:
            x._AssetContainer = None
        for y in value:
            y._AssetContainer = self
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            obj._AssetContainer = self
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            obj._AssetContainer = None
            self._Assets.remove(obj)

    def getSeals(self):
        """All seals applied to this asset container.
        """
        return self._Seals

    def setSeals(self, value):
        for x in self._Seals:
            x._AssetContainer = None
        for y in value:
            y._AssetContainer = self
        self._Seals = value

    Seals = property(getSeals, setSeals)

    def addSeals(self, *Seals):
        for obj in Seals:
            obj._AssetContainer = self
            self._Seals.append(obj)

    def removeSeals(self, *Seals):
        for obj in Seals:
            obj._AssetContainer = None
            self._Seals.remove(obj)

