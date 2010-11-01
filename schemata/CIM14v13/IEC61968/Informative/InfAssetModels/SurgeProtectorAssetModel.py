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

class SurgeProtectorAssetModel(ElectricalAssetModel):
    """Documentation for a type of an SurgeProtector asset of a particular product model made by a manufacturer.
    """

    def __init__(self, SurgeProtectorTypeAsset=None, SurgeProtectorAssets=None, *args, **kw_args):
        """Initializes a new 'SurgeProtectorAssetModel' instance.

        @param SurgeProtectorTypeAsset:
        @param SurgeProtectorAssets:
        """
        self._SurgeProtectorTypeAsset = None
        self.SurgeProtectorTypeAsset = SurgeProtectorTypeAsset

        self._SurgeProtectorAssets = []
        self.SurgeProtectorAssets = [] if SurgeProtectorAssets is None else SurgeProtectorAssets

        super(SurgeProtectorAssetModel, self).__init__(*args, **kw_args)

    def getSurgeProtectorTypeAsset(self):
        
        return self._SurgeProtectorTypeAsset

    def setSurgeProtectorTypeAsset(self, value):
        if self._SurgeProtectorTypeAsset is not None:
            filtered = [x for x in self.SurgeProtectorTypeAsset.SurgeProtectorAssetModels if x != self]
            self._SurgeProtectorTypeAsset._SurgeProtectorAssetModels = filtered

        self._SurgeProtectorTypeAsset = value
        if self._SurgeProtectorTypeAsset is not None:
            self._SurgeProtectorTypeAsset._SurgeProtectorAssetModels.append(self)

    SurgeProtectorTypeAsset = property(getSurgeProtectorTypeAsset, setSurgeProtectorTypeAsset)

    def getSurgeProtectorAssets(self):
        
        return self._SurgeProtectorAssets

    def setSurgeProtectorAssets(self, value):
        for x in self._SurgeProtectorAssets:
            x._SurgeProtectorAssetModel = None
        for y in value:
            y._SurgeProtectorAssetModel = self
        self._SurgeProtectorAssets = value

    SurgeProtectorAssets = property(getSurgeProtectorAssets, setSurgeProtectorAssets)

    def addSurgeProtectorAssets(self, *SurgeProtectorAssets):
        for obj in SurgeProtectorAssets:
            obj._SurgeProtectorAssetModel = self
            self._SurgeProtectorAssets.append(obj)

    def removeSurgeProtectorAssets(self, *SurgeProtectorAssets):
        for obj in SurgeProtectorAssets:
            obj._SurgeProtectorAssetModel = None
            self._SurgeProtectorAssets.remove(obj)

