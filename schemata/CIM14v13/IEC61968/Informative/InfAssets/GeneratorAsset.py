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

from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset

class GeneratorAsset(ElectricalAsset):
    """Physical asset performing the Generator role.
    """

    def __init__(self, GeneratorAssetModel=None, *args, **kw_args):
        """Initializes a new 'GeneratorAsset' instance.

        @param GeneratorAssetModel:
        """
        self._GeneratorAssetModel = None
        self.GeneratorAssetModel = GeneratorAssetModel

        super(GeneratorAsset, self).__init__(*args, **kw_args)

    def getGeneratorAssetModel(self):
        
        return self._GeneratorAssetModel

    def setGeneratorAssetModel(self, value):
        if self._GeneratorAssetModel is not None:
            filtered = [x for x in self.GeneratorAssetModel.GeneratorAssets if x != self]
            self._GeneratorAssetModel._GeneratorAssets = filtered

        self._GeneratorAssetModel = value
        if self._GeneratorAssetModel is not None:
            self._GeneratorAssetModel._GeneratorAssets.append(self)

    GeneratorAssetModel = property(getGeneratorAssetModel, setGeneratorAssetModel)

