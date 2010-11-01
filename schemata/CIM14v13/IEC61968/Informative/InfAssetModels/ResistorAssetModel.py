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

class ResistorAssetModel(ElectricalAssetModel):
    """Documentation for a type of a resistor asset of a particular product model made by a manufacturer.
    """

    def __init__(self, ResistorTypeAsset=None, ResistorAssets=None, *args, **kw_args):
        """Initializes a new 'ResistorAssetModel' instance.

        @param ResistorTypeAsset:
        @param ResistorAssets:
        """
        self._ResistorTypeAsset = None
        self.ResistorTypeAsset = ResistorTypeAsset

        self._ResistorAssets = []
        self.ResistorAssets = [] if ResistorAssets is None else ResistorAssets

        super(ResistorAssetModel, self).__init__(*args, **kw_args)

    def getResistorTypeAsset(self):
        
        return self._ResistorTypeAsset

    def setResistorTypeAsset(self, value):
        if self._ResistorTypeAsset is not None:
            filtered = [x for x in self.ResistorTypeAsset.ResistorAssetModels if x != self]
            self._ResistorTypeAsset._ResistorAssetModels = filtered

        self._ResistorTypeAsset = value
        if self._ResistorTypeAsset is not None:
            self._ResistorTypeAsset._ResistorAssetModels.append(self)

    ResistorTypeAsset = property(getResistorTypeAsset, setResistorTypeAsset)

    def getResistorAssets(self):
        
        return self._ResistorAssets

    def setResistorAssets(self, value):
        for x in self._ResistorAssets:
            x._ResistorAssetModel = None
        for y in value:
            y._ResistorAssetModel = self
        self._ResistorAssets = value

    ResistorAssets = property(getResistorAssets, setResistorAssets)

    def addResistorAssets(self, *ResistorAssets):
        for obj in ResistorAssets:
            obj._ResistorAssetModel = self
            self._ResistorAssets.append(obj)

    def removeResistorAssets(self, *ResistorAssets):
        for obj in ResistorAssets:
            obj._ResistorAssetModel = None
            self._ResistorAssets.remove(obj)

