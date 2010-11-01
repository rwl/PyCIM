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

from CIM14v13.IEC61968.Informative.InfTypeAsset.ElectricalTypeAsset import ElectricalTypeAsset

class ComFunctionTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic communication function that may be used for various purposes such as work planning.
    """

    def __init__(self, ComFunctionAssetModels=None, *args, **kw_args):
        """Initializes a new 'ComFunctionTypeAsset' instance.

        @param ComFunctionAssetModels:
        """
        self._ComFunctionAssetModels = []
        self.ComFunctionAssetModels = [] if ComFunctionAssetModels is None else ComFunctionAssetModels

        super(ComFunctionTypeAsset, self).__init__(*args, **kw_args)

    def getComFunctionAssetModels(self):
        
        return self._ComFunctionAssetModels

    def setComFunctionAssetModels(self, value):
        for x in self._ComFunctionAssetModels:
            x._ComFunctionTypeAsset = None
        for y in value:
            y._ComFunctionTypeAsset = self
        self._ComFunctionAssetModels = value

    ComFunctionAssetModels = property(getComFunctionAssetModels, setComFunctionAssetModels)

    def addComFunctionAssetModels(self, *ComFunctionAssetModels):
        for obj in ComFunctionAssetModels:
            obj._ComFunctionTypeAsset = self
            self._ComFunctionAssetModels.append(obj)

    def removeComFunctionAssetModels(self, *ComFunctionAssetModels):
        for obj in ComFunctionAssetModels:
            obj._ComFunctionTypeAsset = None
            self._ComFunctionAssetModels.remove(obj)

