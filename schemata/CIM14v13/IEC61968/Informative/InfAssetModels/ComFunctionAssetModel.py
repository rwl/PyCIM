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

class ComFunctionAssetModel(ElectricalAssetModel):
    """Documentation for a type of communication function of a particular product model made by a manufacturer.
    """

    def __init__(self, ComFunctionTypeAsset=None, **kw_args):
        """Initializes a new 'ComFunctionAssetModel' instance.

        @param ComFunctionTypeAsset:
        """
        self._ComFunctionTypeAsset = None
        self.ComFunctionTypeAsset = ComFunctionTypeAsset

        super(ComFunctionAssetModel, self).__init__(**kw_args)

    def getComFunctionTypeAsset(self):
        
        return self._ComFunctionTypeAsset

    def setComFunctionTypeAsset(self, value):
        if self._ComFunctionTypeAsset is not None:
            filtered = [x for x in self.ComFunctionTypeAsset.ComFunctionAssetModels if x != self]
            self._ComFunctionTypeAsset._ComFunctionAssetModels = filtered

        self._ComFunctionTypeAsset = value
        if self._ComFunctionTypeAsset is not None:
            self._ComFunctionTypeAsset._ComFunctionAssetModels.append(self)

    ComFunctionTypeAsset = property(getComFunctionTypeAsset, setComFunctionTypeAsset)

