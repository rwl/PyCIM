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

from CIM14v13.IEC61968.Informative.InfAssetModels.ElectricalAssetModel import ElectricalAssetModel

class StreetlightAssetModel(ElectricalAssetModel):
    """Documentation for a type of a streelight of a particular product model made by a manufacturer.
    """

    def __init__(self, lampKind='highPressureSodium', lightRating=0.0, Streetlights=None, StreetlightTypeAssets=None, *args, **kw_args):
        """Initializes a new 'StreetlightAssetModel' instance.

        @param lampKind: Lamp kind supplied from manufacturer (vs. one that has been replaced in the field). Values are: "highPressureSodium", "other", "metalHalide", "mercuryVapor"
        @param lightRating: Power rating of light as supplied by the manufacturer. 
        @param Streetlights:
        @param StreetlightTypeAssets:
        """
        #: Lamp kind supplied from manufacturer (vs. one that has been replaced in the field). Values are: "highPressureSodium", "other", "metalHalide", "mercuryVapor"
        self.lampKind = lampKind

        #: Power rating of light as supplied by the manufacturer. 
        self.lightRating = lightRating

        self._Streetlights = []
        self.Streetlights = [] if Streetlights is None else Streetlights

        self._StreetlightTypeAssets = []
        self.StreetlightTypeAssets = [] if StreetlightTypeAssets is None else StreetlightTypeAssets

        super(StreetlightAssetModel, self).__init__(*args, **kw_args)

    def getStreetlights(self):
        
        return self._Streetlights

    def setStreetlights(self, value):
        for x in self._Streetlights:
            x._StreetlightAssetModel = None
        for y in value:
            y._StreetlightAssetModel = self
        self._Streetlights = value

    Streetlights = property(getStreetlights, setStreetlights)

    def addStreetlights(self, *Streetlights):
        for obj in Streetlights:
            obj._StreetlightAssetModel = self
            self._Streetlights.append(obj)

    def removeStreetlights(self, *Streetlights):
        for obj in Streetlights:
            obj._StreetlightAssetModel = None
            self._Streetlights.remove(obj)

    def getStreetlightTypeAssets(self):
        
        return self._StreetlightTypeAssets

    def setStreetlightTypeAssets(self, value):
        for p in self._StreetlightTypeAssets:
            filtered = [q for q in p.StreetlightAssetModels if q != self]
            self._StreetlightTypeAssets._StreetlightAssetModels = filtered
        for r in value:
            if self not in r._StreetlightAssetModels:
                r._StreetlightAssetModels.append(self)
        self._StreetlightTypeAssets = value

    StreetlightTypeAssets = property(getStreetlightTypeAssets, setStreetlightTypeAssets)

    def addStreetlightTypeAssets(self, *StreetlightTypeAssets):
        for obj in StreetlightTypeAssets:
            if self not in obj._StreetlightAssetModels:
                obj._StreetlightAssetModels.append(self)
            self._StreetlightTypeAssets.append(obj)

    def removeStreetlightTypeAssets(self, *StreetlightTypeAssets):
        for obj in StreetlightTypeAssets:
            if self in obj._StreetlightAssetModels:
                obj._StreetlightAssetModels.remove(self)
            self._StreetlightTypeAssets.remove(obj)

