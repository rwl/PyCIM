# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61968.Assets.Asset import Asset

class AssetContainer(Asset):
    """Asset that is aggregation of other assets such as conductors, transformers, switchgear, land, fences, buildings, equipment, vehicles, etc.Asset that is aggregation of other assets such as conductors, transformers, switchgear, land, fences, buildings, equipment, vehicles, etc.
    """

    def __init__(self, Seals=None, Assets=None, LandProperties=None, *args, **kw_args):
        """Initialises a new 'AssetContainer' instance.

        @param Seals: All seals applied to this asset container.
        @param Assets:
        @param LandProperties:
        """
        self._Seals = []
        self.Seals = [] if Seals is None else Seals

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._LandProperties = []
        self.LandProperties = [] if LandProperties is None else LandProperties

        super(AssetContainer, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Seals", "Assets", "LandProperties"]
    _many_refs = ["Seals", "Assets", "LandProperties"]

    def getSeals(self):
        """All seals applied to this asset container.
        """
        return self._Seals

    def setSeals(self, value):
        for x in self._Seals:
            x.AssetContainer = None
        for y in value:
            y._AssetContainer = self
        self._Seals = value

    Seals = property(getSeals, setSeals)

    def addSeals(self, *Seals):
        for obj in Seals:
            obj.AssetContainer = self

    def removeSeals(self, *Seals):
        for obj in Seals:
            obj.AssetContainer = None

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for x in self._Assets:
            x.AssetContainer = None
        for y in value:
            y._AssetContainer = self
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            obj.AssetContainer = self

    def removeAssets(self, *Assets):
        for obj in Assets:
            obj.AssetContainer = None

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

