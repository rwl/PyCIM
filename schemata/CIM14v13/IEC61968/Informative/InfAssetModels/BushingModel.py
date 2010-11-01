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

class BushingModel(ElectricalAssetModel):
    """Documentation for a type of a bushing of a particular product model made by a manufacturer.
    """

    def __init__(self, insulationKind='paperoil', BushingAsset=None, *args, **kw_args):
        """Initializes a new 'BushingModel' instance.

        @param insulationKind: Kind of insulation used in this bushing model. Values are: "paperoil", "compound", "other", "solidPorcelain"
        @param BushingAsset:
        """
        #: Kind of insulation used in this bushing model. Values are: "paperoil", "compound", "other", "solidPorcelain"
        self.insulationKind = insulationKind

        self._BushingAsset = None
        self.BushingAsset = BushingAsset

        super(BushingModel, self).__init__(*args, **kw_args)

    def getBushingAsset(self):
        
        return self._BushingAsset

    def setBushingAsset(self, value):
        if self._BushingAsset is not None:
            self._BushingAsset._BushingModel = None

        self._BushingAsset = value
        if self._BushingAsset is not None:
            self._BushingAsset._BushingModel = self

    BushingAsset = property(getBushingAsset, setBushingAsset)

