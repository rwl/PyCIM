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

class DimensionsInfo(IdentifiedObject):
    """As applicable, the basic linear, area, or volume dimensions of an asset, asset type (AssetModel) or other type of object (such as land area). Units and multipliers are specified per dimension.
    """

    def __init__(self, sizeLength=0.0, sizeDepth=0.0, sizeDiameter=0.0, orientation='', sizeWidth=0.0, Assets=None, Specifications=None, Locations=None, *args, **kw_args):
        """Initializes a new 'DimensionsInfo' instance.

        @param sizeLength: Length measurement. 
        @param sizeDepth: Depth measurement. 
        @param sizeDiameter: Diameter measurement. 
        @param orientation: A description of the orientation of the object relative to the dimensions. As an example, a vault may have north-south orientation for the sizeLength measurement and sizeDepth may be the height of the vault. 
        @param sizeWidth: Width measurement. 
        @param Assets:
        @param Specifications:
        @param Locations:
        """
        #: Length measurement.
        self.sizeLength = sizeLength

        #: Depth measurement.
        self.sizeDepth = sizeDepth

        #: Diameter measurement.
        self.sizeDiameter = sizeDiameter

        #: A description of the orientation of the object relative to the dimensions. As an example, a vault may have north-south orientation for the sizeLength measurement and sizeDepth may be the height of the vault.
        self.orientation = orientation

        #: Width measurement.
        self.sizeWidth = sizeWidth

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._Specifications = []
        self.Specifications = [] if Specifications is None else Specifications

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        super(DimensionsInfo, self).__init__(*args, **kw_args)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for x in self._Assets:
            x._DimensionsInfo = None
        for y in value:
            y._DimensionsInfo = self
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            obj._DimensionsInfo = self
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            obj._DimensionsInfo = None
            self._Assets.remove(obj)

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

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for x in self._Locations:
            x._DimensionsInfo = None
        for y in value:
            y._DimensionsInfo = self
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            obj._DimensionsInfo = self
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            obj._DimensionsInfo = None
            self._Locations.remove(obj)

