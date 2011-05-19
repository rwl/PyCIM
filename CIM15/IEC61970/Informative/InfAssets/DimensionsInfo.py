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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class DimensionsInfo(IdentifiedObject):
    """As applicable, the basic linear, area, or volume dimensions of an asset, asset type (AssetModel) or other type of object (such as land area). Units and multipliers are specified per dimension.As applicable, the basic linear, area, or volume dimensions of an asset, asset type (AssetModel) or other type of object (such as land area). Units and multipliers are specified per dimension.
    """

    def __init__(self, sizeWidth=0.0, sizeDiameter=0.0, sizeLength=0.0, orientation='', sizeDepth=0.0, Locations=None, AssetInfos=None, Specifications=None, *args, **kw_args):
        """Initialises a new 'DimensionsInfo' instance.

        @param sizeWidth: Width measurement. 
        @param sizeDiameter: Diameter measurement. 
        @param sizeLength: Length measurement. 
        @param orientation: A description of the orientation of the object relative to the dimensions. As an example, a vault may have north-south orientation for the sizeLength measurement and sizeDepth may be the height of the vault. 
        @param sizeDepth: Depth measurement. 
        @param Locations:
        @param AssetInfos:
        @param Specifications:
        """
        #: Width measurement.
        self.sizeWidth = sizeWidth

        #: Diameter measurement.
        self.sizeDiameter = sizeDiameter

        #: Length measurement.
        self.sizeLength = sizeLength

        #: A description of the orientation of the object relative to the dimensions. As an example, a vault may have north-south orientation for the sizeLength measurement and sizeDepth may be the height of the vault.
        self.orientation = orientation

        #: Depth measurement.
        self.sizeDepth = sizeDepth

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._AssetInfos = []
        self.AssetInfos = [] if AssetInfos is None else AssetInfos

        self._Specifications = []
        self.Specifications = [] if Specifications is None else Specifications

        super(DimensionsInfo, self).__init__(*args, **kw_args)

    _attrs = ["sizeWidth", "sizeDiameter", "sizeLength", "orientation", "sizeDepth"]
    _attr_types = {"sizeWidth": float, "sizeDiameter": float, "sizeLength": float, "orientation": str, "sizeDepth": float}
    _defaults = {"sizeWidth": 0.0, "sizeDiameter": 0.0, "sizeLength": 0.0, "orientation": '', "sizeDepth": 0.0}
    _enums = {}
    _refs = ["Locations", "AssetInfos", "Specifications"]
    _many_refs = ["Locations", "AssetInfos", "Specifications"]

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for x in self._Locations:
            x.DimensionsInfo = None
        for y in value:
            y._DimensionsInfo = self
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            obj.DimensionsInfo = self

    def removeLocations(self, *Locations):
        for obj in Locations:
            obj.DimensionsInfo = None

    def getAssetInfos(self):
        
        return self._AssetInfos

    def setAssetInfos(self, value):
        for x in self._AssetInfos:
            x.DimensionsInfo = None
        for y in value:
            y._DimensionsInfo = self
        self._AssetInfos = value

    AssetInfos = property(getAssetInfos, setAssetInfos)

    def addAssetInfos(self, *AssetInfos):
        for obj in AssetInfos:
            obj.DimensionsInfo = self

    def removeAssetInfos(self, *AssetInfos):
        for obj in AssetInfos:
            obj.DimensionsInfo = None

    def getSpecifications(self):
        
        return self._Specifications

    def setSpecifications(self, value):
        for p in self._Specifications:
            filtered = [q for q in p.DimensionsInfos if q != self]
            self._Specifications._DimensionsInfos = filtered
        for r in value:
            if self not in r._DimensionsInfos:
                r._DimensionsInfos.append(self)
        self._Specifications = value

    Specifications = property(getSpecifications, setSpecifications)

    def addSpecifications(self, *Specifications):
        for obj in Specifications:
            if self not in obj._DimensionsInfos:
                obj._DimensionsInfos.append(self)
            self._Specifications.append(obj)

    def removeSpecifications(self, *Specifications):
        for obj in Specifications:
            if self in obj._DimensionsInfos:
                obj._DimensionsInfos.remove(self)
            self._Specifications.remove(obj)

