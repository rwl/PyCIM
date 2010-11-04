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

class GeneratorAssetModel(ElectricalAssetModel):
    """Documentation for a type of generation equipment of a particular product model made by a manufacturer.
    """

    def __init__(self, GeneratorAssets=None, GeneratorTypeAsset=None, **kw_args):
        """Initializes a new 'GeneratorAssetModel' instance.

        @param GeneratorAssets:
        @param GeneratorTypeAsset:
        """
        self._GeneratorAssets = []
        self.GeneratorAssets = [] if GeneratorAssets is None else GeneratorAssets

        self._GeneratorTypeAsset = None
        self.GeneratorTypeAsset = GeneratorTypeAsset

        super(GeneratorAssetModel, self).__init__(**kw_args)

    def getGeneratorAssets(self):
        
        return self._GeneratorAssets

    def setGeneratorAssets(self, value):
        for x in self._GeneratorAssets:
            x._GeneratorAssetModel = None
        for y in value:
            y._GeneratorAssetModel = self
        self._GeneratorAssets = value

    GeneratorAssets = property(getGeneratorAssets, setGeneratorAssets)

    def addGeneratorAssets(self, *GeneratorAssets):
        for obj in GeneratorAssets:
            obj._GeneratorAssetModel = self
            self._GeneratorAssets.append(obj)

    def removeGeneratorAssets(self, *GeneratorAssets):
        for obj in GeneratorAssets:
            obj._GeneratorAssetModel = None
            self._GeneratorAssets.remove(obj)

    def getGeneratorTypeAsset(self):
        
        return self._GeneratorTypeAsset

    def setGeneratorTypeAsset(self, value):
        if self._GeneratorTypeAsset is not None:
            filtered = [x for x in self.GeneratorTypeAsset.GeneratorAssetModels if x != self]
            self._GeneratorTypeAsset._GeneratorAssetModels = filtered

        self._GeneratorTypeAsset = value
        if self._GeneratorTypeAsset is not None:
            self._GeneratorTypeAsset._GeneratorAssetModels.append(self)

    GeneratorTypeAsset = property(getGeneratorTypeAsset, setGeneratorTypeAsset)

